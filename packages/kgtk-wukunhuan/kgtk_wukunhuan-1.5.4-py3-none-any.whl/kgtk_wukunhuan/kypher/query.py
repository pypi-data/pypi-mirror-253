"""
Kypher queries over KGTK graphs.
"""

import sys
import os.path
import io
import re
import time
import itertools
import copy

import sh
from   odictliteral import odict

from   kgtk_wukunhuan.exceptions import KGTKException
import kgtk_wukunhuan.kypher.parser as parser
import kgtk_wukunhuan.kypher.sqlstore as ss
from   kgtk_wukunhuan.kypher.utils import *
import kgtk_wukunhuan.kypher.indexspec as ispec
from   kgtk_wukunhuan.kypher.functions import SqlFunction


### TO DO:

# - support node property access without having to introduce the property variable in the
#   match clause first (e.g., y.salary in the multi-graph join example)
# + support parameters in lists
# + support concat function (|| operator in sqlite)
# - maybe support positional parameters $0, $1,...
# - intelligent interpretation of ^ and $ when regex-matching to string literals?
#   - one can use kgtk_unstringify first to get to the text content
# - allow |-alternatives in relationship and node patterns (the latter being an
#   extension to Cypher)
# - more intelligent index creation
# - investigate redundant join clauses
# - header column dealiasing/normalization, checking for required columns
# - bump graph timestamps when they get queried
# + allow order-by on column aliases (currently they are undefined variables)
# + (not) exists pattern handling
# + null-value handling and testing
# - handle properties that are ambiguous across graphs
# + graphs fed in from stdin
# + graph naming independent from files, so we don't have to have source data files
#   available after import for querying, e.g.: ... -i $FILE1 --as g1 -i $FILE2 --as g2 ...
# + with named graphs, we probably also need some kind of --info command to list content
# + investigate Cyphers multiple distinct match clauses more thoroughly; apparently, a
#   difference is that in a single pattern, each relationship must match a different edge
#   which is kind of like UVBR in SNePS, but in multiple match patterns that restriction
#   is only enforced within each match clauses's pattern.  This means if we don't enforce
#   the uniqueness principle, multiple strict match clauses do not add anything
# + optional match clauses need to allow multiple ones so they can fail individually
# - --create and --remove to instantiate and add/remove edge patterns from result bindings
# - --with clause to compute derived values to use by --create and --remove


### Utilities

def dwim_to_string_para(x):
    """Try to coerce 'x' to a KGTK string value that can be passed as a query parameter.
    """
    from kgtk_wukunhuan.value.kgtkvalue import KgtkValue # expensive: 120ms
    x = str(x)
    m = KgtkValue.strict_string_re.match(x)
    if m is not None:
        return x
    # if we have an enclosing pair of quotes, remove them:
    if x.startswith('"') and x.endswith('"'):
        x = x[1:-1]
    x = re.sub(r'(?P<char>["\|])', r'\\\g<char>', x)
    return '"%s"' % x

def dwim_to_lqstring_para(x):
    """Try to coerce 'x' to a KGTK LQ-string value that can be passed as a query parameter.
    """
    from kgtk_wukunhuan.value.kgtkvalue import KgtkValue # expensive: 120ms
    x = str(x)
    m = KgtkValue.strict_language_qualified_string_re.match(x)
    if m is not None:
        return x
    atpos = x.rfind('@')
    if atpos > 0:
        text = x[0:atpos]
        # this allows an empty or invalid language:
        lang = x[atpos+1:]
        # if we have an enclosing pair of quotes, remove them:
        if text.startswith("'") and text.endswith("'"):
            text = text[1:-1]
        text = re.sub(r"(?P<char>['\|])", r'\\\g<char>', text)
        return "'%s'@%s" % (text, lang)
    raise KGTKException("cannot coerce '%s' into a language-qualified string" % x)


### Query translation:

# An expression in Kypher can be ('+' means handled fully, 'o' partially):
# (from https://neo4j.com/docs/cypher-manual/current/syntax/expressions/)
#
# + A decimal (integer or float) literal: 13, -40000, 3.14, 6.022E23.
# + A hexadecimal integer literal (starting with 0x): 0x13af, 0xFC3A9, -0x66eff
#   - HC: get converted into decimal
# + An octal integer literal (starting with 0): 01372, 02127, -05671.
#   - HC: get converted into decimal
# + A string literal: 'Hello', "World".
# + A boolean literal: true, false, TRUE, FALSE.
#   - HC: get converted into 0/1
# + A variable: n, x, rel, myFancyVariable, `A name with weird stuff in it[]!`.
# + A property: n.prop, x.prop, rel.thisProperty, myFancyVariable.`(weird property name)`
# - A dynamic property: n["prop"], rel[n.city + n.zip], map[coll[0]].
#   - HC: not doable in SQL, amounts to a function or column variable
# + A parameter: $param, $0
# + A list of expressions: ['a', 'b'], [1, 2, 3], ['a', 2, n.property, $param], [ ].
#   - HC: only lists of literals
# + A function call: length(p), nodes(p).
# + An aggregate function: avg(x.prop), count(*).
# + A path-pattern: (a)-->()<--(b).
# + An operator application: 1 + 2 and 3 < 4.
# + A predicate expression is an expression that returns true or false: a.prop = 'Hello', length(p) > 10, exists(a.name).
# + An existential subquery is an expression that returns true or false: EXISTS { MATCH (n)-[r]→(p) WHERE p.name = 'Sven' }.
# + A regular expression: a.name =~ 'Tim.*'
#   - HC: SQLite supports LIKE and GLOB (which both have different regexp syntax),
#     and REGEXP and MATCH through user-defined functions (we support =~ via kgtk_regex)
# - A case-sensitive string matching expression: a.surname STARTS WITH 'Sven', a.surname ENDS WITH 'son' or a.surname CONTAINS 'son'
#   - HC: would need to be implemented via a user-defined function
# - A CASE expression.

# Using properties to restrict on "wide" columns:
#
# Example - unrestricted:
#
#    (a)-[:loves]->(b)
#
# Example - qualified:
#
#    (a {nationality: "Austria"})-[:loves]->(b)
#
# This could mean:
#    {'node1': <Variable a>, 'node1;nationality': "Austria", 'label': "loves", 'node2': <Variable b>}
#
#    (a)-[:loves {graph: "g1"}]->(b)
#
# This could mean:
#    {'node1': <Variable a>, 'label': "loves", 'graph': "g1", 'node2': <Variable b>}
#
# Assumption: if we access something via a property, it will always be accessed via a column,
# not via a normalized edge; if data has mixed representation for some edges, it has to be
# normalized one way or the other first for the query to get all results.  If not, it will
# only pick up the representation used in the query, other edges will be ignored.
#
# For structured literals, we assume their fields are implied/virtual wide columns that aren't
# materialized.  For example:
#
#    (id)-[:P580]->(time {`kgtk:year`: year})
#    where year <= 2010
#
# which would be the same as (if we named the accessors like our column names):
#
#    (id)-[:P580]->(time)
#    where kgtk_year(time) <= 2010


class KgtkQuery(object):

    def __init__(self, files, store, options=None, query=None,
                 match='()', where=None, optionals=None, with_=None,
                 ret='*', order=None, skip=None, limit=None, multi=None,
                 parameters={}, index='auto', force=False, dont_optimize=False,
                 loglevel=0):
        self.options = options or {}
        self.store = store
        self.loglevel = loglevel
        self.force = force
        self.parameters = parameters
        self.defer_params = False
        self.index_mode = index
        
        if query is None:
            # supplying a query through individual clause arguments is a little bit easier,
            # since they can be in any order, can have defaults, are easier to shell-quote, etc.:
            query = io.StringIO()
            # for now we allow/require exactly one strict match pattern, even though in Cypher
            # there could be any number and conceivably optionals could come before strict:
            match and query.write(' MATCH ' + match)
            where and query.write(' WHERE ' + where)
            # optionals is a list of match pattern/where pairs, where single-element lists can be atoms:
            for omatch in listify(optionals):
                omatch = listify(omatch)
                query.write(' OPTIONAL MATCH ' + omatch[0])
                if len(omatch) > 1 and omatch[1] is not None:
                    query.write(' WHERE ' + omatch[1])
            # with_ is a single (vars, where) tuple, where a single-element atom/list
            # is interpreted as the variables clause to a 'with <vars>...':
            if with_ is not None:
                with_ = listify(with_) + [None]
                query.write(' WITH ' + with_[0])
                with_[1] and query.write(' WHERE ' + with_[1])
            ret and query.write(' RETURN ' + ret)
            order and query.write(' ORDER BY ' + order)
            skip and query.write(' SKIP ' + str(skip))
            limit and query.write(' LIMIT ' + str(limit))
            query = query.getvalue()
        self.log(2, 'Kypher:' + query)
        
        self.query = parser.intern(query)
        self.match_clause = self.query.get_match_clause()
        self.optional_clauses = self.query.get_optional_match_clauses()
        self.with_clause = self.query.get_with_clause()
        self.return_clause = self.query.get_return_clause()
        self.order_clause = self.query.get_order_clause()
        self.skip_clause = self.query.get_skip_clause()
        self.limit_clause = self.query.get_limit_clause()
        if multi is not None and multi < 1:
            raise KGTKException(f'Illegal multi-edge value: {multi}')
        self.multi_edge = multi
        self.dont_optimize = dont_optimize
        
        # process/import files after we parsed the query, so we get syntax errors right away:
        self.files = []
        for file in listify(files):
            file = str(file) # in case we get a path object
            alias = self.get_input_option(file, 'alias')
            comment = self.get_input_option(file, 'comment')
            index_specs = self.get_input_option(file, 'index_specs')
            append_files = self.get_input_option(file, 'append')
            store.add_graph(file, alias=alias, index_specs=index_specs, append=append_files)
            # use aliases for handle matching, otherwise unnormalized files except for stdin:
            norm_file = store.get_normalized_file(file, alias=alias)
            if store.is_standard_input(file):
                file = norm_file
            self.files.append(alias or file)
            comment is not None and store.set_file_comment(norm_file, comment)
            
        self.default_graph = self.files[0]
        self.graph_handle_map = {}
        self.result_header = None
        self.translation_iter = None

    def reset(self):
        """Reset all slots that are computed during translation back to their original values.
        """
        # TO DO: it is assumed that any caller that needs retranslation massages the initial
        # state created by __init__() into something that can then be used appropriately for
        # a re-run, but we might need more fine-grained reset/reinit methods down the line
        self.graph_handle_map = {}
        self.result_header = None
        self.translation_iter = None

    def get_input_option(self, file, option, dflt=None):
        for input, opts in self.options.items():
            if input == file or opts.get('alias') == file:
                return opts.get(option, dflt)
        return dflt

    def log(self, level, message):
        if self.loglevel >= level:
            header = '[%s query]:' % time.strftime('%Y-%m-%d %H:%M:%S')
            sys.stderr.write('%s %s\n' % (header, message))
            sys.stderr.flush()

    def map_graph_handle_to_file(self, handle):
        """Performes a greedy mapping of 'handle' to either a full file name
        or the first file basename that contains 'handle' as a substring.
        If handle contains a numeric suffix, we also check its prefix portion.
        For example, handle 'g12' is also matched as 'g' in the file basename.
        """
        files = self.files
        hmap = self.graph_handle_map
        if handle in hmap:
            return hmap[handle]
        base_handle = handle
        m = re.search(r'[0-9]+$', handle)
        if m is not None and m.start() > 0:
            base_handle = handle[0:m.start()]
        mapped_files = hmap.values()
        # don't do this: it would allow the default graph to be remapped to an explicit
        # handle, but that would change the handle semantics for existing queries:
        # mapped_files = [f for h, f in hmap.items() if h != f or h != self.default_graph]
        for file in files:
            if file not in mapped_files:
                key = file
                if handle == key:
                    hmap[handle] = file
                    return file
                key = os.path.basename(file)
                if key.find(handle) >= 0 or key.find(base_handle) >= 0:
                    hmap[handle] = file
                    return file
        # also don't do this which is the converse of the above: it would allow an implicit
        # graph handle to be remapped to a file that was already explicitly mapped before
        # (we clarified implicit mapping of the default graph in the documentation):
        # if handle == self.default_graph:
        #     file = self.default_graph
        #     hmap[handle] = file
        #     return file
        raise KGTKException("failed to uniquely map handle '%s' onto one of %s" % (handle, files))

    def get_parameter_value(self, name):
        value = self.parameters.get(name)
        if value is None:
            if self.defer_params:
                # value will be provided later, just use the parameter name as its value for now;
                # we use a single-element tuple to mark it as a place holder:
                value = (name,)
                self.parameters[name] = value
            else:
                raise KGTKException("undefined query parameter: '%s'" % name)
        return value

    def get_pattern_clause_graph(self, clause):
        """Return the graph table for this 'clause', initialize it if necessary.
        """
        node1 = clause[0]
        if hasattr(node1, '_graph_table'):
            return node1._graph_table
        graph = node1.graph
        if graph is not None:
            # TO DO: register these graph variables so we can use them later to disambiguate
            # graph-table-specific property expressions or rowid() calls on join variables:
            graph = graph.name
        else:
            graph = self.default_graph
        node1._graph_table = self.store.get_file_graph(self.map_graph_handle_to_file(graph))
        return node1._graph_table

    def get_pattern_clause_graph_alias(self, clause):
        """Return the graph table alias for this 'clause', initialize it if necessary.
        """
        # assumes self.init_match_clauses() has been called:
        node1 = clause[0]
        return node1._graph_alias
    
    def get_pattern_clause_match_clause(self, clause):
        """Return the match clause this pattern 'clause' belongs to.
        """
        node1 = clause[0]
        # now this backpointer is always added by the parser:
        return node1._match_clause
    
    # in case we have aliases which could be different in every graph, stubs for now:
    def get_node1_column(self, graph):
        return 'node1'
    def get_node2_column(self, graph):
        return 'node2'
    def get_label_column(self, graph):
        return 'label'
    def get_id_column(self, graph):
        return 'id'
    def get_edge_columns(self, graph):
        return ('id', 'node1', 'label', 'node2')
        
    def pattern_clause_to_sql(self, clause, graph, state):
        node1 = clause[0]
        rel = clause[1]
        node2 = clause[2]

        if rel.labels is not None and SqlFunction.is_virtual_graph(rel.labels[0]):
            # special-case translation of virtual graph pattern clauses:
            vgraph = rel.labels[0]
            vgraphfn = SqlFunction.get_function(vgraph, store=self.store)
            vgraphfn.translate_call_to_sql(self, clause, state)
            # in case the translator already called 'load':
            state.register_vtable(vgraphfn.get_name(), vgraphfn)
            vgraphfn.load()
            state.register_vtable(vgraphfn.get_name(), vgraphfn)
            return
        
        node1col = self.get_node1_column(graph)
        if node1.labels is not None:
            para = state.get_literal_parameter(node1.labels[0])
            state.add_match_clause_restriction((graph, node1col), para)
        # we do not exclude anonymous vars here, since they can connect edges: <-[]-()-[]->
        if node1.variable is not None:
            state.register_clause_variable(node1.variable.name, (graph, node1col))

        node2col = self.get_node2_column(graph)
        if node2.labels is not None:
            para = state.get_literal_parameter(node2.labels[0])
            state.add_match_clause_restriction((graph, node2col), para)
        # we do not exclude anonymous vars here (see above):
        if node2.variable is not None:
            state.register_clause_variable(node2.variable.name, (graph, node2col))
            
        labelcol = self.get_label_column(graph)
        idcol = self.get_id_column(graph)
        if rel.labels is not None:
            para = state.get_literal_parameter(rel.labels[0])
            state.add_match_clause_restriction((graph, labelcol), para)
        # but an anonymous relation variable cannot connect to anything else:
        if rel.variable is not None and not isinstance(rel.variable, parser.AnonymousVariable):
            state.register_clause_variable(rel.variable.name, (graph, idcol))

    def pattern_props_to_sql(self, pattern, graph, column, state):
        # 'pattern' is a node or relationship pattern for 'graph.column'.  'column' should be 'node1', 'node2' or 'id'.
        props = getattr(pattern, 'properties', None)
        if props is None or len(props) == 0:
            return
        # if we need to access a property, we need to register anonymous variables as well:
        state.register_clause_variable(pattern.variable.name, (graph, column))
        for prop, expr in props.items():
            # TO DO: figure out how to better abstract property to column mapping (also see below):
            propcol = isinstance(pattern, parser.RelationshipPattern) and prop  or  column + ';' + prop
            # TRICKY/TO DO: if the property value is a standalone variable, we register it as a free
            # variable before evaluating it, since properties can be ambiguous across different graphs
            # and only within a clause do we know which graph is actually meant.  Think about this
            # some more, this issue comes up in the time-machine use case:
            if isinstance(expr, parser.Variable):
                state.register_clause_variable(expr.name, (graph, propcol))
            expr = self.expression_to_sql(expr, state)
            state.add_match_clause_restriction((graph, propcol), expr)

    def pattern_clause_props_to_sql(self, clause, graph, state):
        node1 = clause[0]
        node1col = self.get_node1_column(graph)
        self.pattern_props_to_sql(node1, graph, node1col, state)
        node2 = clause[2]
        node2col = self.get_node2_column(graph)
        self.pattern_props_to_sql(node2, graph, node2col, state)
        rel = clause[1]
        idcol = self.get_id_column(graph)
        self.pattern_props_to_sql(rel, graph, idcol, state)

    OPERATOR_TABLE = {
        parser.Add: '+', parser.Sub: '-', parser.Multi: '*', parser.Div: '/', parser.Mod: '%',
        parser.Eq: '=', parser.Neq: '!=', parser.Lt: '<', parser.Gt: '>',
        parser.Lte: '<=', parser.Gte: '>=',
        parser.Not: 'NOT', parser.And: 'AND', parser.Or: 'OR',
    }

    def is_kgtk_operator(self, op):
        """Return True if 'op' is a special KGTK function or virtual property.
        """
        return str(op).upper().startswith('KGTK_')

    def variable_to_sql(self, expr, state):
        """Translate the variable 'expr' into the corresponding graph (alias), column and SQL.
        The graph component might be None for special variables such as '*' or aliases.
        """
        query_var = expr.name
        if query_var == '*':
            return None, query_var, query_var
        sql_vars = state.lookup_variable(query_var, error=True)
        # we allow regular and alias variables of the same name, but once an alias
        # of name 'x' is defined, it will shadow access to any regular variable 'x':
        for graph, col in sql_vars:
            if graph == self.ALIAS_GRAPH:
                # variable names a return column alias, rename it apart to avoid name conflicts:
                column = self.alias_column_name(col)
                return None, column, sql_quote_ident(column)
                
        # if we are currently translating a match clause, use a clause-local reference
        # if possible, to do the right thing for where conditions of optional clauses
        # (a restriction needs to be evaluated relative to the local optional match pattern
        # *before* a restricted variable gets joined with a strict match somewhere -
        # see unit test 'test_kgtk_query_optional_where_vars_are_local()'):
        graph = None
        if state.get_match_clause():
            for vg, vc in sql_vars:
                for gt, ga in self.get_match_clause_graphs(state.get_match_clause()):
                    if vg == ga:
                        graph, column = vg, vc
                        break
                if graph is not None:
                    break
        if graph is None:
            # otherwise, pick the representative from the set of equiv-joined column vars,
            # which corresponds to the graph alias and column name used by the first reference:
            graph, column = sql_vars[0]

        table = state.get_alias_table(graph)
        if self.store.is_vector_column(table, column):
            return graph, column, self.store.vector_column_to_sql(table, column, table_alias=graph)
        return graph, column, f'{graph}.{sql_quote_ident(column)}'

    def property_to_sql(self, expr, state):
        """Translate the property lookup expression 'expr' into the corresponding
        graph (alias), column name and SQL translation.
        """
        assert isinstance(expr, parser.Expression2), f'Not a property lookup expression: {expr}'
        arg1 = expr.arg1
        arg2 = expr.arg2
        if isinstance(arg1, parser.Variable):
            graph, column, sql = self.variable_to_sql(arg1, state)
            for proplook in arg2:
                if not isinstance(proplook, parser.PropertyLookup):
                    break # error
                prop = proplook.property
                if self.is_kgtk_operator(prop) and SqlFunction.is_defined(prop):
                    sqlfn = SqlFunction.get_function(prop, store=self.store)
                    sqlfn.load()
                    sql = f'{sqlfn.get_name()}({sql})'
                elif column == self.get_id_column(graph):
                    # we are referring to the relation ID, subsitute it with the prop column:
                    sql = sql[:-(len(column)+1)] + prop + '"'
                    column = prop
                else:
                    # we must be referring to a node-path column such as node1;name or node2;creator:
                    # TO DO: check existance of column here instead of waiting for SQLite to error
                    column += (';' + prop)
                    sql = sql[:-1] + ';' + prop + '"'
            else:
                return graph, column, sql
        raise KGTKException("Unhandled property lookup expression: " + str(expr))

    def function_call_to_sql(self, expr, state):
        function = expr.function
        if is_text_match_operator(function):
            # TO DO: consider moving this into the function API as well:
            return translate_text_match_op_to_sql(self, expr, state)
        elif SqlFunction.is_defined(function):
            # use generalized SQL function API:
            sqlfn = SqlFunction.get_function(function, store=self.store)
            return sqlfn.translate_call_to_sql(self, expr, state)
        elif function.upper() == 'EXISTS':
            # illegal arguments duped the grammar to translate this into an actual function call:
            raise KGTKException("Illegal 'EXISTS' function call")
        # otherwise, assume it is some non-special SQL built-in function,
        # if it isn't, the database will complain later during execution:
        args = [self.expression_to_sql(arg, state) for arg in expr.args]
        distinct = expr.distinct and 'DISTINCT ' or ''
        return f'{function}({distinct}{", ".join(args)})'

    def exists_subquery_to_sql(self, match_clause, state):
        """Translate an 'EXISTS {<pattern> [where]}' subquery 'match_clause' into an SQL condition.
        Different from Cypher, our <pattern> can have multiple parts separated by commas and can
        be graph-qualified.  EXISTS is handled very similar to --match and --opt clauses except that
        it is an expression.
        """
        try:
            # TO DO: this mirrors parts of 'translate_to_sql()', figure out whether we can
            #        refactor some of this logic into a more general functionality
            nvars = len([x for x in state.variable_map if not self.query.is_anonymous_variable(x)])
            state.push_subquery()
            state.set_match_clause(match_clause)

            explicit = isinstance(match_clause, parser.ExplicitExistsExpression)
            if len(match_clause.pattern) > 1 and not explicit:
                raise KGTKException("Need explicit 'EXISTS' subquery for comma-chained patterns")

            # register clause top-level info such as variables and restrictions:
            for clause in match_clause.get_pattern_clauses():
                graph_alias = self.get_pattern_clause_graph_alias(clause)
                self.pattern_clause_to_sql(clause, graph_alias, state)
            for clause in match_clause.get_pattern_clauses():
                graph_alias = self.get_pattern_clause_graph_alias(clause)
                self.pattern_clause_props_to_sql(clause, graph_alias, state)

            nvars -= len([x for x in state.variable_map if not self.query.is_anonymous_variable(x)])
            if nvars != 0 and not explicit:
                # in unmarked patterns and the EXISTS function, we are only allowed to reference existing vars:
                raise KGTKException("Need explicit 'EXISTS' subquery to introduce new pattern variables")

            sources, joined, int_condition, ext_condition = self.match_clause_to_sql(match_clause, state)
            aux_tables = list(state.get_match_clause_aux_tables(match_clause))
        
            sql = f'EXISTS (SELECT 1 FROM {self.graph_names_to_sql_join(sources + list(joined) + aux_tables)}'
            if int_condition or ext_condition:
                sql += f' WHERE {" AND ".join(listify(ext_condition) + listify(int_condition))}'
            sql += ')'
            return sql
        finally:
            state.set_match_clause(None)
            state.pop_subquery()

    def expression_to_sql(self, expr, state):
        """Translate a Kypher expression 'expr' into its SQL equivalent.
        """
        expr_type = type(expr)
        if expr_type == parser.Literal:
            return state.get_literal_parameter(expr.value)
        elif expr_type == parser.Parameter:
            value = self.get_parameter_value(expr.name)
            return state.get_literal_parameter(value)
        
        elif expr_type == parser.Variable:
            graph, column, sql = self.variable_to_sql(expr, state)
            return sql
        
        elif expr_type == parser.List:
            # we only allow literals in lists, Cypher also supports variables:
            state.disable_variables()
            elements = [self.expression_to_sql(elt, state) for elt in expr.elements]
            state.enable_variables()
            return '(' + ', '.join(elements) + ')'
        
        elif expr_type == parser.Minus:
            arg = self.expression_to_sql(expr.arg, state)
            return '(- %s)' % arg
        elif expr_type in (parser.Add, parser.Sub, parser.Multi, parser.Div, parser.Mod):
            arg1 = self.expression_to_sql(expr.arg1, state)
            arg2 = self.expression_to_sql(expr.arg2, state)
            op = self.OPERATOR_TABLE[expr_type]
            return '(%s %s %s)' % (arg1, op, arg2)
        elif expr_type == parser.Hat:
            raise KGTKException("Unsupported operator: '^'")
        
        elif expr_type in (parser.Eq, parser.Neq, parser.Lt, parser.Gt, parser.Lte, parser.Gte):
            arg1 = self.expression_to_sql(expr.arg1, state)
            arg2 = self.expression_to_sql(expr.arg2, state)
            op = self.OPERATOR_TABLE[expr_type]
            return '(%s %s %s)' % (arg1, op, arg2)
        elif expr_type == parser.Not:
            arg = self.expression_to_sql(expr.arg, state)
            return '(NOT %s)' % arg
        elif expr_type in (parser.And, parser.Or):
            arg1 = self.expression_to_sql(expr.arg1, state)
            arg2 = self.expression_to_sql(expr.arg2, state)
            op = self.OPERATOR_TABLE[expr_type]
            return '(%s %s %s)' % (arg1, op, arg2)
        elif expr_type == parser.Xor:
            raise KGTKException("Unsupported operator: 'XOR'")
        elif expr_type == parser.Case:
            # TO DO: implement, has the same syntax as SQL:
            raise KGTKException("Unsupported operator: 'CASE'")
        
        elif expr_type == parser.Call:
            return self.function_call_to_sql(expr, state)
        
        elif expr_type == parser.Expression2:
            graph, column, sql = self.property_to_sql(expr, state)
            return sql
        
        elif expr_type == parser.Expression3:
            arg1 = self.expression_to_sql(expr.arg1, state)
            op = expr.operator.upper()
            if op in ('IS_NULL', 'IS_NOT_NULL'):
                return '(%s %s)' % (arg1, op.replace('_', ' '))
            if expr.arg2 is None:
                raise KGTKException('Unhandled operator: %s' % str(op))
            arg2 = self.expression_to_sql(expr.arg2, state)
            if op in ('IN'):
                return '(%s %s %s)' % (arg1, op, arg2)
            elif op in ('REGEX'):
                sqlfn = SqlFunction.get_function('KGTK_REGEX', store=self.store)
                sqlfn.load()
                return f'{sqlfn.get_name()}({arg1}, {arg2})'
            else:
                raise KGTKException('Unhandled operator: %s' % str(op))

        elif issubclass(expr_type, parser.ExistsExpression):
            # both implicit and explicit EXISTS expressions are translated into subqueries:
            return self.exists_subquery_to_sql(expr, state)

        else:
            raise KGTKException('Unhandled expression type: %s' % str(parser.object_to_tree(expr)))

    def where_clause_to_sql(self, where_clause, state):
        if where_clause is None:
            return ''
        else:
            return self.expression_to_sql(where_clause.expression, state)

    ALIAS_GRAPH = '_'
    ALIAS_COLUMN_PREFIX = '_aLias.'

    def alias_column_name(self, column):
        """Rename an alias 'column' apart so it doesn't conflict with any data table column names.
        """
        # for now we simply prepend this prefix, a more thorough solution would look at actual
        # table columns to make sure none of the column names starts with the prefix:
        return self.ALIAS_COLUMN_PREFIX + column

    def unalias_column_name(self, column):
        """If 'column' is a renamed alias, unrename it; otherwise leave it unmodified.
        """
        return column.startswith(self.ALIAS_COLUMN_PREFIX) and column[len(self.ALIAS_COLUMN_PREFIX):] or column

    def return_clause_to_sql_selection(self, clause, state):
        select = clause.distinct and 'DISTINCT ' or ''
        first = True
        # Cypher does not have a 'GROUP BY' clause but instead uses non-aggregate return columns
        # that precede an aggregate function as grouping keys, so we have to keep track of those:
        agg_info = []
        for item in clause.items:
            expr = self.expression_to_sql(item.expression, state)
            select += first and expr or (', ' + expr)
            first = False
            # check if this item calls an aggregation function or not: if it does then preceding columns
            # that aren't aggregates are used for grouping, if it doesn't this column might be used for grouping:
            is_agg = parser.has_element(
                item.expression, lambda x: isinstance(x, parser.Call) and SqlFunction.is_aggregate(x.function))
            if item.name is not None:
                # we create an alias variable object here, so we can evaluate it for proper renaming:
                alias_var = parser.Variable(item._query, item.name)
                # we have to register the alias as a variable, otherwise it can't be referenced in --order-by,
                # but it is not tied to a specific graph table, thus that part is ALIAS_GRAPH below:
                state.register_clause_variable(item.name, (self.ALIAS_GRAPH, item.name), nojoins=True)
                sql_alias = self.expression_to_sql(alias_var, state)
                select += ' ' + sql_alias
                agg_info.append(not is_agg and sql_alias or None)
            else:
                agg_info.append(not is_agg and expr or None)
                
        # we only need to group if there is at least one aggregate column and
        # at least one regular column before one of the aggregate columns:
        first_reg = len(agg_info)
        last_agg = -1
        for col, aggi in enumerate(agg_info):
            if aggi is not None:
                first_reg = min(col, first_reg)
            else:
                last_agg = max(col, last_agg)
        if last_agg > first_reg:
            group_by = [col for col in agg_info[0:last_agg] if col is not None]
            group_by = 'GROUP BY ' + ', '.join(group_by)
        else:
            group_by = None
        return select, group_by

    def order_clause_to_sql(self, order_clause, state):
        if order_clause is None:
            return None
        items = []
        for sort_item in order_clause.items:
            expr = self.expression_to_sql(sort_item.expression, state)
            direction = sort_item.direction.upper()
            items.append(expr + (direction.startswith('ASC') and '' or (' ' + direction)))
        return 'ORDER BY ' + ', '.join(items)
    
    def limit_clauses_to_sql(self, skip_clause, limit_clause, state):
        if skip_clause is None and limit_clause is None:
            return None
        state.disable_variables()
        limit = 'LIMIT'
        if limit_clause is not None:
            limit += ' ' + self.expression_to_sql(limit_clause.expression, state)
        else:
            limit += ' -1'
        if skip_clause is not None:
            limit += ' OFFSET ' + self.expression_to_sql(skip_clause.expression, state)
        state.enable_variables()
        return limit

    def get_top_level_match_clauses(self):
        """Return all strict and optional top-level match clauses of this query in order.
        Returns the (single) strict match clause first which is important for
        later optional joins to strict clause variables to work correctly.
        """
        return (self.match_clause, *self.optional_clauses)

    def get_all_match_clauses(self):
        """Return all strict, optional and other pattern-matching clauses of this query.
        """
        top_level_clauses = self.get_top_level_match_clauses()
        other_clauses = (c for c in self.query.get_all_match_clauses() if c not in top_level_clauses)
        return top_level_clauses + tuple(other_clauses)
    
    def init_match_clause(self, match_clause, state):
        """Initialize graph and table alias info for this 'match_clause'.
        """
        i = len(state.alias_map) + 1
        # we initialize this here for now; conceivably we could also invent
        # some per-clause syntax for it, for example, --match! and --opt!:
        match_clause.dont_optimize = self.dont_optimize
        for clause in match_clause.get_pattern_clauses():
            graph = self.get_pattern_clause_graph(clause)
            # create per-clause graph table alias for self-joins (keep the DB qualifier
            # if we have it to avoid name clashes but change the separator char):
            graph_alias = f'{self.store.get_qualified_table_name(graph, sep="_")}_c{i}'
            clause[0]._graph_alias = graph_alias
            state.register_table_alias(graph, graph_alias)
            i += 1
                
    def init_match_clauses(self, state):
        """Initialize graph and table alias info for all match and pattern clauses.
        """
        for match_clause in self.get_all_match_clauses():
            self.init_match_clause(match_clause, state)

    def get_match_clause_graphs(self, match_clause):
        """Return the set of graph table names with aliases referenced by this 'match_clause'.
        """
        # IMPORTANT: we cannot currently cache this and need to recompute the list at every call
        # so we'll pick up virtual graphs once they've been registered by 'pattern_clause_to_sql()':
        graphs = set()
        graphs_list = []
        for clause in match_clause.get_pattern_clauses():
            graph_table = self.get_pattern_clause_graph(clause)
            graph_alias = self.get_pattern_clause_graph_alias(clause)
            graph = (graph_table, graph_alias)
            if graph not in graphs:
                graphs.add(graph)
                graphs_list.append(graph)
        # extra logic so we preserve the original graph order in the standard case
        # to not upset the optimization of any existing queries in the wild:
        return graphs_list if match_clause.dont_optimize else graphs

    def get_all_match_clause_graphs(self):
        """Return the set of graph table names with aliases referenced by this query.
        """
        # IMPORTANT: do not cache this - see above:
        graphs = set()
        for match_clause in self.get_all_match_clauses():
            graphs.update(self.get_match_clause_graphs(match_clause))
        return graphs

    def graph_names_to_sql_join(self, graphs, dont_optimize=False, append=False):
        """Translate a list of (graph, alias) pairs into an SQL table list with aliases.
        Choose the appropriate INNER or CROSS join operator based on 'dont_optimize'
        (note that this is an SQLite-specific idiom to disable the query optimizer).
        If 'append', append to an existing join starting with the respective join operator.
        """
        if not dont_optimize:
            # preserve the original graph order in the standard case to not
            # upset the optimization of any existing queries in the wild:
            graphs = sorted(listify(graphs))
        appendop = (dont_optimize  and 'CROSS JOIN ' or 'INNER JOIN ') if append else ''
        joinop = (dont_optimize  and ' CROSS JOIN ' or ', ')
        return appendop + joinop.join([g + ' AS ' + a for g, a in graphs])

    def match_clause_to_sql(self, match_clause, state):
        """Translate a strict or optional 'match_clause' into a set of source tables,
        joined tables, internal and external join and where conditions which can then
        be assembled into appropriate FROM/WHERE/INNER JOIN/LEFT JOIN and any necessary
        nested joins depending on the particular structure of 'match_clause'.  This is
        a bit wild and wooly and will likely need further refinement down the road.
        """
        state.set_match_clause(match_clause)
        clause_sources = list(self.get_match_clause_graphs(match_clause))
        if not match_clause.dont_optimize:
            # preserve the original graph order in the standard case to not
            # upset the optimization of any existing queries in the wild:
            clause_sources = sorted(clause_sources)
        primary_source = clause_sources[0]
        sources = clause_sources.copy()

        joined = set()
        internal_condition = []
        external_condition = []
        
        for (g1, c1), (g2, c2) in sorted(list(state.get_match_clause_joins(match_clause))):
            condition = '%s.%s = %s.%s' % (g1, sql_quote_ident(c1), g2, sql_quote_ident(c2))
            graph1 = (state.get_alias_table(g1), g1)
            graph2 = (state.get_alias_table(g2), g2)
            internal = graph1 in clause_sources and graph2 in clause_sources
            if graph1 != primary_source:
                if graph1 in clause_sources:
                    joined.add(graph1)
                graph1 in sources and sources.remove(graph1)
            if graph2 != primary_source:
                if graph2 in clause_sources:
                    joined.add(graph2)
                graph2 in sources and sources.remove(graph2)
            if internal:
                internal_condition.append(condition)
            else:
                external_condition.append(condition)

        for (g, c), val in sorted(list(state.get_match_clause_restrictions(match_clause))):
            internal_condition.append('%s.%s = %s' % (g, sql_quote_ident(c), val))

        where = self.where_clause_to_sql(match_clause.get_where_clause(), state)
        if where:
            internal_condition.append(where)
        internal_condition = '\n   AND '.join(internal_condition)
        external_condition = '\n   AND '.join(external_condition)

        if match_clause.dont_optimize:
            # order joined tables in the order they appear in clause_sources:
            joined = [(graph, clause_sources.index(graph)) for graph in joined]
            joined.sort(key=lambda x: x[1])
            joined = [x[0] for x in joined]

        state.set_match_clause(None)
        return sources, joined, internal_condition, external_condition

    def with_clause_to_sql(self, with_clause, state):
        """Translate a 'WITH ... WHERE ...' clause which currently is primarily a vehicle to
        communicate a global WHERE clause that applies across all match clauses, so for now
        we only support 'WITH * ...'.  But we do want to generalize this at some point, since
        it gives us a way to chain queries and condition on aggregates, for example.  Once we
        do that, this needs to be generalized to take the translated query it wraps as an arg.
        """
        if with_clause is None:
            return ""
        select = self.return_clause_to_sql_selection(with_clause, state)
        if select != ('*', None):
            raise KGTKException("unsupported WITH clause, only 'WITH * ...' is currently supported")
        where = self.where_clause_to_sql(with_clause.where, state)
        return where
    
    def translate_to_sql_iter(self):
        """Translate this query into an equivalent SQL expression.
        Return the SQL as part of the accumulated final translation state.
        """
        state = TranslationState(self)

        # process strict and optional match clauses in order which is important to get
        # the proper clause variable registration order; that way optional clauses that
        # reference variables from earlier optional or strict clauses will join correctly:
        self.init_match_clauses(state)
        for match_clause in self.get_top_level_match_clauses():
            state.set_match_clause(match_clause)
            # translate clause top-level info such as variables and restrictions:
            for clause in match_clause.get_pattern_clauses():
                graph_alias = self.get_pattern_clause_graph_alias(clause)
                self.pattern_clause_to_sql(clause, graph_alias, state)
            
            # translate properties:
            for clause in match_clause.get_pattern_clauses():
                graph_alias = self.get_pattern_clause_graph_alias(clause)
                self.pattern_clause_props_to_sql(clause, graph_alias, state)
            state.set_match_clause(None)

        # assemble SQL query:
        query = io.StringIO()
        
        select, group_by = self.return_clause_to_sql_selection(self.return_clause, state)
        query.write('SELECT %s' % select)

        # start with the mandatory strict match clause:
        sources, joined, int_condition, ext_condition = self.match_clause_to_sql(self.match_clause, state)
        aux_tables = list(state.get_match_clause_aux_tables(self.match_clause))
        if len(sources) > 1 and not self.force:
            raise KGTKException('match clause generates a cross-product which can be very expensive, use --force to override')
        assert not ext_condition, 'INTERNAL ERROR: unexpected match clause'

        where = []
        query.write(f'\nFROM {self.graph_names_to_sql_join(sources + aux_tables)}')
        if joined:
                query.write(f'\n{self.graph_names_to_sql_join(joined, dont_optimize=self.match_clause.dont_optimize, append=True)}')
        if int_condition:
            if joined:
                query.write('\nON %s' % int_condition)
            else:
                # we need to defer WHERE in case there are left joins:
                where.append(int_condition)

        # now add any left joins from optional match clauses:
        for opt_clause in self.optional_clauses:
            sources, joined, int_condition, ext_condition = self.match_clause_to_sql(opt_clause, state)
            aux_tables = list(state.get_match_clause_aux_tables(opt_clause))
            if len(sources) > 1 and not self.force:
                raise KGTKException('optional clause generates a cross-product which can be very expensive, use --force to override')
            nested = len(joined) > 0
            query.write(f'\nLEFT JOIN {"(" if nested else ""}{self.graph_names_to_sql_join(sources + aux_tables)}')
            if nested:
                query.write(f'\n    {self.graph_names_to_sql_join(joined, dont_optimize=opt_clause.dont_optimize, append=True)}')
                query.write('\n    ON %s)' % int_condition.replace('\n', '\n    '))
                query.write(f'\nON {ext_condition}')
            else:
                query.write('\nON %s' % '\n   AND '.join(listify(ext_condition) + listify(int_condition)))

        # process any 'WITH * WHERE ...' clause to add to the global WHERE condition if necessary:
        with_where = self.with_clause_to_sql(self.with_clause, state)
        with_where and where.append(with_where)
        
        # finally add WHERE clause from strict match and/or WITH clause in case there were any:
        where and query.write('\nWHERE %s' % ('\n   AND '.join(where)))

        # add various other clauses:
        group_by and query.write('\n' + group_by)
        order = self.order_clause_to_sql(self.order_clause, state)
        order and query.write('\n' + order)
        limit = self.limit_clauses_to_sql(self.skip_clause, self.limit_clause, state)
        limit and query.write('\n' + limit)
        query = query.getvalue().replace(' TRUE\nAND', '')
        query, parameters = state.replace_literal_parameters(query)

        # logging:
        rule = '-' * 45
        self.log(1, 'SQL Translation:\n%s\n  %s\n  PARAS: %s\n%s'
                 % (rule, query.replace('\n', '\n     '), parameters, rule))

        state.set_sql(query)
        state.set_parameters(parameters)
        
        # implement this as a generator, so we can retranslate from scratch if necessary:
        yield state

    def translate_to_sql(self):
        """Translate this query into an equivalent SQL expression.
        Return the SQL as part of the accumulated final translation state.
        This is the top-level controller that handles possible retranslation
        restarts in case the query was rewritten or augmented somewhere.
        """
        while True:
            self.translation_iter = self.translate_to_sql_iter()
            try:
                for state in self.translation_iter:
                    return state
            except GeneratorExit as e:
                if e.args == ('_retranslate',):
                    #print('retranslating...')
                    continue
                else:
                    raise e

    def retranslate(self):
        """Abort the current translation to the top level and restart from scratch.
        This is needed by certain translation specialists that need to
        rewrite or augment the initial query.
        """
        self.reset()
        raise GeneratorExit('_retranslate')

    
    def compute_auto_indexes(self, state):
        """Compute column indexes that are likely needed to run this query efficiently.
        This is just an estimate based on columns involved in joins and restrictions.
        """
        indexes = set()
        for match_clause in self.get_all_match_clauses():
            joins = state.get_match_clause_joins(match_clause)
            restrictions = state.get_match_clause_restrictions(match_clause)
            if len(joins) > 0:
                for (g1, c1), (g2, c2) in joins:
                    g1 = state.get_alias_table(g1)
                    g2 = state.get_alias_table(g2)
                    # do not create any indexes on virtual tables:
                    if state.lookup_vtable(g1) is None:
                        indexes.add((g1, c1))
                    if state.lookup_vtable(g2) is None:
                        indexes.add((g2, c2))
            if len(restrictions) > 0:
                # even if we have joins, we might need additional indexes on restricted columns:
                for (g, c), val in restrictions:
                    g = state.get_alias_table(g)
                    # do not create any indexes on virtual tables:
                    if state.lookup_vtable(g) is None:
                        indexes.add((g, c))
        return indexes

    def get_explicit_graph_index_specs(self):
        """Collect all explicit per-input index specs and return them
        as an ordered dict of {<graph>: [index-spec+ ...] ...} items.
        """
        explicit_index_specs = odict()
        for file in self.files:
            index_specs = self.get_input_option(file, 'index_specs')
            if index_specs is not None:
                graph = self.store.get_file_graph(file)
                explicit_index_specs[graph] = index_specs
        return explicit_index_specs

    def get_default_graph_index_specs(self):
        """Collect all default index specs and return them as an ordered dict of
        {<graph>: [index-spec+ ...] ...} items for all query graphs that do not
        have any explicit index spec specified for them.
        """
        explicit_index_specs = self.get_explicit_graph_index_specs()
        default_index_specs = odict()
        for graph, alias in self.get_all_match_clause_graphs():
            if graph not in explicit_index_specs:
                default_index_specs[graph] = listify(self.index_mode)
        return default_index_specs

    def ensure_indexes(self, graphs, index_specs, state, explain=False):
        """Ensure that for each graph in 'graphs' all indexes according to 'index_specs' are available.
        'state' is the final translation state of the query.
        """
        graphs = listify(graphs)
        for index_spec in listify(index_specs):
            index_spec = ispec.get_normalized_index_mode(index_spec)
            if isinstance(index_spec, list):
                for spec in index_spec:
                    for graph in graphs:
                        self.store.ensure_graph_index(graph, ispec.TableIndex(graph, spec), explain=explain)
                    
            elif index_spec == ispec.INDEX_MODE_AUTO:
                # build indexes as suggested by query joins and restrictions (restricted to 'graphs'):
                for graph, column in self.compute_auto_indexes(state):
                    if graph in graphs:
                        # for now unconditionally restrict to core columns:
                        if column in self.get_edge_columns(graph):
                            #unique = column == self.get_id_column(graph)
                            # for now don't enforce uniqueness on edge IDs to support noisy data:
                            unique = False
                            self.store.ensure_graph_index_for_columns(graph, column, unique=unique, explain=explain)
                            
            elif index_spec == ispec.INDEX_MODE_EXPERT:
                # build indexes as suggested by the database (restricted to 'graphs'):
                for name, graph, columns in self.store.suggest_indexes(state.get_sql()):
                    if graph in graphs:
                        # only consider first column, multi-column indexes can be specified manually:
                        column = columns[0]
                        #unique = column == self.get_id_column(graph)
                        # for now don't enforce uniqueness on edge IDs to support noisy data:
                        unique = False
                        self.store.ensure_graph_index_for_columns(graph, column, unique=unique, explain=explain)

            elif index_spec == ispec.INDEX_MODE_NONE:
                pass

            elif index_spec == ispec.INDEX_MODE_CLEAR:
                for graph in graphs:
                    self.store.drop_graph_indexes(graph)

            elif index_spec == ispec.INDEX_MODE_CLEAR_TEXT:
                for graph in graphs:
                    self.store.drop_graph_indexes(graph, index_type=ispec.TextIndex)
            
            elif index_spec in (ispec.INDEX_MODE_AUTO_TEXT):
                print(f'WARN: {index_spec} not yet implemented')

    def ensure_relevant_indexes(self, state, explain=False):
        """Ensure that relevant indexes for this query are available on the database.
        First creates any indexes explicitly specified on individual inputs.  Then, for any
        graphs referenced in the query that do not have an explicit index specification, create
        indexes based on the default index_mode strategy.  The default for that is 'auto' which
        will use 'compute_auto_indexes' to decide what should be indexed.  'state' is assumed
        to be the final translation state of the query.  If 'explain' is True, do not actually
        build any indexes, only show commands that would be executed.
        """
        # NOTES
        # - what we want is the minimal number of indexes that allow this query to run efficiently,
        #   since index creation itself is expensive in time and disk space
        # - however, to do this right we need some approximate analysis of the query, e.g., for a join
        #   we'll generally only need an index on one of the involved columns, however, knowing for
        #   which one requires knowledge of table size, statistics and other selectivity of the query
        # - skewed distribution of fanout in columns complicates this further, since an average
        #   fanout might be very different from maximum fanouts (e.g., for wikidata node2)
        # - large fanouts might force us to use two-column indexes such as 'label/node2' and 'label/node1'
        # - to handle this better, we will exploit the SQLite expert command to create (variants) of
        #   the indexes it suggests, since that often wants multi-column indexes which are expensive
        # - we also need some manual control as well to force certain indexing patterns
        # - we only index core columns for now, but we might have use cases where that is too restrictive
        # TO DO: parse all index specs before we perform any actions to detect errors eagerly
        for graph, index_specs in self.get_explicit_graph_index_specs().items():
            self.ensure_indexes(graph, index_specs, state, explain=explain)
        for graph, index_specs in self.get_default_graph_index_specs().items():
            self.ensure_indexes(graph, index_specs, state, explain=explain)

        
    def execute(self):
        state = self.translate_to_sql()
        self.ensure_relevant_indexes(state)
        result = self.store.execute(state.get_sql(), state.get_parameters())
        self.result_header = [self.unalias_column_name(c[0]) for c in result.description]
        result = self.wrap_multi_edge_result(result)
        return result

    def wrap_multi_edge_result(self, result):
        """If we need to return multi-edges, wrap 'result' with the appropriate
        iterator magic that first flattens and then regroups appropriately.
        This also adjust the header column list as needed and filters out rows
        that contain empty values if the query had optional clauses.
        For single-edge queries, return the 'result' iterator unmodified.
        """
        if self.multi_edge and self.multi_edge > 1:
            ncols = len(self.result_header)
            if ncols % self.multi_edge != 0:
                raise KGTKException(f'illegal multi-edge value: {ncols} result columns' +
                                    f' cannot be evenly split into {self.multi_edge} separate rows')
            ncols = ncols // self.multi_edge
            self.result_header = self.result_header[:ncols]
            flatres = itertools.chain.from_iterable(result)
            result = zip(*([flatres] * ncols))
            if len(self.optional_clauses) > 0:
                # if we have optionals, filter out tuples that contain empty (aka null) values -
                # relies on all values being strings and that we can't distinguish null from empty
                # (this is similar to SPARQL CONSTRUCT where triples are not created for patterns
                # that involve an unbound/null variable):
                result = filter(all, result)
        return result

    def explain(self, mode='plan'):
        state = self.translate_to_sql()
        self.ensure_relevant_indexes(state, explain=True)
        result = self.store.explain(state.get_sql(), parameters=state.get_parameters(), mode=mode)
        return result


class TranslationState(object):
    """Accumulates and manages various state information during translation.
    """

    def __init__(self, query):
        self.query = query
        self.literal_map = {}         # maps Kypher literals onto parameter placeholders
        self.variable_map = {}        # maps Kypher variables onto representative (graph, col) SQL columns
        self.alias_map = {}           # maps tables to their aliases and vice versa
        self.vtable_map = {}          # maps referenced virtual table names to their SqlFunction object
        self.match_clause = None      # match clause we are currently processing
        self.match_clause_info = {}   # maps match clauses onto joins, restrictions, etc. encountered
        self.sql = None               # final SQL translation of 'query'
        self.parameters = None        # final parameter values for translated query
        self.subquery_stack = []      # stack to manage info local to subqueries

    def get_literal_map(self):
        return self.literal_map

    def get_variable_map(self):
        return self.variable_map

    def disable_variables(self):
        """Disable any variable processing (e.g., for contexts where they are illegal).
        """
        self._saved_variable_map = self.variable_map
        self.variable_map = None

    def enable_variables(self):
        """Enable variable processing again.
        """
        self.variable_map = self._saved_variable_map

    def lookup_variable(self, variable, error=True):
        """Lookup 'variable' in the current variable map.  Raise an error if variables
        are currently disabled or if 'variable' is undefined (unless 'error' is False).
        """
        if self.variable_map is None:
            if error:
                # for cases where external variables are not allowed (e.g. LIMIT):
                raise KGTKException('Illegal context for variable: %s' % variable)
            else:
                return None
        sql_vars = self.variable_map.get(variable)
        if sql_vars is None and error:
            raise KGTKException('Undefined variable: %s' % variable)
        return sql_vars

    def register_table_alias(self, table, alias):
        """Record 'alias' as an alias for 'table'.  Raise an error if the alias
        if already used as a table name or as an alias for a different table.
        """
        current = self.alias_map.get(alias)
        if current is None:
            self.alias_map[alias] = table
            self.alias_map.setdefault(table, []).append(alias)
        elif isinstance(current, list):
            raise KGTKException(f'Alias {alias} already used as table name')
        elif current != table:
            raise KGTKException(f'Alias {alias} already in use for {current}')

    def get_alias_table(self, alias, error=True):
        """Return the table for which 'alias' has been registered as an alias.
        If 'alias' is not a registered table alias, raise an error if 'error' is True.
        """
        table = self.alias_map.get(alias)
        if table is None and error:
            raise KGTKException(f'Alias {alias} is not defined')
        return table

    def get_table_aliases(self, table, create_prefix=None):
        """Get the currently defined aliases for 'table'.  If none are defined
        and 'create_prefix' is provided, create a new alias based on that.
        Otherwise, raise an error.
        """
        aliases = self.alias_map.get(table)
        if aliases is not None:
            return aliases
        elif create_prefix is not None:
            for i in range(1, 1000000):
                alias = f'{create_prefix}_{i}'
                if self.alias_map.get(alias) is None:
                    self.register_table_alias(table, alias)
                    return self.alias_map[table]
            raise KGTKException('Internal error: alias map exhausted')
        else:
            raise KGTKException(f'No aliases defined for {table}')

    def get_vtable_map(self):
        return self.vtable_map

    def register_vtable(self, vtable_name, sql_func):
        """Register that the virtual table 'vtable_name' has been referenced and
        is implemented by SqlFunction 'sql_func'.
        """
        self.vtable_map[vtable_name] = sql_func

    def lookup_vtable(self, vtable_name):
        """Lookup the SqlFunction implementing the virtual table 'vtable_name'.
        Return None if 'vtable_name' is not a registered virtual table.
        """
        return self.vtable_map.get(vtable_name)
    
    def get_match_clause(self):
        """Return the current match clause."""
        return self.match_clause

    def set_match_clause(self, clause):
        """Set the current match clause to 'clause'"""
        self.match_clause = clause

    def get_match_clause_joins(self, clause=None):
        """Returns all joins encounterd in this match 'clause' which maps equivalent
        SQL column pairs (avoiding dupes and redundant flips).  'clause' defaults to
        the current match clause.
        """
        clause = clause or self.match_clause
        info = self.match_clause_info.setdefault(clause, {})
        joins = info.setdefault('joins', set())
        return joins

    def add_match_clause_join(self, var1, var2, clause=None):
        """Add a join between 'var1' and 'var2' to 'clause's joins.
        'clause' defaults to the current match clause.
        """
        self.get_match_clause_joins(clause=clause).add((var1, var2))

    def get_match_clause_restrictions(self, clause=None):
        """Return all restrictions encountered in this match 'clause' which maps
        (graph, col) SQL columns onto literal restrictions.  'clause' defaults to
        the current match clause.
        """
        clause = clause or self.match_clause
        info = self.match_clause_info.setdefault(clause, {})
        restrictions = info.setdefault('restrictions', set())
        return restrictions

    def add_match_clause_restriction(self, sqlvar, expression, clause=None):
        """Add a restriction of 'sqlvar' to 'expression' to 'clause's restrictions.
        'clause' defaults to the current match clause.
        """
        self.get_match_clause_restrictions(clause=clause).add((sqlvar, expression))

    def get_match_clause_aux_tables(self, clause=None):
        """Return all auxiliary source tables encountered in this match 'clause'.
        """
        clause = clause or self.match_clause
        info = self.match_clause_info.setdefault(clause, {})
        aux_tables = info.setdefault('aux_tables', set())
        return aux_tables

    def add_match_clause_aux_table(self, table, alias, clause=None):
        """Add auxiliary table 'table' with its 'alias' to 'clause's auxiliary tables.
        'clause' defaults to the current match clause.
        """
        self.get_match_clause_aux_tables(clause=clause).add((table, alias))

    def get_sql(self):
        return self.sql

    def set_sql(self, sql):
        self.sql = sql

    def get_parameters(self):
        return self.parameters

    def set_parameters(self, params):
        self.parameters = params

        
    def get_literal_parameter(self, literal):
        """Return a parameter placeholder such as '?12?' that will be mapped to 'literal'
        and will later be replaced with a query parameter at the appropriate position.
        """
        litmap = self.get_literal_map()
        if literal in litmap:
            return litmap[literal]
        else:
            placeholder = '???%d??' % len(litmap)
            litmap[literal] = placeholder
            return placeholder

    def replace_literal_parameters(self, raw_query):
        """Replace the named literal placeholders in 'raw_query' with positional
        parameters and build a list of actual parameters to substitute for them.
        """
        litmap = self.get_literal_map()
        query = io.StringIO()
        parameters = []
        # reverse 'litmap' to map placeholders onto literal values:
        litmap = {p: l for l, p in litmap.items()}
        for token in re.split(r'\?\?', raw_query):
            if token.startswith('?'):
                parameters.append(litmap['??' + token + '??'])
                token = '?'
            query.write(token)
        return query.getvalue(), parameters
                 
    def register_clause_variable(self, query_var, sql_var, nojoins=False):
        """Register a reference to the Kypher variable 'query_var' which corresponds to the
        SQL clause variable 'sql_var' represented as '(graph, column)' where 'graph' is a
        table alias for the relevant graph specific to the current clause.  If this is the
        first reference to 'query_var', simply add it to the variable map.  Otherwise, find the
        best existing reference to equiv-join it with and record the necessary join in 'joins'
        (unless 'nojoins' is True).
        """
        varmap = self.get_variable_map()
        sql_vars = varmap.get(query_var)
        if sql_vars is None:
            # we use a list here now to preserve the order which matters for optionals:
            varmap[query_var] = [sql_var]
        else:
            # POLICY: we either find the earliest equivalent variable from the same clause
            # (as in '(x)-[]->{x)'), or the earliest registered variable from a different
            # clause, which is what we need to handle cross-clause references from optionals
            # (assuming strict and optional match clauses are processed appropriately in order):
            # NOTE: further optimizations might be possible here, e.g., we might want to prefer
            # a self-join on the same column, since it might reduce the number of auto-indexes:
            this_graph, this_col = sql_var
            best_var = None
            for equiv_var in sql_vars:
                equiv_graph, equiv_col = equiv_var
                if best_var is None:
                    best_var = equiv_var
                elif this_graph == equiv_graph:
                    # we match on graph and clause, since clause is encoded in graph:
                    best_var = equiv_var
                    break
                else:
                    # keep current earliest 'best_var':
                    pass
            # not sure if they could ever be equal, but just in case:
            if sql_var != best_var:
                sql_var not in sql_vars and sql_vars.append(sql_var)
                # we never join an alias with anything:
                if this_graph != self.query.ALIAS_GRAPH:
                    equiv = [best_var, sql_var]
                    # normalize join order by order in 'sql_vars' so earlier vars come first:
                    equiv.sort(key=lambda v: sql_vars.index(v))
                    if not nojoins:
                        self.add_match_clause_join(equiv[0], equiv[1])

    def push_subquery(self):
        """Save the current state so it doesn't get polluted by subquery-local information.
        We only care about the current match clause and subquery-local variable mappings.
        """
        self.subquery_stack.append((self.match_clause, self.variable_map))
        self.variable_map = copy.deepcopy(self.variable_map)

    def pop_subquery(self):
        """Restore the current state to what it was before we entered a subquery.
        """
        self.match_clause, self.variable_map = self.subquery_stack.pop()


### Text match support

# This is a bit messy and idiosyncratic, so we are keeping it outside the regular translator.
# TO DO: see if we can refactor and package this better with the new SqlFunction API

TEXTMATCH_OPERATORS = {'TEXTMATCH': 'match', 'TEXTLIKE': 'like', 'TEXTGLOB': 'glob',
                       'MATCHSCORE': 'score', 'BM25': 'score'}

def is_text_match_operator(op):
    """Return True if 'op' is a special KGTK text search function.
    """
    return str(op).upper() in TEXTMATCH_OPERATORS

def normalize_text_match_operator(op):
    """Normalize the textmatch operator 'op' to a logical string name.
    """
    return TEXTMATCH_OPERATORS.get(str(op).upper())

def translate_text_match_op_to_sql(query, expr, state):
    """Translate a text match expression 'expr' into appropriate full-text index operations.
    """
    # Unnamed invocations require the referenced variable to uniquely select a graph
    # and associated text index; if there is ambiguity, an error will be raised:
    # (1) --match '...(x)-[]->(l)...' --where '...textmatch(l, "foo bar")...' --return '...bm25(l)...'
    #     column-based match on 'l' only, requires 'l' to be associated with a unique graph and
    #     the graph be associated with a unique text index that indexes the node2 column
    # (2) --match '...(x)-[r]->(l)...' --where '...textmatch(r, "foo bar")...' --return '...bm25(r)...'
    #     all-indexed-column-based match, requires 'r' to be associated with a unique graph and
    #     the graph to be associated with a unique text index, for the associated score function
    #     either r or l could be used as long as l is as discriminative as r
    # (3) --match '...(x)-[r]->(l)...' --where '...textmatch(r.node2, "foo bar")...' --return '...bm25(r.node2)...'
    #     column-based match on node2 only, requires 'r' to be associated with a unique graph and
    #     the graph be associated with a unique text index that indexes the node2 column; can be used
    #     in case the associated l variable does not uniquely specify a text index
    # (4) --match '...(x)-[r]->(l)...' --where '...textmatch(r.id, "foo bar")...' --return '...bm25(r.id)...'
    #     column-based match on id only, requires 'r' to be associated with a unique graph and
    #     the graph be associated with a unique text index that indexes the id column
    #
    # Named invocations specify the name of a specific index to use in addition to a graph variable.
    # This can be used for explicit disambiguation, for example, if a graph has multiple text indexes
    # associated with it.  In this case the named index needs to be usable for the specified variable.
    # Index names can be provided with a variable whose name should not match any match variables.
    # We can then use property syntax if we want to specify specific match variables.  In the examples
    # below we assume we have a text index named 'myidx2'.
    # (1) --match '...(x)-[]->(l)...' --where '...textmatch(myidx2.l, "foo bar")...' --return '...bm25(myidx2.l)...'
    #     column-based match on 'l' only, requires 'l' to be associated with the graph of myidx2
    #     and myidx2 to index the node2 column
    # (2) --match '...(x)-[r]->(l)...' --where '...textmatch(myidx2.r, "foo bar")...' --return '...bm25(myidx2.r)...'
    #     all-indexed-column-based match, requires 'r' to be associated with the graph of myidx2
    # (3) --match '...(x)-[r]->(l)...' --where '...textmatch(myidx2.r.node2, "foo bar")...' --return '...bm25(myidx2.r.node2)...'
    #     column-based match on node2 only, requires 'r' to be associated with the graph of myidx2
    #     and myidx2 to index the node2 column
    # (4) --match '...(x)-[r]->(l)...' --where '...textmatch(myidx2.r.id, "foo bar")...' --return '...bm25(myidx2.r.id)...'
    #     column-based match on id only, requires 'r' to be associated with the graph of myidx2
    #     and myidx2 to index the node2 column
    
    normfun = normalize_text_match_operator(expr.function)
    if not normfun:
        raise KGTKException(f"Unsupported text match function: {expr.function}")
    arguments = expr.args
    arity = len(arguments)
    if arity < 1:
        raise KGTKException(f"Missing arguments in {expr.function} expression")

    # handle first argument which can be a variable or property expression (possibly starting with an index name):
    # ('Variable', {'name': 'l'})
    # ('Expression2', {'arg1': ('Variable', {'name': 'r'}), 'arg2': [('PropertyLookup', {'property': 'node2'})]})
    # ('Expression2', {'arg1': ('Variable', {'name': 'myidx'}), 'arg2': [('PropertyLookup', {'property': 'r'})]})
    # ('Expression2', {'arg1': ('Variable', {'name': 'myidx'}), 'arg2': [('PropertyLookup', {'property': 'r'}), ('PropertyLookup', {'property': 'node2'})]})
    arg1 = arguments[0]
    index_name = None
    if isinstance(arg1, parser.Expression2) and isinstance(arg1.arg1, parser.Variable):
        # we have a property reference, check if base variable is an index name:
        sql_vars = state.lookup_variable(arg1.arg1.name, error=False)
        if sql_vars is None:
            index_name = arg1.arg1.name
            props = arg1.arg2
            arg1.arg1.name = props[0].property
            arg1.arg2 = props[1:]
            if len(props) == 1:
                arg1 = arg1.arg1

    # figure out the graph and column name:
    # TO DO: for now we ignore the possibility of graph or column-ambiguous variables
    #        and simply go with the SQL translation, but this needs to be generalized:
    if isinstance(arg1, parser.Variable):
        # key in on Variableness to figure out whether this might refer to whole index or just a column:
        graph_alias, column_name, sql = query.variable_to_sql(arg1, state)
    elif isinstance(arg1, parser.Expression2) and isinstance(arg1.arg1, parser.Variable):
        graph_alias, column_name, sql = query.property_to_sql(arg1, state)
    else:
        raise KGTKException(f"First argument to {expr.function} needs to be variable or property")

    # find applicable indexes:
    graph = state.get_alias_table(graph_alias)
    if column_name == query.get_id_column(graph) and isinstance(arg1, parser.Variable):
        # we have an all-indexed-columns match:
        column = None
    else:
        # we have a column-specific match:
        column = column_name
    indexes = find_matching_text_indexes(query, graph, index_name, column)
    if len(indexes) == 0:
        # for now, until we support mode:autotext:
        raise KGTKException(f"No usable text index found for {expr.function}")
    elif len(indexes) > 1:
        raise KGTKException(f"Multiple applicable text indexes found for {expr.function}")

    # generate the SQL translation:
    index = indexes[0]
    index_table = index.get_name()
    qualified_index_table = query.store.get_qualified_table_name(index_table, db=index.db)
    index_alias = state.get_table_aliases(qualified_index_table, create_prefix='txtidx')[0]
    index_column = index_table
    if not (column_name == query.get_id_column(graph) and isinstance(arg1, parser.Variable)):
        # we have a column-specific search:
        index_column = column_name
    index_column = sql_quote_ident(index_column)
    state.add_match_clause_aux_table(qualified_index_table, index_alias)

    if normfun in ('match', 'like', 'glob'):
        if arity != 2:
            raise KGTKException(f"Extraneous {expr.function} arguments")
        operator = normfun.upper()
        arg2 = query.expression_to_sql(arguments[1], state)
        return f'{index_alias}.{index_column} {operator} {arg2} and {index_alias}.rowid = {graph_alias}.rowid'
    elif normfun in ('score'):
        # scoring function always needs the special table column, even for column-based match:
        return f'BM25({index_alias}.{index_table})'

def get_implied_text_indexes(query, graph):
    """Return text indexes that will be available at query time implied by
    current indexes plus state changes and index creations from query options.
    Does not actually create any indexes or change associated info tables.
    """
    index_specs = query.get_explicit_graph_index_specs().get(graph)
    index_specs = query.get_default_graph_index_specs().get(graph) if index_specs is None else index_specs
    current_indexes = [idx for idx in query.store.get_graph_indexes(graph) if isinstance(idx, ispec.TextIndex)]
    explicit_indexes = []
    for index_spec in index_specs:
        index_spec = ispec.get_normalized_index_mode(index_spec)
        if isinstance(index_spec, list):
                for spec in index_spec:
                    index = ispec.TableIndex(graph, spec)
                    if isinstance(index, ispec.TextIndex):
                        explicit_indexes.append(index)
        elif index_spec in (ispec.INDEX_MODE_CLEAR, ispec.INDEX_MODE_CLEAR_TEXT):
            explicit_indexes = []
            current_indexes = []
    for expidx in explicit_indexes[:]:
        for curidx in current_indexes[:]:
            if expidx.redefines(curidx):
                current_indexes.remove(curidx)
            elif curidx.subsumes(expidx):
                explicit_indexes.remove(expidx)
    return explicit_indexes + current_indexes

def find_matching_text_indexes(query, graph, index_name, column):
    """Find text indexes that can be used to match againt 'graph', 'index_name' and 'column'.
    Both 'index_name' and 'column' may be None.  Considers any current indexes as well as
    state changes and index creations implied by 'query' index options, but does not actually
    create any indexes or change associated info tables.
    """
    indexes = []
    for idx in get_implied_text_indexes(query, graph):
        if ((index_name is None or idx.index.options.get('name') == index_name)
            and (column is None or column in idx.index.columns)):
            indexes.append(idx)
    return indexes


"""
>>> store = cq.SqliteStore('/tmp/graphstore.sqlite3.db', create=True)
>>> graph = '/home/hans/Documents/kgtk/code/kgtk/kgtk/kypher/.work/data/graph.tsv'

>>> query = cq.KgtkQuery(graph, store, match='(a)-[:loves]->(b)')
>>> list(query.execute())
[('Hans', 'loves', 'Molly', 'e11'), ('Otto', 'loves', 'Susi', 'e12'), ('Joe', 'loves', 'Joe', 'e14')]

>>> query = cq.KgtkQuery(graph, store, match='(a)-[:loves]->(b)-[:loves]->(a)')
>>> list(query.execute())
[('Joe', 'loves', 'Joe', 'e14', 'Joe', 'loves', 'Joe', 'e14')]

>>> query = cq.KgtkQuery(graph, store, match='(a)-[:loves]->(a)-[:loves]->(a)')
>>> list(query.execute())
[('Joe', 'loves', 'Joe', 'e14', 'Joe', 'loves', 'Joe', 'e14')]

>>> query = cq.KgtkQuery(graph, store, loglevel=1,
                         match='g: (a)-[:loves]->(a), (a)-[r2:name]->(n)')
>>> list(query.execute())
SQL: SELECT *
     FROM graph_1 graph_1_c1, graph_1 graph_1_c2
     WHERE graph_1_c1."label"=?
     AND graph_1_c2."label"=?
     AND graph_1_c1."node1"=graph_1_c1."node2"
     AND graph_1_c1."node1"=graph_1_c2."node1"
PARAS: ['loves', 'name']
[('Joe', 'loves', 'Joe', 'e14', 'Joe', 'name', '"Joe"', 'e23')]
>>> 

# return clause translation:

>>> query = cq.KgtkQuery(graph, store, loglevel=1,
                         match='g: (a)-[:loves]->(a), (a)-[r2:name]->(n)', 
                         ret="distinct a as node1, 'loves' as label, n as node2, r2 as id")

>>> cp.pp.pprint(query.return_clause.to_tree())
(   'Return',
    {   'distinct': False,
        'items': [   (   'ReturnItem',
                         {   'expression': ('Variable', {'name': 'a'}),
                             'name': 'node1'}),
                     (   'ReturnItem',
                         {   'expression': (   'Expression2',
                                               {   'arg1': (   'Variable',
                                                               {'name': 'r2'}),
                                                   'arg2': [   (   'PropertyLookup',
                                                                   {   'property': 'label'})]}),
                             'name': 'label'}),
                     (   'ReturnItem',
                         {   'expression': ('Variable', {'name': 'n'}),
                             'name': 'node2'}),
                     (   'ReturnItem',
                         {   'expression': ('Variable', {'name': 'r2'}),
                             'name': 'id'})]})

>>> list(query.execute())
SQL: SELECT DISTINCT graph_1_c2."node1" "node1", ? "label", graph_1_c2."node2" "node2", graph_1_c2."id" "id"
     FROM graph_1 graph_1_c1, graph_1 graph_1_c2
     WHERE graph_1_c1."label"=?
     AND graph_1_c2."label"=?
     AND graph_1_c1."node1"=graph_1_c1."node2"
     AND graph_1_c1."node1"=graph_1_c2."node1"
PARAS: ['loves', 'loves', 'name']
[('Joe', 'loves', '"Joe"', 'e23')]
>>> query.result_header
['node1', 'label', 'node2', 'id']
"""
