import unittest
import os
import pandas as pd
from src.parser import BDEWParser

class TestBDEWParser(unittest.TestCase):

    def setUp(self):
        # Sets up paths relative to this test file
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.xml_path = os.path.join(self.base_dir, 'data', 'sample_redispatch.xml')
        self.xsd_path = os.path.join(self.base_dir, 'data', 'schema.xsd')
        self.parser = BDEWParser(self.xsd_path)

    def test_schema_exists(self):
        self.assertIsNotNone(self.parser._xsd_schema)

    def test_validation_success(self):
        is_valid = self.parser.validate(self.xml_path)
        self.assertTrue(is_valid)

    def test_parsing_structure(self):
        df = self.parser.parse_to_dataframe(self.xml_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)

        expected_cols = ['ResourceID', 'Start', 'End', 'Capacity_MW', 'Status']
        for col in expected_cols:
            self.assertIn(col, df.columns)

    def test_data_accuracy(self):
        df = self.parser.parse_to_dataframe(self.xml_path)
        # Check the first row capacity (450.5 MW)
        self.assertEqual(df.iloc[0]['Capacity_MW'], 450.5)

if __name__ == '__main__':
    unittest.main()