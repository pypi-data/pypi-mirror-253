import shutil
import unittest
import tempfile
import pandas as pd
from kgtk_wukunhuan.cli_entry import cli_entry
from kgtk_wukunhuan.exceptions import KGTKException

from graph_tool.all import * # type: ignore

class TestExportGT(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir=tempfile.mkdtemp()

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)

    def test_export_gt(self):
        cli_entry("kgtk", "export-gt", "-i", "data/sample_kgtk_edge_file.tsv", "--directed", "--log", f'{self.temp_dir}/log.txt', "-o", f'{self.temp_dir}/graph.gt')

        

        g=load_graph(f'{self.temp_dir}/graph.gt')

        self.assertEqual(g.num_edges(), 287)
        self.assertEqual(g.num_vertices(), 287)

