import shutil
import unittest
import tempfile
import shlex
from   io import StringIO
import pandas as pd
from kgtk_wukunhuan.cli_entry import cli_entry


# TO DO:
# - file aliasing via --as, realiasing
# - files not required to exist after initial import
# - queries from stdin (query pipes not yet supported)
# - NULL value tests and conversion functions

class TestKGTKQuery(unittest.TestCase):
    def setUp(self) -> None:
        self.file_path = 'data/kypher/graph.tsv'
        self.file_path_gz = 'data/kypher/graph.tsv.gz'
        self.file_path_bz2 = 'data/kypher/graph.tsv.bz2'
        self.quals_path = 'data/kypher/quals.tsv'
        self.works_path = 'data/kypher/works.tsv'
        self.props_path = 'data/kypher/props.tsv'
        self.literals_path = 'data/kypher/literals.tsv'
        self.embed_path = 'data/kypher/embed.tsv.gz'
        self.embed_labels_path = 'data/kypher/embed-labels.tsv.gz'
        self.embed_claims_path = 'data/kypher/embed-claims.tsv.gz'
        self.temp_dir = tempfile.mkdtemp()
        self.sqldb = f'{self.temp_dir}/test.sqlite3.db'
        self.df = pd.read_csv(self.file_path, sep='\t')

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)

    def test_kgtk_query_default(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 9)

    def test_kgtk_query_default_gzip(self):
        cli_entry("kgtk", "query", "-i", self.file_path_gz, "-o", f'{self.temp_dir}/out.tsv.gz', '--graph-cache',
                  self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv.gz', sep='\t')
        self.assertTrue(len(df) == 9)

    def test_kgtk_query_default_bz2(self):
        cli_entry("kgtk", "query", "-i", self.file_path_bz2, "-o", f'{self.temp_dir}/out.tsv.bz2', '--graph-cache',
                  self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv.bz2', sep='\t')
        self.assertTrue(len(df) == 9)

    def test_kgtk_query_match(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "(i)-[:loves]->(c)", '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 3)
        ids = list(df['id'].unique())
        self.assertTrue('e11' in ids)
        self.assertTrue('e12' in ids)
        self.assertTrue('e14' in ids)

    def test_kgtk_query_limit(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--limit",
                  "3", '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 3)
        ids = list(df['id'].unique())
        self.assertTrue('e11' in ids)
        self.assertTrue('e12' in ids)
        self.assertTrue('e13' in ids)

    def test_kgtk_query_limit_skip(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--limit",
                  "3", "--skip", "2", '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 3)
        ids = list(df['id'].unique())
        self.assertTrue('e13' in ids)
        self.assertTrue('e14' in ids)
        self.assertTrue('e21' in ids)

    def test_kgtk_query_hans_filter(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "(:Hans)-[]->()", '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 2)
        ids = list(df['id'].unique())
        self.assertTrue('e11' in ids)
        self.assertTrue('e21' in ids)

    def test_kgtk_query_otto_name_filter(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "(:Otto)-[:name]->()", '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 1)
        ids = list(df['id'].unique())
        self.assertTrue('e22' in ids)

    def test_kgtk_query_where_double_letter(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "(p)-[:name]->(n)", "--where", 'n =~".*(.)\\\\1.*"', '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 2)
        ids = list(df['id'].unique())
        self.assertTrue('e22' in ids)
        self.assertTrue('e24' in ids)

    def test_kgtk_query_where_IN(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "(p)-[:name]->(n)", "--where", 'p IN ["Hans", "Susi"]', '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 2)
        ids = list(df['id'].unique())
        self.assertTrue('e21' in ids)
        self.assertTrue('e25' in ids)

    def test_kgtk_query_where_upper_substring(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "(p)-[:name]->(n)", "--where", "upper(substr(n,2,1)) >= 'J'", '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 4)
        ids = list(df['id'].unique())
        self.assertTrue('e22' in ids)
        self.assertTrue('e23' in ids)
        self.assertTrue('e24' in ids)
        self.assertTrue('e25' in ids)

    def test_kgtk_query_where_upper_substring_sorted(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "(p)-[:name]->(n)", "--where", "upper(substr(n,2,1)) >= 'J'", "--order-by", "substr(n,2,1)",
                  '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 4)
        ids = list(df['id'].unique())
        self.assertTrue('e23' == ids[0])
        self.assertTrue('e24' == ids[1])
        self.assertTrue('e22' == ids[2])
        self.assertTrue('e25' == ids[3])

    def test_kgtk_query_where_upper_substring_sorted_desc(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "(p)-[:name]->(n)", "--where", "upper(substr(n,2,1)) >= 'J'", "--order-by", "substr(n,2,1) desc",
                  '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 4)
        ids = list(df['id'].unique())
        self.assertTrue('e25' == ids[0])
        self.assertTrue('e22' == ids[1])
        self.assertTrue('e24' == ids[2])
        self.assertTrue('e23' == ids[3])

    def test_kgtk_query_select_columns(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "(p)-[:name]->(n)", "--where", "upper(substr(n,2,1)) >= 'J'", "--return", "p,n", '--graph-cache',
                  self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 4)
        columns = list(df.columns)
        self.assertTrue('node1' in columns)
        self.assertTrue('node2' in columns)
        node1s = list(df['node1'].unique())
        self.assertTrue('Otto' in node1s)
        self.assertTrue('Joe' in node1s)
        self.assertTrue('Molly' in node1s)
        self.assertTrue('Susi' in node1s)

    def test_kgtk_query_switch_columns(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "(p)-[r:name]->(n)", "--where", "upper(substr(n,2,1)) >= 'J'", "--return", "p,n, r, r.label",
                  '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 4)
        columns = list(df.columns)
        self.assertTrue('node1' in columns)
        self.assertTrue('node2' in columns)
        self.assertTrue('id' in columns)
        self.assertTrue('label' in columns)
        node1s = list(df['node1'].unique())
        self.assertTrue('Otto' in node1s)
        self.assertTrue('Joe' in node1s)
        self.assertTrue('Molly' in node1s)
        self.assertTrue('Susi' in node1s)

    def test_kgtk_query_return_columns_modify_functions(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "(p)-[r:name]->(n)", "--where", "upper(substr(n,2,1)) >= 'J'",
                  "--return", "lower(p) as node1, r.label, n, r",
                  '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 4)
        columns = list(df.columns)
        self.assertTrue('node1' in columns)
        self.assertTrue('node2' in columns)
        self.assertTrue('id' in columns)
        self.assertTrue('label' in columns)
        node1s = list(df['node1'].unique())
        self.assertTrue('otto' in node1s)
        self.assertTrue('joe' in node1s)
        self.assertTrue('molly' in node1s)
        self.assertTrue('susi' in node1s)

    def test_kgtk_query_kgtk_unstringify(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "(p)-[r:name]->(n)", "--where", "upper(substr(n,2,1)) >= 'J'",
                  "--return", "p, r.label, kgtk_unstringify(n) as node2, r",
                  '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 4)
        columns = list(df.columns)
        self.assertTrue('node2' in columns)
        self.assertTrue('node1' in columns)
        self.assertTrue('id' in columns)
        self.assertTrue('label' in columns)
        vals = list(df['node2'].unique())
        self.assertTrue('Molly' in vals)

    def test_kgtk_query_para(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "(p)-[r:name]->(n)", "--where", " n = $name OR n = $name2 OR n = $name3 ",
                  "--para", "name=\"'Hans'@de\"", "--spara", "name2=Susi", "--lqpara", "name3=Otto@de", '--graph-cache',
                  self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 2)
        columns = list(df.columns)
        self.assertTrue('node2' in columns)
        self.assertTrue('node1' in columns)
        self.assertTrue('id' in columns)
        self.assertTrue('label' in columns)
        ids = list(df['id'].unique())
        self.assertTrue('e25' in ids)
        self.assertTrue('e22' in ids)

    def test_kgtk_query_lgstring_land(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "(p)-[r:name]->(n)", "--where", 'n.kgtk_lqstring_lang = "de"', '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 2)
        ids = list(df['id'].unique())
        self.assertTrue('e21' in ids)
        self.assertTrue('e22' in ids)

    def test_kgtk_query_reflexive_edges(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "(a)-[]->(a)", '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 1)
        ids = list(df['id'].unique())
        self.assertTrue('e14' in ids)

    def test_kgtk_query_multi_step_path(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "(na)<-[:name]-(a)-[r:loves]->(b)-[:name]->(nb)", "--return", "r, na, r.label, nb", '--graph-cache',
                  self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 3)
        ids = list(df['id'].unique())
        node2s = list(df['node2'].unique())
        node2_1s = list(df['node2.1'].unique())
        self.assertTrue('e14' in ids)
        self.assertTrue('e11' in ids)
        self.assertTrue('e12' in ids)
        self.assertTrue('Joe' in node2s)
        self.assertTrue("'Hans'@de" in node2s)
        self.assertTrue("'Otto'@de" in node2s)
        self.assertTrue('Joe' in node2_1s)
        self.assertTrue('Molly' in node2_1s)
        self.assertTrue('Susi' in node2_1s)

    def test_kgtk_query_multi_step_path_german_lovers(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "(na)<-[:name]-(a)-[r:loves]->(b)-[:name]->(nb)",
                  "--where", 'na.kgtk_lqstring_lang = "de" OR nb.kgtk_lqstring_lang = "de"',
                  "--return", "r, na, r.label, nb", '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 2)
        ids = list(df['id'].unique())
        node2s = list(df['node2'].unique())
        node2_1s = list(df['node2.1'].unique())
        self.assertTrue('e11' in ids)
        self.assertTrue('e12' in ids)
        self.assertTrue("'Hans'@de" in node2s)
        self.assertTrue("'Otto'@de" in node2s)
        self.assertTrue('Molly' in node2_1s)
        self.assertTrue('Susi' in node2_1s)

    def test_kgtk_query_multi_step_path_german_lovers_anonymous(self):
        cli_entry("kgtk", "query", "-i", self.file_path, "-o", f'{self.temp_dir}/out.tsv', "--match",
                  # test connection through anonymous node variables instead of a and b:
                  "(na)<-[:name]-()-[r:loves]->()-[:name]->(nb)",
                  "--where", 'na.kgtk_lqstring_lang = "de" OR nb.kgtk_lqstring_lang = "de"',
                  "--return", "r, na, r.label, nb", '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 2)
        ids = list(df['id'].unique())
        node2s = list(df['node2'].unique())
        node2_1s = list(df['node2.1'].unique())
        self.assertTrue('e11' in ids)
        self.assertTrue('e12' in ids)
        self.assertTrue("'Hans'@de" in node2s)
        self.assertTrue("'Otto'@de" in node2s)
        self.assertTrue('Molly' in node2_1s)
        self.assertTrue('Susi' in node2_1s)

    def test_kgtk_query_named_multi_graph_join(self):
        cli_entry("kgtk", "query", "-i", self.file_path,
                  "-i", self.works_path,
                  "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "g: (x)-[:loves]->(y), w: (y)-[:works]->(c)", '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 3)
        for i, row in df.iterrows():
            if row['id'] == 'e14':
                self.assertEqual(row['node1'], 'Joe')
                self.assertEqual(row['node2'], 'Joe')
                self.assertEqual(row['id.1'], 'w13')
                self.assertEqual(row['node1.1'], 'Joe')
                self.assertEqual(row['label.1'], 'works')
                self.assertEqual(row['node2.1'], 'Kaiser')
                self.assertEqual(row['node1;salary'], 20000)
                self.assertEqual(row['graph'], 'employ')

    def test_kgtk_query_default_multi_graph_join(self):
        cli_entry("kgtk", "query", "-i", self.file_path,
                  "-i", self.works_path,
                  "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "(x)-[:loves]->(y), w: (y)-[:works]->(c)", '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 3)
        for i, row in df.iterrows():
            if row['id'] == 'e14':
                self.assertEqual(row['node1'], 'Joe')
                self.assertEqual(row['node2'], 'Joe')
                self.assertEqual(row['id.1'], 'w13')
                self.assertEqual(row['node1.1'], 'Joe')
                self.assertEqual(row['label.1'], 'works')
                self.assertEqual(row['node2.1'], 'Kaiser')
                self.assertEqual(row['node1;salary'], 20000)
                self.assertEqual(row['graph'], 'employ')

    def test_kgtk_query_default_multi_graph_join_kgtk_compliant(self):
        cli_entry("kgtk", "query", "-i", self.file_path,
                  "-i", self.works_path,
                  "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "g: (x)-[r:loves]->(y), w: (y)-[:works]->(c)",
                  "--return", 'r, x, r.label, y as node2, c as `node2;work`', '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 3)
        for i, row in df.iterrows():
            if row['id'] == 'e11':
                self.assertEqual(row['node1'], 'Hans')
                self.assertEqual(row['node2'], 'Molly')
                self.assertEqual(row['node2;work'], 'Renal')

    def test_kgtk_query_default_multi_graph_join_property_access_restriction_cast_integer(self):
        cli_entry("kgtk", "query", "-i", self.file_path,
                  "-i", self.works_path,
                  "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "g: (x)-[r:loves]->(y), w: (y {salary: s})-[:works]->(c)",
                  "--where", "cast(s, integer) >= 10000",
                  "--return", 'r, x, r.label, y as node2, c as `node2;work`, s as `node2;salary`', '--graph-cache',
                  self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')

        self.assertTrue(len(df) == 2)
        for i, row in df.iterrows():
            if row['id'] == 'e11':
                self.assertEqual(row['node1'], 'Hans')
                self.assertEqual(row['node2'], 'Molly')
                self.assertEqual(row['node2;work'], 'Renal')

    def test_kgtk_query_multi_graph_ambiguous_return_alias(self):
        # Tests bug fix for case where 'node1'/'node2' return aliases are ambiguous for the two input graphs..
        cli_entry("kgtk", "query",
                  "-i", self.file_path, "-i", self.works_path, "-o", f'{self.temp_dir}/out.tsv',
                  "--match", "g: (:Susi)<-[:loves]-(n1), w: (n1)-[prop]->(n2)",
                  "--return", "prop, prop.label, n1 as node1, n2 as node2",
                  "--order-by", "node2",
                  "--graph-cache", self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 2)
        for i, row in df.iterrows():
            if row['id'] == 'w22':
                self.assertEqual(row['node1'], 'Otto')
                self.assertEqual(row['label'], 'department')
                self.assertEqual(row['node2'], 'Pharm')
                
    def test_kgtk_query_max(self):
        cli_entry("kgtk", "query", "-i", self.file_path,
                  "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "g: (x)-[r]->(y)",
                  "--return", 'max(x) as node1, r.label, y, r', '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 1)
        for i, row in df.iterrows():
            if row['id'] == 'e25':
                self.assertEqual(row['node1'], 'Susi')
                self.assertEqual(row['node2'], 'Susi')

    def test_kgtk_query_max_x_per_r(self):
        cli_entry("kgtk", "query", "-i", self.file_path,
                  "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "g: (x)-[r]->(y)",
                  "--return", 'r, max(x), r.label, y',
                  "--limit", "5", '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')

        self.assertTrue(len(df) == 5)
        ids = list(df['id'].unique())
        self.assertTrue('e11' in ids)
        self.assertTrue('e12' in ids)
        self.assertTrue('e13' in ids)
        self.assertTrue('e14' in ids)
        self.assertTrue('e21' in ids)

    def test_kgtk_query_count(self):
        cli_entry("kgtk", "query", "-i", self.file_path,
                  "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "g: (x)-[r]->(y)",
                  "--where", 'x = "Joe"',
                  "--return", 'count(x) as N', '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')

        self.assertTrue(len(df) == 1)
        for i, row in df.iterrows():
            self.assertEqual(row['N'], 3)

    def test_kgtk_query_count_distinct(self):
        cli_entry("kgtk", "query", "-i", self.file_path,
                  "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "g: (x)-[r]->(y)",
                  "--where", 'x = "Joe"',
                  "--return", 'count(distinct x) as N', '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 1)
        for i, row in df.iterrows():
            self.assertEqual(row['N'], 1)

    def test_kgtk_query_biggest_salary(self):
        cli_entry("kgtk", "query", "-i", self.works_path,
                  "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "w: (y {salary: s})-[r:works]->(c)",
                  "--return", 'max(cast(s, int)) as `node1;salary`, y, "works" as label, c, r', '--graph-cache',
                  self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 1)
        for i, row in df.iterrows():
            self.assertEqual(row['node1;salary'], 20000)
            self.assertEqual(row['node1'], 'Joe')
            self.assertEqual(row['node2'], 'Kaiser')

    def test_kgtk_query_date_filter(self):
        cli_entry("kgtk", "query", "-i", self.quals_path, "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "(eid)-[q]->(time)", "--where", "time.kgtk_date_year < 2005", '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 4)
        ids = list(df['id'].unique())
        self.assertTrue('m11' in ids)
        self.assertTrue('m12' in ids)
        self.assertTrue('m13' in ids)
        self.assertTrue('m14' in ids)

    def test_kgtk_query_three_graphs(self):
        cli_entry("kgtk", "query", "-i", self.works_path,
                  "-i", self.quals_path,
                  "-i", self.props_path,
                  "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "work: (x)-[r {label: rl}]->(y), qual: (r)-[rp {label: p}]->(time), prop: (p)-[:member]->(:set1)",
                  "--where", 'time.kgtk_date_year <= 2000',
                  "--return", 'r as id, x, rl, y, p as trel, time as time', '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 3)
        for i, row in df.iterrows():
            if row['id'] == 'w12':
                self.assertEqual(row['node1'], 'Otto')
                self.assertEqual(row['node2'], 'Kaiser')
                self.assertEqual(row['trel'], 'ends')
                self.assertEqual(row['time'], '^1987-11-08T04:56:34Z/10')

    def test_kgtk_query_property_enumeration_list(self):
        cli_entry("kgtk", "query", "-i", self.works_path,
                  "-i", self.quals_path,
                  "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "work: (x)-[r {label: rl}]->(y), qual: (r)-[rp {label: p}]->(time)",
                  "--where", "p in ['starts', 'ends'] and time.kgtk_date_year <= 2000",
                  "--return", 'r as id, x, rl, y, p as trel, time as time', '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 3)
        for i, row in df.iterrows():
            if row['id'] == 'w12':
                self.assertEqual(row['node1'], 'Otto')
                self.assertEqual(row['node2'], 'Kaiser')
                self.assertEqual(row['trel'], 'ends')
                self.assertEqual(row['time'], '^1987-11-08T04:56:34Z/10')

            if row['id'] == 'w11':
                self.assertEqual(row['node1'], 'Hans')
                self.assertEqual(row['node2'], 'ACME')
                self.assertEqual(row['trel'], 'starts')
                self.assertEqual(row['time'], '^1984-12-17T00:03:12Z/11')

    def test_kgtk_query_multi_graph_regex(self):
        cli_entry("kgtk", "query", "-i", self.works_path,
                  "-i", self.quals_path,
                  "-o", f'{self.temp_dir}/out.tsv', "--match",
                  "work: (x)-[r {label: rl}]->(y), qual: (r)-[rp {label: p}]->(time)",
                  "--where", "p =~ 's.*' and time.kgtk_date_year <= 2000",
                  "--return", 'r as id, x, rl, y, p as trel, time as time',
                  "--order-by", 'p desc, time asc', '--graph-cache', self.sqldb)
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 2)
        for i, row in df.iterrows():
            if row['id'] == 'w13':
                self.assertEqual(row['node1'], 'Joe')
                self.assertEqual(row['node2'], 'Kaiser')
                self.assertEqual(row['trel'], 'starts')
                self.assertEqual(row['time'], '^1996-02-23T08:02:56Z/09')

            if row['id'] == 'w11':
                self.assertEqual(row['node1'], 'Hans')
                self.assertEqual(row['node2'], 'ACME')
                self.assertEqual(row['trel'], 'starts')
                self.assertEqual(row['time'], '^1984-12-17T00:03:12Z/11')

    def test_kgtk_query_mod_operator(self):
        cli_entry('kgtk', 'query', '-i', self.file_path,
                  '--graph-cache', self.sqldb,
                  '-o', f'{self.temp_dir}/out.tsv',
                  '--match', '(n1)-[r:name]->(n2)',
                  '--return', 'r, n1, r.label, n2, length(n2) % 3 as rem')
                  
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 5)
        for i, row in df.iterrows():
            if row['id'] == 'e21':
                self.assertEqual(int(row['rem']), 0)
            if row['id'] == 'e22':
                self.assertEqual(int(row['rem']), 0)
            if row['id'] == 'e23':
                self.assertEqual(int(row['rem']), 2)
            if row['id'] == 'e24':
                self.assertEqual(int(row['rem']), 1)
            if row['id'] == 'e25':
                self.assertEqual(int(row['rem']), 0)

    def test_kgtk_query_order_by_alias(self):
        cli_entry('kgtk', 'query', '-i', self.file_path,
                  '--graph-cache', self.sqldb,
                  '-o', f'{self.temp_dir}/out.tsv',
                  '--match', '(n1)-[r:name]->(n2)',
                  '--return', 'r, n1, r.label, n2, length(n2) as `node2;len`',
                  '--order-by', '`node2;len`')
                  
        df = pd.read_csv(f'{self.temp_dir}/out.tsv', sep='\t')
        self.assertTrue(len(df) == 5)
        for i, row in df.iterrows():
            if i == 0:
                self.assertEqual(int(row['node2;len']), 5)
            if i == 1:
                self.assertEqual(int(row['node2;len']), 6)
            if i == 2:
                self.assertEqual(int(row['node2;len']), 7)
            if i == 3:
                self.assertEqual(int(row['node2;len']), 9)
            if i == 4:
                self.assertEqual(int(row['node2;len']), 9)


    ### Test helpers:
    
    def run_test_query(self, query, input=None, output=None, db=None):
        """Run KGTK 'query' command on 'input' test data and return the result as a dataframe.
        """
        input = input or self.file_path
        output = output or f'{self.temp_dir}/out.tsv'
        db = db or self.sqldb
        # we also support the LITERALS key here for compatibility:
        query = query.format(INPUT=input, LITERALS=input, OUTPUT=output, DB=db)
        cli_entry(*shlex.split(query))
        df = pd.read_csv(output, sep='\t')
        return df
    
    def result_to_dataframe(self, result):
        """Convert one or more 'result' rows into a dataframe.
        """
        if isinstance(result, str):
            result = [result]
        out = StringIO()
        for line in result:
            out.write(line)
            if not line.endswith('\n'):
                out.write('\n')
        df = pd.read_csv(StringIO(out.getvalue()), sep='\t')
        return df

    def assert_test_query_result(self, query_result, ok_result, rowids=None):
        """Assert that the dataframes 'query_result' and specified by 'ok_result' are the same.
        If 'rowids' is not None, only compare the specified rows.  This currently assumes that
        the rows are in the same order; we could generalize that down the line if necessary.
        """
        qdf = query_result
        rdf = self.result_to_dataframe(ok_result)
        if rowids is not None:
            if not isinstance(rowids, list):
                rowids = [rowids]
            qdf = qdf.loc[qdf['id'].isin(rowids)]
            rdf = rdf.loc[rdf['id'].isin(rowids)]
        self.assertTrue(qdf.equals(rdf))


    ### Testing literal accessors:
        
    def run_literal_access_query(self, query, literals=None, output=None, db=None):
        """Run KGTK 'query' command on literals test data and return the result as a dataframe.
        """
        literals = literals or self.literals_path
        return self.run_test_query(query=query, input=literals, output=output, db=db)

    def assert_literal_access_query_result(self, query, result, rowids=None,
                                           literals=None, output=None, db=None):
        """Assert that the dataframes produced by 'query' and defined by 'result' are the same.
        If 'rowids' is not None, only compare the specified rows.  This currently assumes that
        the rows are in the same order; we could generalize that down the line if necessary.
        """
        qdf = self.run_literal_access_query(query)
        self.assert_test_query_result(qdf, result, rowids=rowids)

    def test_kgtk_query_literal_access_kgtk_string(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:sy1)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_string(v) as `node2;is_string`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;is_string""",
                """esy1\tsy1\tsymbol\tFooBar\t0"""]
        self.assert_literal_access_query_result(query, result)

        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:st1)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_string(v) as `node2;is_string`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;is_string""",
                """est1\tst1\tstring\t"Franz Klammer"\t1"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_stringify(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:sy1)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_stringify(v) as `node2;as_string`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;as_string""",
                """esy1\tsy1\tsymbol\tFooBar\t"FooBar\""""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_unstringify(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:st2)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_unstringify(v) as `node2;as_symbol`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;as_symbol""",
                """est2\tst2\tstring\t"KGTK"\tKGTK"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_lqstring(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:st1)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_lqstring(v) as `node2;is_lqstring`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;is_lqstring""",
                """est1\tst1\tstring\t"Franz Klammer"\t0"""]
        self.assert_literal_access_query_result(query, result)

        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:lq1)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_lqstring(v) as `node2;is_lqstring`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;is_lqstring""",
                """elq1\tlq1\tlqstring\t'hans'@de\t1"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_lqstring_text(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:lq1)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_lqstring_text(v) as `node2;text`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;text""",
                """elq1\tlq1\tlqstring\t'hans'@de\thans"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_lqstring_text_string(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:lq1)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_lqstring_text_string(v) as `node2;string`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;string""",
                """elq1\tlq1\tlqstring\t'hans'@de\t"hans\""""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_lqstring_lang(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:lq1)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_lqstring_lang(v) as `node2;lang`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;lang""",
                """elq1\tlq1\tlqstring\t'hans'@de\tde"""]
        self.assert_literal_access_query_result(query, result)

        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:lq2)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_lqstring_lang(v) as `node2;lang`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;lang""",
                """elq2\tlq2\tlqstring\t'otto'@de-bav\tde"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_lqstring_suffix(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:lq1)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_lqstring_suffix(v) as `node2;suffix`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;suffix""",
                """elq1\tlq1\tlqstring\t'hans'@de"""]
        self.assert_literal_access_query_result(query, result)

        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:lq2)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_lqstring_suffix(v) as `node2;suffix`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;suffix""",
                """elq2\tlq2\tlqstring\t'otto'@de-bav\t-bav"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_lqstring_lang_suffix(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:lq1)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_lqstring_lang_suffix(v) as `node2;lang_suffix`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;lang_suffix""",
                """elq1\tlq1\tlqstring\t'hans'@de\tde"""]
        self.assert_literal_access_query_result(query, result)

        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:lq2)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_lqstring_lang_suffix(v) as `node2;lang_suffix`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;lang_suffix""",
                """elq2\tlq2\tlqstring\t'otto'@de-bav\tde-bav"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_date(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:lq1)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_date(v) as `node2;is_date`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;is_date""",
                """elq1\tlq1\tlqstring\t'hans'@de\t0"""]
        self.assert_literal_access_query_result(query, result)

        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:d6)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_date(v) as `node2;is_date`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;is_date""",
                """ed6\td6\tdate\t^2020-10-30T02:03:57+10:30/9\t1"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_date_date(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:d6)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_date_date(v) as `node2;date`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;date""",
                """ed6\td6\tdate\t^2020-10-30T02:03:57+10:30/9\t^2020-10-30"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_date_time(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:d6)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_date_time(v) as `node2;time`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;time""",
                """ed6\td6\tdate\t^2020-10-30T02:03:57+10:30/9\t^02:03:57+10:30"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_date_and_time(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:d6)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_date_and_time(v) as `node2;date_and_time`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;date_and_time""",
                """ed6\td6\tdate\t^2020-10-30T02:03:57+10:30/9\t^2020-10-30T02:03:57+10:30"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_date_year(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:d6)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_date_year(v) as `node2;year`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;year""",
                """ed6\td6\tdate\t^2020-10-30T02:03:57+10:30/9\t2020"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_date_month(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:d6)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_date_month(v) as `node2;month`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;month""",
                """ed6\td6\tdate\t^2020-10-30T02:03:57+10:30/9\t10"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_date_day(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:d6)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_date_day(v) as `node2;day`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;day""",
                """ed6\td6\tdate\t^2020-10-30T02:03:57+10:30/9\t30"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_date_hour(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:d6)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_date_hour(v) as `node2;hour`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;hour""",
                """ed6\td6\tdate\t^2020-10-30T02:03:57+10:30/9\t2"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_date_minutes(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:d6)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_date_minutes(v) as `node2;minutes`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;minutes""",
                """ed6\td6\tdate\t^2020-10-30T02:03:57+10:30/9\t3"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_date_seconds(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:d6)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_date_seconds(v) as `node2;seconds`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;seconds""",
                """ed6\td6\tdate\t^2020-10-30T02:03:57+10:30/9\t57"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_date_zone(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:d6)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_date_zone(v) as `node2;date_zone`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;date_zone""",
                """ed6\td6\tdate\t^2020-10-30T02:03:57+10:30/9\t+10:30"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_date_zone_string(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:d6)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_date_zone_string(v) as `node2;zone_string`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;zone_string""",
                """ed6\td6\tdate\t^2020-10-30T02:03:57+10:30/9\t"+10:30\""""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_date_precision(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:d6)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_date_precision(v) as `node2;precision`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;precision""",
                """ed6\td6\tdate\t^2020-10-30T02:03:57+10:30/9\t9"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_number(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1)-[r:quantity]->(v)'
                        --return 'r, n1, r.label, v, kgtk_number(v) as `node2;is_number`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;is_number""",
                """eq1\tq1\tquantity\t0\t1""",
                """eq2\tq2\tquantity\t0.0\t1""",
                """eq3\tq3\tquantity\t+1234\t1""",
                """eq4\tq4\tquantity\t-12345.1234\t1""",
                """eq5\tq5\tquantity\t4567.12e-10\t1""",
                """eq6\tq6\tquantity\t100m\t0""",
                """eq7\tq7\tquantity\t+1.609344e03[-0.1,+0.2]m\t0""",
                """eq8\tq8\tquantity\t1.609344e03[-0.1,+0.2]Q11573\t0"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_quantity(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1)-[r:quantity]->(v)'
                        --return 'r, n1, r.label, v, kgtk_quantity(v) as `node2;is_quantity`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;is_quantity""",
                """eq1\tq1\tquantity\t0\t0""",
                """eq2\tq2\tquantity\t0.0\t0""",
                """eq3\tq3\tquantity\t+1234\t0""",
                """eq4\tq4\tquantity\t-12345.1234\t0""",
                """eq5\tq5\tquantity\t4567.12e-10\t0""",
                """eq6\tq6\tquantity\t100m\t1""",
                """eq7\tq7\tquantity\t+1.609344e03[-0.1,+0.2]m\t1""",
                """eq8\tq8\tquantity\t1.609344e03[-0.1,+0.2]Q11573\t1"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_quantity_numeral(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1)-[r:quantity]->(v)'
                        --return 'r, n1, r.label, v, kgtk_quantity_numeral(v) as `node2;numeral`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;numeral""",
                """eq1\tq1\tquantity\t0\t0""",
                """eq2\tq2\tquantity\t0.0\t0.0""",
                """eq3\tq3\tquantity\t+1234\t+1234""",
                """eq4\tq4\tquantity\t-12345.1234\t-12345.1234""",
                """eq5\tq5\tquantity\t4567.12e-10\t4567.12e-10""",
                """eq6\tq6\tquantity\t100m\t100""",
                """eq7\tq7\tquantity\t+1.609344e03[-0.1,+0.2]m\t+1.609344e03""",
                """eq8\tq8\tquantity\t1.609344e03[-0.1,+0.2]Q11573\t1.609344e03"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_quantity_numeral_string(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1)-[r:quantity]->(v)'
                        --return 'r, n1, r.label, v, kgtk_quantity_numeral_string(v) as `node2;numeral_string`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;numeral_string""",
                """eq1\tq1\tquantity\t0\t"0\"""",
                """eq2\tq2\tquantity\t0.0\t"0.0\"""",
                """eq3\tq3\tquantity\t+1234\t"+1234\"""",
                """eq4\tq4\tquantity\t-12345.1234\t"-12345.1234\"""",
                """eq5\tq5\tquantity\t4567.12e-10\t"4567.12e-10\"""",
                """eq6\tq6\tquantity\t100m\t"100\"""",
                """eq7\tq7\tquantity\t+1.609344e03[-0.1,+0.2]m\t"+1.609344e03\"""",
                """eq8\tq8\tquantity\t1.609344e03[-0.1,+0.2]Q11573\t"1.609344e03\""""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_quantity_number(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1)-[r:quantity]->(v)'
                        --return 'r, n1, r.label, v, kgtk_quantity_number(v) as `node2;number`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;number""",
                """eq1\tq1\tquantity\t0\t0""",
                """eq2\tq2\tquantity\t0.0\t0.0""",
                """eq3\tq3\tquantity\t+1234\t1234""",
                """eq4\tq4\tquantity\t-12345.1234\t-12345.1234""",
                """eq5\tq5\tquantity\t4567.12e-10\t4.56712e-07""",
                """eq6\tq6\tquantity\t100m\t100""",
                """eq7\tq7\tquantity\t+1.609344e03[-0.1,+0.2]m\t1609.344""",
                """eq8\tq8\tquantity\t1.609344e03[-0.1,+0.2]Q11573\t1609.344"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_quantity_number_int(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1)-[r:quantity]->(v)'
                        --return 'r, n1, r.label, v, kgtk_quantity_number_int(v) as `node2;number_int`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;number_int""",
                """eq1\tq1\tquantity\t0\t0""",
                """eq2\tq2\tquantity\t0.0\t0""",
                """eq3\tq3\tquantity\t+1234\t1234""",
                """eq4\tq4\tquantity\t-12345.1234\t-12345""",
                """eq5\tq5\tquantity\t4567.12e-10\t0""",
                """eq6\tq6\tquantity\t100m\t100""",
                """eq7\tq7\tquantity\t+1.609344e03[-0.1,+0.2]m\t1609""",
                """eq8\tq8\tquantity\t1.609344e03[-0.1,+0.2]Q11573\t1609"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_quantity_number_float(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1)-[r:quantity]->(v)'
                        --return 'r, n1, r.label, v, kgtk_quantity_number_float(v) as `node2;number_float`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;number_float""",
                """eq1\tq1\tquantity\t0\t0.0""",
                """eq2\tq2\tquantity\t0.0\t0.0""",
                """eq3\tq3\tquantity\t+1234\t1234.0""",
                """eq4\tq4\tquantity\t-12345.1234\t-12345.1234""",
                """eq5\tq5\tquantity\t4567.12e-10\t4.56712e-07""",
                """eq6\tq6\tquantity\t100m\t100.0""",
                """eq7\tq7\tquantity\t+1.609344e03[-0.1,+0.2]m\t1609.344""",
                """eq8\tq8\tquantity\t1.609344e03[-0.1,+0.2]Q11573\t1609.344"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_quantity_si_units(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1)-[r:quantity]->(v)'
                        --return 'r, n1, r.label, v, kgtk_quantity_si_units(v) as `node2;si_units`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;si_units""",
                """eq1\tq1\tquantity\t0\t""",
                """eq2\tq2\tquantity\t0.0\t""",
                """eq3\tq3\tquantity\t+1234\t""",
                """eq4\tq4\tquantity\t-12345.1234\t""",
                """eq5\tq5\tquantity\t4567.12e-10\t""",
                """eq6\tq6\tquantity\t100m\tm""",
                """eq7\tq7\tquantity\t+1.609344e03[-0.1,+0.2]m\tm""",
                """eq8\tq8\tquantity\t1.609344e03[-0.1,+0.2]Q11573\t"""]
        self.assert_literal_access_query_result(query, result, rowids=['eq5', 'eq6', 'eq7', 'eq8'])

    def test_kgtk_query_literal_access_kgtk_quantity_wd_units(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1)-[r:quantity]->(v)'
                        --return 'r, n1, r.label, v, kgtk_quantity_wd_units(v) as `node2;wd_units`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;wd_units""",
                """eq1\tq1\tquantity\t0\t""",
                """eq2\tq2\tquantity\t0.0\t""",
                """eq3\tq3\tquantity\t+1234\t""",
                """eq4\tq4\tquantity\t-12345.1234\t""",
                """eq5\tq5\tquantity\t4567.12e-10\t""",
                """eq6\tq6\tquantity\t100m\t""",
                """eq7\tq7\tquantity\t+1.609344e03[-0.1,+0.2]m\t""",
                """eq8\tq8\tquantity\t1.609344e03[-0.1,+0.2]Q11573\tQ11573"""]
        self.assert_literal_access_query_result(query, result, rowids=['eq5', 'eq6', 'eq7', 'eq8'])

    def test_kgtk_query_literal_access_kgtk_quantity_tolerance(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1)-[r:quantity]->(v)'
                        --return 'r, n1, r.label, v, kgtk_quantity_tolerance(v) as `node2;tolerance`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;tolerance""",
                """eq1\tq1\tquantity\t0\t""",
                """eq2\tq2\tquantity\t0.0\t""",
                """eq3\tq3\tquantity\t+1234\t""",
                """eq4\tq4\tquantity\t-12345.1234\t""",
                """eq5\tq5\tquantity\t4567.12e-10\t""",
                """eq6\tq6\tquantity\t100m\t""",
                """eq7\tq7\tquantity\t+1.609344e03[-0.1,+0.2]m\t[-0.1,+0.2]""",
                """eq8\tq8\tquantity\t1.609344e03[-0.1,+0.2]Q11573\t[-0.1,+0.2]"""]
        self.assert_literal_access_query_result(query, result, rowids=['eq5', 'eq6', 'eq7', 'eq8'])

    def test_kgtk_query_literal_access_kgtk_quantity_tolerance_string(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1)-[r:quantity]->(v)'
                        --return 'r, n1, r.label, v, kgtk_quantity_tolerance_string(v) as `node2;tolerance_string`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;tolerance_string""",
                """eq1\tq1\tquantity\t0\t""",
                """eq2\tq2\tquantity\t0.0\t""",
                """eq3\tq3\tquantity\t+1234\t""",
                """eq4\tq4\tquantity\t-12345.1234\t""",
                """eq5\tq5\tquantity\t4567.12e-10\t""",
                """eq6\tq6\tquantity\t100m\t""",
                """eq7\tq7\tquantity\t+1.609344e03[-0.1,+0.2]m\t"[-0.1,+0.2]\"""",
                """eq8\tq8\tquantity\t1.609344e03[-0.1,+0.2]Q11573\t"[-0.1,+0.2]\""""]
        self.assert_literal_access_query_result(query, result, rowids=['eq5', 'eq6', 'eq7', 'eq8'])

    def test_kgtk_query_literal_access_kgtk_quantity_low_tolerance(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1)-[r:quantity]->(v)'
                        --return 'r, n1, r.label, v, kgtk_quantity_low_tolerance(v) as `node2;low_tolerance`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;low_tolerance""",
                """eq1\tq1\tquantity\t0\t""",
                """eq2\tq2\tquantity\t0.0\t""",
                """eq3\tq3\tquantity\t+1234\t""",
                """eq4\tq4\tquantity\t-12345.1234\t""",
                """eq5\tq5\tquantity\t4567.12e-10\t""",
                """eq6\tq6\tquantity\t100m\t""",
                """eq7\tq7\tquantity\t+1.609344e03[-0.1,+0.2]m\t-0.1""",
                """eq8\tq8\tquantity\t1.609344e03[-0.1,+0.2]Q11573\t-0.1"""]
        self.assert_literal_access_query_result(query, result, rowids=['eq5', 'eq6', 'eq7', 'eq8'])

    def test_kgtk_query_literal_access_kgtk_quantity_high_tolerance(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1)-[r:quantity]->(v)'
                        --return 'r, n1, r.label, v, kgtk_quantity_high_tolerance(v) as `node2;high_tolerance`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;high_tolerance""",
                """eq1\tq1\tquantity\t0\t""",
                """eq2\tq2\tquantity\t0.0\t""",
                """eq3\tq3\tquantity\t+1234\t""",
                """eq4\tq4\tquantity\t-12345.1234\t""",
                """eq5\tq5\tquantity\t4567.12e-10\t""",
                """eq6\tq6\tquantity\t100m\t""",
                """eq7\tq7\tquantity\t+1.609344e03[-0.1,+0.2]m\t0.2""",
                """eq8\tq8\tquantity\t1.609344e03[-0.1,+0.2]Q11573\t0.2"""]
        self.assert_literal_access_query_result(query, result, rowids=['eq5', 'eq6', 'eq7', 'eq8'])

    def test_kgtk_query_literal_access_kgtk_geo_coords(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1:st1)-[r]->(v)'
                        --return 'r, n1, r.label, v, kgtk_geo_coords(v) as `node2;is_geo_coords`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;is_geo_coords""",
                """est1\tst1\tstring\t"Franz Klammer"\t0"""]
        self.assert_literal_access_query_result(query, result)

        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1)-[r:geoloc]->(v)'
                        --return 'r, n1, r.label, v, kgtk_geo_coords(v) as `node2;is_geo_coords`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;is_geo_coords""",
                """egl1\tgl1\tgeoloc\t@-42.42/69.123\t1""",
                """egl2\tgl2\tgeoloc\t@19.42/-69.123e-1\t1"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_geo_coords_lat(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1)-[r:geoloc]->(v)'
                        --return 'r, n1, r.label, v, kgtk_geo_coords_lat(v) as `node2;latitude`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;latitude""",
                """egl1\tgl1\tgeoloc\t@-42.42/69.123\t-42.42""",
                """egl2\tgl2\tgeoloc\t@19.42/-69.123e-1\t19.42"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_kgtk_geo_coords_long(self):
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1)-[r:geoloc]->(v)'
                        --return 'r, n1, r.label, v, kgtk_geo_coords_long(v) as `node2;longitude`'
                """
        result=["""id\tnode1\tlabel\tnode2\tnode2;longitude""",
                """egl1\tgl1\tgeoloc\t@-42.42/69.123\t69.123""",
                """egl2\tgl2\tgeoloc\t@19.42/-69.123e-1\t-6.9123"""]
        self.assert_literal_access_query_result(query, result)

    def test_kgtk_query_literal_access_big_numbers(self):
        """Test overflow from very long integer values and parsing of floating point constants.
        """
        query = """kgtk query -i {LITERALS} -o {OUTPUT} --graph-cache {DB}
                        --match  '(n1)-[r]->(v)' --limit 1
                        --return 'kgtk_quantity_number("+162000000000000000000000Q122922") as n1, \
                                  kgtk_quantity_number("-162000000000000000000000Q122922") as n2, \
                                  kgtk_quantity_number_int("+162000000000000000000000Q122922") as n3, \
                                  kgtk_quantity_number_int("+162000000000000000000000Q122922") as n4, \
                                  kgtk_quantity_number_float("+162000000000000000000000Q122922") as n5, \
                                  kgtk_quantity_number_float("-162000000000000000000000Q122922") as n6, \
                                  1.7976931348623157e+308 as f1, +1.7976931348623157e+308 as f2, -1.7976931348623157e+308 as f3, \
                                  2.2250738585072014e-308 as f4, +2.2250738585072014e-308 as f5, -2.2250738585072014e-308 as f6 \
                                 '
                """
        # TO DO: we might need to make this test more tolerant to work around any floating point precision issues:
        result=["""n1\tn2\tn3\tn4\tn5\tn6\tf1\tf2\tf3\tf4\tf5\tf6""",
                """1.62e+23\t-1.62e+23\t9223372036854775807\t9223372036854775807\t1.62e+23\t-1.62e+23"""
                + """\t1.7976931348623157e+308\t1.7976931348623157e+308\t-1.7976931348623157e+308\t"""
                + """2.2250738585072014e-308\t2.2250738585072014e-308\t-2.2250738585072014e-308"""]
        self.assert_literal_access_query_result(query, result)


    ### Testing pyeval:

    def test_kgtk_query_pyeval(self):
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB} --limit 1
                        --return 'pyeval(printf($FMT, "Otto")) as value' --para FMT="'%s'.swapcase()"
                """
        result=["""value""",
                """oTTO"""]
        qdf = self.run_test_query(query)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_pyeval_multi(self):
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB} --limit 1
                        --return 'pyeval(char(34), "Otto", char(34), ".swapcase()") as value'
                """
        result=["""value""",
                """oTTO"""]
        qdf = self.run_test_query(query)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_pycall_0(self):
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB} --import uuid --limit 1
                        --return 'pycall("uuid.uuid4") as value'
                """
        import uuid
        qdf = self.run_test_query(query)
        self.assertTrue(len(qdf) == 1)
        for i, row in qdf.iterrows():
            self.assertEqual(len(row['value']), len(str(uuid.uuid4())))

    def test_kgtk_query_pycall_1(self):
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB} --limit 1
                        --return 'pycall("list", "Otto") as value'
                """
        result=["""value""",
                """['O', 't', 't', 'o']"""]
        qdf = self.run_test_query(query)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_pycall_2(self):
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB} --import math --limit 1
                        --return 'pycall("math.fmod", 42, 17) as value'
                """
        result=["""value""",
                """8.0"""]
        qdf = self.run_test_query(query)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_pycall_3(self):
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB} --limit 1
                        --return 'pycall("max", 1, 2, 3) as value'
                """
        result=["""value""",
                """3"""]
        qdf = self.run_test_query(query)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_pycall_4(self):
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB} --limit 1
                        --return 'pycall("max", 1, 2, 3, 4) as value'
                """
        result=["""value""",
                """4"""]
        qdf = self.run_test_query(query)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_pycall_5(self):
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB} --limit 1
                        --return 'pycall("max", 1, 2, 3, 4, 5) as value'
                """
        result=["""value""",
                """5"""]
        qdf = self.run_test_query(query)
        self.assert_test_query_result(qdf, result)


    ### Testing optional match (queries straight from the manual):

    def test_kgtk_query_optional_strict(self):
        # Initial non-optional strict query - for good measure.
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match  'w: (p)-[r:works]->(c), g: (p)-[:name]->(n), q: (r)-[:starts]->(s)'
                        --return 'c as company, p as employee, n as name, s as start'
                """
        result = ["""company\temployee\tname\tstart""",
                  """ACME\tHans\t'Hans'@de\t^1984-12-17T00:03:12Z/11""",
                  """Kaiser\tJoe\t"Joe"\t^1996-02-23T08:02:56Z/09""",
                  """Cakes\tSusi\t"Susi"\t^2008-10-01T12:49:18Z/07"""]
        inputs = ' '.join([self.file_path, self.works_path, self.quals_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_optional_start_date(self):
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match  'w: (p)-[r:works]->(c), g: (p)-[:name]->(n)'
                        --opt    'q: (r)-[:starts]->(s)'
                        --return 'c as company, p as employee, n as name, s as start'
                """
        result = ["""company\temployee\tname\tstart""",
                  """ACME\tHans\t'Hans'@de\t^1984-12-17T00:03:12Z/11""",
                  """Kaiser\tOtto\t'Otto'@de\t""",
                  """Kaiser\tJoe\t"Joe"\t^1996-02-23T08:02:56Z/09""",
                  """Renal\tMolly\t"Molly"\t""",
                  """Cakes\tSusi\t"Susi"\t^2008-10-01T12:49:18Z/07"""]
        inputs = ' '.join([self.file_path, self.works_path, self.quals_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_optional_independent_start_and_end(self):
        # Multiple independent optionals for start and/or end dates:
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match  'w: (p)-[r:works]->(c), g: (p)-[:name]->(n)'
                        --opt    'q: (r)-[:starts]->(s)'
                        --opt    'q: (r)-[:ends]->(e)'
                        --return 'c as company, p as employee, n as name, s as start, e as end'
                """
        result = ["""company\temployee\tname\tstart\tend""",
                  """ACME\tHans\t'Hans'@de\t^1984-12-17T00:03:12Z/11\t""",
                  """Kaiser\tOtto\t'Otto'@de\t\t^1987-11-08T04:56:34Z/10""",
                  """Kaiser\tJoe\t"Joe"\t^1996-02-23T08:02:56Z/09\t""",
                  """Renal\tMolly\t"Molly"\t\t^2001-04-09T06:16:27Z/08""",
                  """Cakes\tSusi\t"Susi"\t^2008-10-01T12:49:18Z/07\t"""]
        inputs = ' '.join([self.file_path, self.works_path, self.quals_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_optional_join_with_where(self):
        # Optional join with where (note that optional clauses do not inherit the last graph variable
        # from the previous match clause, so we could have omitted the `g` specification):
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match 'w: (p)-[r:works]->(c)'
                        --opt   'g: (p)-[r2]->(l)-[:name]->(ln)'
                        --where 'r2.label != "name" and kgtk_null_to_empty(kgtk_lqstring_lang(ln)) != "de"'
                        --return 'c as company, p as employee, r2.label as affrel, l as affiliate, ln as name'
                """
        result = ["""company\temployee\taffrel\taffiliate\tname""",
                  """ACME\tHans\tloves\tMolly\t"Molly\"""",
                  """Kaiser\tOtto\tloves\tSusi\t"Susi\"""",
                  """Kaiser\tJoe\tloves\tJoe\t"Joe\"""",
                  """Renal\tMolly\t\t\t""",
                  """Cakes\tSusi\t\t\t"""]
        inputs = ' '.join([self.file_path, self.works_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_optional_on_optional_with_independent_wheres(self):
        # Optional on optional with independent where clauses, which gives more results:
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match 'w: (p)-[r:works]->(c)'
                        --opt   'g: (p)-[r2]->(l)'
                        --where 'r2.label != "name"'
                        --opt   'g: (l)-[:name]->(ln)'
                        --where 'kgtk_null_to_empty(kgtk_lqstring_lang(ln)) != "de"'
                        --return 'c as company, p as employee, r2.label as affrel, l as affiliate, ln as name'
                """
        result = ["""company\temployee\taffrel\taffiliate\tname""",
                  """ACME\tHans\tloves\tMolly\t"Molly\"""",
                  """Kaiser\tOtto\tloves\tSusi\t"Susi\"""",
                  """Kaiser\tJoe\tfriend\tOtto\t""",
                  """Kaiser\tJoe\tloves\tJoe\t"Joe\"""",
                  """Renal\tMolly\t\t\t""",
                  """Cakes\tSusi\t\t\t"""]
        inputs = ' '.join([self.file_path, self.works_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_optional_where_on_every_match(self):
        # "Where Mania" - same query as before:
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match 'w: (p)-[r]->(c)'
                        --where 'r.label = "works"'
                        --opt   'g: (p)-[r2]->(l)'
                        --where 'r2.label != "name"'
                        --opt   'g: (l)-[:name]->(ln)'
                        --where 'kgtk_null_to_empty(kgtk_lqstring_lang(ln)) != "de"'
                        --return 'c as company, p as employee, r2.label as affrel, l as affiliate, ln as name'
                """
        result = ["""company\temployee\taffrel\taffiliate\tname""",
                  """ACME\tHans\tloves\tMolly\t"Molly\"""",
                  """Kaiser\tOtto\tloves\tSusi\t"Susi\"""",
                  """Kaiser\tJoe\tfriend\tOtto\t""",
                  """Kaiser\tJoe\tloves\tJoe\t"Joe\"""",
                  """Renal\tMolly\t\t\t""",
                  """Cakes\tSusi\t\t\t"""]
        inputs = ' '.join([self.file_path, self.works_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_optional_emulating_not_exists_with_global_where(self):
        # Emulating "not exists" via optionals and global `--where:` clause:
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match  'w: (p)-[r]->(c)'
                        --where  'r.label = "works"'
                        --opt    'g: (p)-[r2]->(l)'
                        --where  'r2.label != "name"'
                        --opt    'g: (l)-[:name]->(ln)'
                        --where  'kgtk_null_to_empty(kgtk_lqstring_lang(ln)) != "de"'
                        --where: 'ln is null'
                        --return 'c as company, p as employee, r2.label as affrel, l as affiliate, ln as name'
                """
        result = ["""company\temployee\taffrel\taffiliate\tname""",
                  """Kaiser\tJoe\tfriend\tOtto\t""",
                  """Renal\tMolly\t\t\t""",
                  """Cakes\tSusi\t\t\t"""]
        inputs = ' '.join([self.file_path, self.works_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_optional_global_where_is_with_where(self):
        # `--where:` is a shorthand for `--with * --where...`:
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match 'w: (p)-[r]->(c)'
                        --where 'r.label = "works"'
                        --opt   'g: (p)-[r2]->(l)'
                        --where 'r2.label != "name"'
                        --opt   'g: (l)-[:name]->(ln)'
                        --where 'kgtk_null_to_empty(kgtk_lqstring_lang(ln)) != "de"'
                        --with  '*'
                        --where 'ln is null'
                        --return 'c as company, p as employee, r2.label as affrel, l as affiliate, ln as name'
                """
        result = ["""company\temployee\taffrel\taffiliate\tname""",
                  """Kaiser\tJoe\tfriend\tOtto\t""",
                  """Renal\tMolly\t\t\t""",
                  """Cakes\tSusi\t\t\t"""]
        inputs = ' '.join([self.file_path, self.works_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_optional_incorrect_not_exists(self):
        # Incorrect "not exists", we cannot test for NULL inside the optional clause and
        # now that clause always fails, therefore all names are NULL:
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match 'w: (p)-[r]->(c)'
                        --where 'r.label = "works"'
                        --opt   'g: (p)-[r2]->(l)'
                        --where 'r2.label != "name"'
                        --opt   'g: (l)-[:name]->(ln)'
                        --where 'kgtk_null_to_empty(kgtk_lqstring_lang(ln)) != "de" and ln is null'
                        --return 'c as company, p as employee, r2.label as affrel, l as affiliate, ln as name'
                """
        result = ["""company\temployee\taffrel\taffiliate\tname""",
                  """ACME\tHans\tloves\tMolly\t""",
                  """Kaiser\tOtto\tloves\tSusi\t""",
                  """Kaiser\tJoe\tfriend\tOtto\t""",
                  """Kaiser\tJoe\tloves\tJoe\t""",
                  """Renal\tMolly\t\t\t""",
                  """Cakes\tSusi\t\t\t"""]
        inputs = ' '.join([self.file_path, self.works_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_optional_find_symmetric_edges(self):
        # Finding symmetric edges:
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match 'g: (x)-[r]->(y)'
                        --where 'r.label != "name"'
                        --opt   'g: (y)-[r2]->(x)'
                        --where 'r.label = r2.label'
                        --return 'x, r.label, y, r2 is not null as symmetric'
                """
        result = ["""node1\tlabel\tnode2\tsymmetric""",
                  """Hans\tloves\tMolly\t0""",
                  """Otto\tloves\tSusi\t0""",
                  """Joe\tfriend\tOtto\t0""",
                  """Joe\tloves\tJoe\t1"""]
        inputs = ' '.join([self.file_path, self.works_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_multi_edges_with_optional(self):
        # Output multi-edges combined with optionals:
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --multi 3
                        --match 'g: (x)-[r1:loves]->(y),
                                 w: (x)-[r2:works]->(c)'
                        --opt   'g: (x)-[r3:friend]->(f)'
                        --return 'x, r1.label, y,
                                  x, r2.label, c,
                                  x, r3.label, f'
                """
        result = ["""node1\tlabel\tnode2""",
                  """Hans\tloves\tMolly""",
                  """Hans\tworks\tACME""",
                  """Otto\tloves\tSusi""",
                  """Otto\tworks\tKaiser""",
                  """Joe\tloves\tJoe""",
                  """Joe\tworks\tKaiser""",
                  """Joe\tfriend\tOtto"""]
        inputs = ' '.join([self.file_path, self.works_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_optional_where_vars_are_local(self):
        # Test for a bug fix in optional where clause variable translation:
        # the variable in 'x > "Joe"' needs to be translated relative to
        # the local match clause as g.x and not w.x, since we use a nested
        # join based on the optional pattern and restriction to compute
        # the table that is then left-joined with the table of the strict match:
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match 'w: (x)-[:works]->(c)'
                        --opt   'g: ()-[:loves]->(x), (x)-[:name]->(n)'
                        --where 'x > "Joe"'
                       --return 'x as person, n as name, c as company'
                """
        result = ["""person\tname\tcompany""",
                  """Hans\t\tACME""",
                  """Otto\t\tKaiser""",
                  """Joe\t\tKaiser""",
                  """Molly\t"Molly"\tRenal""",
                  """Susi\t"Susi"\tCakes"""]
        inputs = ' '.join([self.file_path, self.works_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_optional_where_vars_are_local_strict_variant(self):
        # For reference, this moves the where clause into the strict match which
        # creates a different result, since now it is evaluated for each source edge,
        # while before the optional simply failed if either the loves edge wasn't
        # present or the where restriction failed in which case the result was just null:
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match 'w: (x)-[:works]->(c)'
                        --where 'x > "Joe"'
                        --opt   'g: ()-[:loves]->(x), (x)-[:name]->(n)'
                       --return 'x as person, n as name, c as company'
                """
        result = ["""person\tname\tcompany""",
                  """Molly\t"Molly"\tRenal""",
                  """Otto\t\tKaiser""",
                  """Susi\t"Susi"\tCakes"""]
        inputs = ' '.join([self.file_path, self.works_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)
        

    def test_kgtk_query_special_functions(self):
        # Test functions such as 'concat' and 'likelihood' that require special translation:
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match 'g: (x)-[r1:loves]->(y), \
                                 w: (x)-[r2:works]->(c)' \
                        --where 'likelihood(not x is null, 0.9)' \
                        --return 'lower(concat(x, y, 3, c, 2.5)) as value'
                """
        result = ["""value""",
                  """hansmolly3acme2.5""",
                  """ottosusi3kaiser2.5""",
                  """joejoe3kaiser2.5"""]
        inputs = ' '.join([self.file_path, self.works_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_exists_explicit_people_who_are_loved(self):
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match '(x)-[:name]->(n)'
                        --where 'EXISTS {{()-[:loves]->(x)}}'
                        --return 'x as node1, n as name'
                """
        result = ['''node1\tname''',
                  '''Joe\t"Joe"''',
                  '''Molly\t"Molly"''',
                  '''Susi\t"Susi"''']
        inputs = ' '.join([self.file_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)
        
    def test_kgtk_query_exists_explicit_people_who_are_loved_and_rich(self):
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match '(x)-[:name]->(n)'
                        --where 'EXISTS {{()-[:loves]->(x), w: (x {{salary: s}})-[:works]->()
                                         WHERE cast(s, int) >= 10000}}'
                        --return 'x as node1, n as name'
                """
        result = ['''node1\tname''',
                  '''Joe\t"Joe"''',
                  '''Molly\t"Molly"''']
        inputs = ' '.join([self.file_path, self.works_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_exists_function_people_who_are_loved(self):
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match '(x)-[:name]->(n)'
                        --where 'EXISTS(()-[:loves]->(x))'
                        --return 'x as node1, n as name'
                """
        result = ['''node1\tname''',
                  '''Joe\t"Joe"''',
                  '''Molly\t"Molly"''',
                  '''Susi\t"Susi"''']
        inputs = ' '.join([self.file_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)
        
    def test_kgtk_query_exists_implicit_people_who_are_loved(self):
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match '(x)-[:name]->(n)'
                        --where '()-[:loves]->(x)'
                        --return 'x as node1, n as name'
                """
        result = ['''node1\tname''',
                  '''Joe\t"Joe"''',
                  '''Molly\t"Molly"''',
                  '''Susi\t"Susi"''']
        inputs = ' '.join([self.file_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)
        
    def test_kgtk_query_exists_implicit_in_return(self):
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match '(x)-[:name]->(n)'
                        --return 'x as node1, n as name, ()-[:loves]->(x) or ()-[:friend]->(x) as happy'
                """
        result = ["""node1\tname\thappy""",
                  """Hans\t'Hans'@de\t0""",
                  """Otto\t'Otto'@de\t1""",
                  """Joe\t"Joe"\t1""",
                  """Molly\t"Molly"\t1""",
                  """Susi\t"Susi"\t1"""]
        inputs = ' '.join([self.file_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)
        
    def test_kgtk_query_exists_implicit_pattern_chain(self):
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match '(x)-[:name]->(n)'
                        --where '()-[:loves]->(x)-[:friend]->()'
                        --return 'x as node1, n as name'
                """
        result = ['''node1\tname''',
                  '''Joe\t"Joe"''']
        inputs = ' '.join([self.file_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)
        
    def test_kgtk_query_exists_implicit_pattern_chain_new_variable_error(self):
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match '(x)-[:name]->(n)'
                        --where '()-[:loves]->(x)-[:friend]->(f)'
                        --return 'x as node1, n as name'
                """
        inputs = ' '.join([self.file_path])
        self.assertRaises(Exception, self.run_test_query, query, inputs)
        
    def test_kgtk_query_exists_explicit_nested(self):
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match '(x)-[:name]->(n)'
                        --where 'EXISTS {{()-[:loves]->(x), \
                                         w: (x)-[wr:works]->() \
                                         WHERE NOT EXISTS {{q: (wr)-[:ends]->(e) \
                                                           WHERE e < "^2000"}}}}' \
                        --return 'x as node1, n as name'
                """
        result = ['''node1\tname''',
                  '''Joe\t"Joe"''',
                  '''Molly\t"Molly"''',
                  '''Susi\t"Susi"''']
        inputs = ' '.join([self.file_path, self.works_path, self.quals_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)


    def test_kgtk_query_implicit_default_graph_already_used_1(self):
        """Fail because the default graph is already mapped to 'g' and thus can't be used implicitly later.
        """
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match 'g: (x)-[:name]->(n)'
                        --where 'exists(()-[:loves]->(x))'
                        --return 'x as node1, n as name'
                """
        inputs = ' '.join([self.file_path])
        self.assertRaises(Exception, self.run_test_query, query, inputs)

    def test_kgtk_query_implicit_default_graph_already_used_2(self):
        """Fail because the default graph is already mapped implicitly and thus can't be mapped to 'g' later.
        """
        query = """kgtk query -i {INPUT} -o {OUTPUT} --graph-cache {DB}
                        --match '(x)-[:name]->(n)'
                        --where 'exists(g: ()-[:loves]->(x))'
                        --return 'x as node1, n as name'
                """
        inputs = ' '.join([self.file_path])
        self.assertRaises(Exception, self.run_test_query, query, inputs)


    def test_kgtk_query_kypherv_import_embeddings_with_defaults(self):
        # Kypher-V manual example:
        query = """kgtk query -o {OUTPUT} --graph-cache {DB}
                        -i {INPUT} --idx vector:node2 mode:valuegraph
                        --match '(x)-[r]->(v)'
                        --return 'r as id, x as node1, r.label as label, kgtk_stringify(substr(kvec_to_base64(v), 2, 20)) as node2'
                        --limit 5
                """
        result = [
            '''id\tnode1\tlabel\tnode2''',
            '''e-3bc7d18e\tQ100428034\temb\t"5oXdvZaFe78lxhm/xfy2"''',
            '''e-ecf67b59\tQ10061\temb\t"kOTZvbezFr81FoG+QhgK"''',
            '''e-46106323\tQ101638\temb\t"2cQevgXyib91AWu+cv5h"''',
            '''e-b06fd3c7\tQ101911\temb\t"kUQ0vaJISL+MI4g9rvwa"''',
            '''e-842953ca\tQ102118866\temb\t"000Hv645Qr/KVFu9eCk/"''',
        ]
        inputs = ' '.join([self.embed_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_kypherv_import_embeddings_with_minimal_defaults(self):
        # Kypher-V manual example:
        query = """kgtk query -o {OUTPUT} --graph-cache {DB}
                        -i {INPUT} --idx vector: mode:valuegraph
                        --match '(x)-[r]->(v)'
                        --return 'r as id, x as node1, r.label as label, kgtk_stringify(substr(kvec_to_base64(v), 2, 20)) as node2'
                        --limit 2
                """
        result = [
            '''id\tnode1\tlabel\tnode2''',
            '''e-3bc7d18e\tQ100428034\temb\t"5oXdvZaFe78lxhm/xfy2"''',
            '''e-ecf67b59\tQ10061\temb\t"kOTZvbezFr81FoG+QhgK"''',
        ]
        inputs = ' '.join([self.embed_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_kypherv_import_embeddings_with_options(self):
        # Kypher-V manual example:
        query = """kgtk query -o {OUTPUT} --graph-cache {DB}
                        -i {INPUT} --idx vector:node2/fmt=auto/dtype=float32/store=inline/norm=False mode:valuegraph
                        --match '(x)-[r]->(v)'
                        --return 'r as id, x as node1, r.label as label, kgtk_stringify(substr(kvec_to_base64(v), 2, 20)) as node2'
                        --limit 2
                """
        result = [
            '''id\tnode1\tlabel\tnode2''',
            '''e-3bc7d18e\tQ100428034\temb\t"5oXdvZaFe78lxhm/xfy2"''',
            '''e-ecf67b59\tQ10061\temb\t"kOTZvbezFr81FoG+QhgK"''',
        ]
        inputs = ' '.join([self.embed_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_kypherv_basic_similarity(self):
        # Kypher-V manual example:
        query = """kgtk query -o {OUTPUT} --graph-cache {DB}
                        -i {INPUT} --idx vector: mode:valuegraph
                        --match '`embed.tsv`: (x:Q868)-[]->(xv),
                                              (y:Q913)-[]->(yv),
                                 `labels.tsv`: (x)-[]->(xl),
                                               (y)-[]->(yl)'
                         --return 'xl as xlabel, yl as ylabel, substr(kvec_cos_sim(xv, yv), 1, 8) as sim'
                """
        result = [
            """xlabel\tylabel\tsim""",
            """'Aristotle'@en\t'Socrates'@en\t0.692607""",
        ]
        # we list labels first, so the --idx spec applies to the last embed input:
        inputs = ' '.join([self.embed_labels_path, self.embed_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_kypherv_similarity_to_random_vector(self):
        # Kypher-V manual example:
        query = """kgtk query -o {OUTPUT} --graph-cache {DB}
                        -i {INPUT} --idx vector: mode:valuegraph
                        --match '`embed.tsv`: (x:Q868)-[]->(xv),
                                 `labels.tsv`: (x)-[]->(xl)'
                         --return 'xl as xlabel, substr(kvec_cos_sim(xv, kvec_unstringify(pyeval("[1] * 100"))), 1, 8) as sim'
                """
        result = [
            """xlabel\tsim""",
            """'Aristotle'@en\t0.003323""",
        ]
        # we list labels first, so the --idx spec applies to the last embed input:
        inputs = ' '.join([self.embed_labels_path, self.embed_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_kypherv_cos_sim_via_dot_product(self):
        # Kypher-V manual example:
        query = """kgtk query -o {OUTPUT} --graph-cache {DB}
                        -i {INPUT} --idx vector: mode:valuegraph
                        --match '`embed.tsv`: (x:Q868)-[]->(xv),
                                              (y:Q913)-[]->(yv),
                                 `labels.tsv`: (x)-[]->(xl),
                                               (y)-[]->(yl)'
                         --return 'xl as xlabel, yl as ylabel,
                                   substr(kvec_dot(kvec_divide(xv, kvec_l2_norm(xv)), kvec_divide(yv, kvec_l2_norm(yv))), 1, 8) as sim'
                """
        result = [
            """xlabel\tylabel\tsim""",
            """'Aristotle'@en\t'Socrates'@en\t0.692607""",
        ]
        # we list labels first, so the --idx spec applies to the last embed input:
        inputs = ' '.join([self.embed_labels_path, self.embed_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_kypherv_brute_force_sim_search(self):
        # Kypher-V manual example:
        query = """kgtk query -o {OUTPUT} --graph-cache {DB}
                        -i {INPUT} --idx vector: mode:valuegraph
                        --match '`embed.tsv`: (x:Q913)-[]->(xv),
                                              (y)-[]->(yv),
                                 `labels.tsv`: (x)-[]->(xl),
                                               (y)-[]->(yl)'
                        --return 'x as x, xl as xlabel, y as y, yl as ylabel, substr(kvec_cos_sim(xv, yv), 1, 8) as sim'
                        --order  'sim desc'
                        --limit 5
                """
        result = [
            """x\txlabel\ty\tylabel\tsim""",
            """Q913\t'Socrates'@en\tQ913\t'Socrates'@en\t1.0""",
            """Q913\t'Socrates'@en\tQ179149\t'Antisthenes'@en\t0.824994""",
            """Q913\t'Socrates'@en\tQ409647\t'Aeschines of Sphettus'@en\t0.814151""",
            """Q913\t'Socrates'@en\tQ666230\t'Aristobulus of Paneas'@en\t0.801446""",
            """Q913\t'Socrates'@en\tQ380190\t'Phaedo of Elis'@en\t0.785770""",
        ]
        # we list labels first, so the --idx spec applies to the last embed input:
        inputs = ' '.join([self.embed_labels_path, self.embed_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)

    def test_kgtk_query_kypherv_sim_search_no_nn_index_error(self):
        # Kypher-V manual example - fail because we don't have an NN index built yet:
        query = """kgtk query -o {OUTPUT} --graph-cache {DB}
                        -i {INPUT} --idx vector: mode:valuegraph
                        --match '`embed.tsv`: (x:Q913)-[]->(xv),
                                              (xv)-[r:kvec_topk_cos_sim {{k: 10}}]->(y),
                                 `labels.tsv`: (x)-[]->(xl),
                                               (y)-[]->(yl)'
                        --return 'x as x, xl as xlabel, y as y, yl as ylabel, substr(r.similarity, 1, 8) as sim'
                        --limit 5
                """
        # we list labels first, so the --idx spec applies to the last embed input:
        inputs = ' '.join([self.embed_labels_path, self.embed_path])
        self.assertRaises(Exception, self.run_test_query, query, inputs)

    def test_kgtk_query_kypherv_sim_search_with_nn_index(self):
        # Kypher-V manual example:
        query = """kgtk query -o {OUTPUT} --graph-cache {DB}
                        -i {INPUT} --idx vector:node2/nn/nlist=8 mode:valuegraph
                        --match '`embed.tsv`: (x:Q913)-[]->(xv),
                                              (xv)-[r:kvec_topk_cos_sim {{k: 10}}]->(y),
                                 `labels.tsv`: (x)-[]->(xl),
                                               (y)-[]->(yl)'
                        --return 'x as x, xl as xlabel, y as y, yl as ylabel, substr(r.similarity, 1, 8) as sim'
                        --limit 5
                """
        result = [
            """x\txlabel\ty\tylabel\tsim""",
            """Q913\t'Socrates'@en\tQ913\t'Socrates'@en\t1.0""",
            """Q913\t'Socrates'@en\tQ179149\t'Antisthenes'@en\t0.824994""",
            """Q913\t'Socrates'@en\tQ409647\t'Aeschines of Sphettus'@en\t0.814151""",
            """Q913\t'Socrates'@en\tQ666230\t'Aristobulus of Paneas'@en\t0.801446""",
            """Q913\t'Socrates'@en\tQ380190\t'Phaedo of Elis'@en\t0.785770"""
        ]
        # we list labels first, so the --idx spec applies to the last embed input:
        inputs = ' '.join([self.embed_labels_path, self.embed_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)
        
    def test_kgtk_query_kypherv_sim_search_with_cutoff_and_vector_export(self):
        # Kypher-V manual example:
        query = """kgtk query -o {OUTPUT} --graph-cache {DB}
                        -i {INPUT} --idx vector:node2/nn/nlist=8 mode:valuegraph
                        --match '`embed.tsv`: (x:Q913)-[]->(xv),
                                              (xv)-[r:kvec_topk_cos_sim {{nprobe: 8}}]->(y),
                                `labels.tsv`: (x)-[]->(xl),
                                              (y)-[]->(yl)'
                        --where  'x != y and r.similarity >= 0.8'
                       --return 'x as x, xl as xlabel, y as y, yl as ylabel, substr(r.similarity, 1, 8) as sim, r.vid as yvid, 
                                 kgtk_stringify(substr(kvec_to_base64(r.vector), 2, 20)) as yv'
                """
        result = [
            '''x\txlabel\ty\tylabel\tsim\tyvid\tyv''',
            '''Q913\t'Socrates'@en\tQ179149\t'Antisthenes'@en\t0.824994\te-ea594b00\t"LDeCPTLTJ79I0HK+si3t"''',
            '''Q913\t'Socrates'@en\tQ409647\t'Aeschines of Sphettus'@en\t0.814151\te-0685ee35\t"5lOZvNnqEb85jqe+S5Qv"''',
            '''Q913\t'Socrates'@en\tQ666230\t'Aristobulus of Paneas'@en\t0.801446\te-2906ba9a\t"Ex++vHClDL9nnLW+qXvT"'''
        ]
        # we list labels first, so the --idx spec applies to the last embed input:
        inputs = ' '.join([self.embed_labels_path, self.embed_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)
        
    def test_kgtk_query_kypherv_sim_search_vector_join_bad(self):
        # Kypher-V manual example:
        query = """kgtk query -o {OUTPUT} --graph-cache {DB}
                        -i {INPUT} --idx vector:node2/nn/nlist=8 mode:valuegraph
                        --match '`embed.tsv`: (x)-[]->(xv),
                                              (xv)-[r:kvec_topk_cos_sim {{k: 5}}]->(y),
                                 `claims.tsv`: (y)-[:P31]->(:Q5),
                                               (y)-[:P106]->(:Q36180),
                                 `labels.tsv`: (x)-[]->(xl),
                                               (y)-[]->(yl)'
                        --where  'x in ["Q859", "Q868", "Q913"]'
                        --return 'x as x, xl as xlabel, y as y, yl as ylabel, substr(r.similarity, 1, 8) as sim'
                """
        result = [
            """x\txlabel\ty\tylabel\tsim""",
            """Q859\t'Plato'@en\tQ41155\t'Heraclitus'@en\t0.747522""",
            """Q859\t'Plato'@en\tQ83375\t'Empedocles'@en\t0.742346""",
            """Q868\t'Aristotle'@en\tQ868\t'Aristotle'@en\t1.0""",
            """Q868\t'Aristotle'@en\tQ10261\t'Pythagoras'@en\t0.769469""",
            """Q868\t'Aristotle'@en\tQ5264\t'Hippocrates'@en\t0.755326"""
        ]
        # we list labels first, so the --idx spec applies to the last embed input:
        inputs = ' '.join([self.embed_labels_path, self.embed_claims_path, self.embed_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)
        
    def test_kgtk_query_kypherv_sim_search_vector_join_good(self):
        # Kypher-V manual example:
        query = """kgtk query -o {OUTPUT} --graph-cache {DB}
                        -i {INPUT} --idx vector:node2/nn/nlist=8 mode:valuegraph
                        --match '`embed.tsv`: (x)-[]->(xv),
                                              (xv)-[r:kvec_topk_cos_sim {{k: 5, maxk: 100}}]->(y),
                                 `claims.tsv`: (y)-[:P31]->(:Q5),
                                               (y)-[:P106]->(:Q36180),
                                 `labels.tsv`: (x)-[]->(xl),
                                               (y)-[]->(yl)'
                        --where  'x in ["Q859", "Q868", "Q913"]'
                        --return 'x as x, xl as xlabel, y as y, yl as ylabel, substr(r.similarity, 1, 8) as sim'
                """
        result = [
            """x\txlabel\ty\tylabel\tsim""",
            """Q859\t'Plato'@en\tQ41155\t'Heraclitus'@en\t0.747522""",
            """Q859\t'Plato'@en\tQ83375\t'Empedocles'@en\t0.742346""",
            """Q859\t'Plato'@en\tQ5264\t'Hippocrates'@en\t0.727953""",
            """Q859\t'Plato'@en\tQ868\t'Aristotle'@en\t0.733143""",
            """Q859\t'Plato'@en\tQ1430\t'Marcus Aurelius'@en\t0.703216""",
            """Q868\t'Aristotle'@en\tQ868\t'Aristotle'@en\t1.0""",
            """Q868\t'Aristotle'@en\tQ10261\t'Pythagoras'@en\t0.769469""",
            """Q868\t'Aristotle'@en\tQ5264\t'Hippocrates'@en\t0.755326""",
            """Q868\t'Aristotle'@en\tQ41155\t'Heraclitus'@en\t0.739228""",
            """Q868\t'Aristotle'@en\tQ271809\t'Proclus'@en\t0.725646""",
            """Q913\t'Socrates'@en\tQ271809\t'Proclus'@en\t0.765996""",
            """Q913\t'Socrates'@en\tQ5264\t'Hippocrates'@en\t0.767316""",
            """Q913\t'Socrates'@en\tQ1430\t'Marcus Aurelius'@en\t0.759520""",
            """Q913\t'Socrates'@en\tQ10261\t'Pythagoras'@en\t0.751109""",
            """Q913\t'Socrates'@en\tQ83375\t'Empedocles'@en\t0.744120"""
        ]
        # we list labels first, so the --idx spec applies to the last embed input:
        inputs = ' '.join([self.embed_labels_path, self.embed_claims_path, self.embed_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)
        
    def test_kgtk_query_kypherv_sim_search_vector_join_unbalanced(self):
        # Kypher-V manual example:
        query = """kgtk query -o {OUTPUT} --graph-cache {DB}
                        -i {INPUT} --idx vector:node2/nn/nlist=8 mode:valuegraph
                        --match '`embed.tsv`: (x)-[]->(xv),
                                              (xv)-[r:kvec_topk_cos_sim {{k: 50}}]->(y),
                                  `claims.tsv`: (y)-[:P31]->(:Q5),
                                                (y)-[:P106]->(:Q36180),
                                  `labels.tsv`: (x)-[]->(xl),
                                                (y)-[]->(yl)'
                        --where  'x in ["Q859", "Q868", "Q913"]'
                        --return 'x as x, xl as xlabel, y as y, yl as ylabel, substr(r.similarity, 1, 8) as sim'
                        --limit 15
                """
        result = [
            """x\txlabel\ty\tylabel\tsim""",
            """Q859\t'Plato'@en\tQ41155\t'Heraclitus'@en\t0.747522""",
            """Q859\t'Plato'@en\tQ83375\t'Empedocles'@en\t0.742346""",
            """Q859\t'Plato'@en\tQ868\t'Aristotle'@en\t0.733143""",
            """Q859\t'Plato'@en\tQ5264\t'Hippocrates'@en\t0.727953""",
            """Q859\t'Plato'@en\tQ1430\t'Marcus Aurelius'@en\t0.703216""",
            """Q859\t'Plato'@en\tQ10261\t'Pythagoras'@en\t0.696925""",
            """Q859\t'Plato'@en\tQ125551\t'Parmenides'@en\t0.693956""",
            """Q859\t'Plato'@en\tQ47154\t'Lucretius'@en\t0.693444""",
            """Q859\t'Plato'@en\tQ271809\t'Proclus'@en\t0.688394""",
            """Q859\t'Plato'@en\tQ59138\t'Diogenes Laërtius'@en\t0.680530""",
            """Q859\t'Plato'@en\tQ313924\t'Nicolaus of Damascus'@en\t0.677434""",
            """Q859\t'Plato'@en\tQ175042\t'Nigidius Figulus'@en\t0.649016""",
            """Q859\t'Plato'@en\tQ561367\t'Lucius Aelius Stilo Praeconinus'@en\t0.646487""",
            """Q868\t'Aristotle'@en\tQ868\t'Aristotle'@en\t1.0""",
            """Q868\t'Aristotle'@en\tQ10261\t'Pythagoras'@en\t0.769469"""
        ]
        # we list labels first, so the --idx spec applies to the last embed input:
        inputs = ' '.join([self.embed_labels_path, self.embed_claims_path, self.embed_path])
        qdf = self.run_test_query(query, input=inputs)
        self.assert_test_query_result(qdf, result)
