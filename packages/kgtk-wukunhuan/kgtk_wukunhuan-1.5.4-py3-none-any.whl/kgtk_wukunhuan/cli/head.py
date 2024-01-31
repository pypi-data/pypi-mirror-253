"""This utility is analogous to the POSIX 'head' command.

When "-n N" is positive, it will pass just the first N data edges of a KGTK
input file to the KGTK output file.

When "-n N" is negative, it will pass all except the last N edges of the KGTK
input file to the KGTK output file.

The header record, cotaining the column names, is always passed and is not
included in N.

Multiplier suffixes are not supported.

Although positive "-n N" has the same effect as KgtkReader's '--record-limit N'
option, this code currently implements the limit itself.

--mode=NONE is default.

TODO: Need KgtkWriterOptions

"""

from argparse import Namespace, SUPPRESS

from kgtk_wukunhuan.cli_argparse import KGTKArgumentParser, KGTKFiles


def parser():
    return {
        'help': 'Pass the head (first records) of a KGTK file.',
        'description': 'This utility is analogous to the POSIX "head" command. ' +
                       '\n\nWhen "-n N" is positive, it will pass just the first N data edges of a KGTK input file to the KGTK output file. ' +
                       '\n\nWhen "-n N" is negative, it will pass all except the last N edges of the KGTK input file to the KGTK output file. ' +
                       '\n\nThe header record, cotaining the column names, is always passed and is not included in N. ' +
                       '\n\nMultiplier suffixes are not supported. ' +
                       '\n\nUse this command to filter the output of any KGTK command: ' +
                       '\n\nkgtk xxx / head -n 20 ' +
                       '\n\nUse it to limit the records in a file: ' +
                       '\n\nkgtk head -i file.tsv -o file.html' +
                       '\n\nThis command defaults to --mode=NONE so it will work with TSV files that do not follow KGTK column naming conventions.' +
                       '\n\nAdditional options are shown in expert help.\nkgtk --expert head --help'
    }


def add_arguments_extended(parser: KGTKArgumentParser, parsed_shared_args: Namespace):
    """
    Parse arguments
    Args:
        parser (argparse.ArgumentParser)
    """
    from kgtk_wukunhuan.io.kgtkreader import KgtkReader, KgtkReaderOptions, KgtkReaderMode
    from kgtk_wukunhuan.io.kgtkwriter import KgtkWriter
    from kgtk_wukunhuan.value.kgtkvalueoptions import KgtkValueOptions

    _expert: bool = parsed_shared_args._expert

    # This helper function makes it easy to suppress options from
    # The help message.  The options are still there, and initialize
    # what they need to initialize.
    def h(msg: str) -> str:
        if _expert:
            return msg
        else:
            return SUPPRESS

    parser.add_input_file()
    parser.add_output_file()

    parser.add_argument("-n", "--edges", dest="edge_limit", type=int, default=10,
                        help="The number of records to pass if positive (default=%(default)d).")

    parser.add_argument("--output-format", dest="output_format", help=h("The file format (default=kgtk)"), type=str,
                        choices=KgtkWriter.OUTPUT_FORMAT_CHOICES)

    KgtkReader.add_debug_arguments(parser, expert=_expert)
    KgtkReaderOptions.add_arguments(parser,
                                    mode_options=True,
                                    default_mode=KgtkReaderMode.NONE,
                                    expert=_expert)
    KgtkValueOptions.add_arguments(parser, expert=_expert)


def run(input_file: KGTKFiles,
        output_file: KGTKFiles,

        edge_limit: int,
        output_format: str,

        errors_to_stdout: bool = False,
        errors_to_stderr: bool = True,
        show_options: bool = False,
        verbose: bool = False,
        very_verbose: bool = False,

        **kwargs  # Whatever KgtkFileOptions and KgtkValueOptions want.
        ) -> int:
    # import modules locally
    from pathlib import Path
    import sys
    import typing

    from kgtk_wukunhuan.exceptions import KGTKException
    from kgtk_wukunhuan.io.kgtkreader import KgtkReaderOptions, KgtkReaderMode
    from kgtk_wukunhuan.value.kgtkvalueoptions import KgtkValueOptions
    from kgtk_wukunhuan.utils.head import Head
    try:
        input_file_path: Path = KGTKArgumentParser.get_input_file(input_file)
        output_file_path: Path = KGTKArgumentParser.get_output_file(output_file)

        # Select where to send error messages, defaulting to stderr.
        error_file: typing.TextIO = sys.stdout if errors_to_stdout else sys.stderr

        # TODO: check that at most one input file is stdin?

        # Build the option structures.
        reader_options: KgtkReaderOptions = KgtkReaderOptions.from_dict(kwargs, mode=KgtkReaderMode.NONE)
        value_options: KgtkValueOptions = KgtkValueOptions.from_dict(kwargs)

        head = Head(input_kgtk_file=input_file_path,
                    output_kgtk_file=output_file_path,
                    edge_limit=edge_limit,
                    output_format=output_format,
                    reader_options=reader_options,
                    value_options=value_options,
                    error_file=error_file,
                    show_options=show_options,
                    verbose=verbose,
                    very_verbose=very_verbose)
        head.process()
        return 0

    except SystemExit as e:
        raise KGTKException("Exit requested")
    except Exception as e:
        raise KGTKException(str(e))
