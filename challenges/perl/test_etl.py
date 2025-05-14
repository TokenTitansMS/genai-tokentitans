import unittest
import os
from etl import etl_process, TABLE_NAME

schema_file = "mysqlCreateSchemaPyTest.sql"
values_file = "mysqlInsertValuesPyTest.sql"

class TestETLProcess(unittest.TestCase):
    def setUp(self):
        """Set up a mock CSV file for testing."""
        self.test_csv = "test_prices.csv"
        with open(self.test_csv, "w") as csvfile:
            csvfile.write("ticker,date,open,high,low,close,vol\n")
            csvfile.write("AAC,20110112,9.73,9.73,9.73,9.73,200\n")
            csvfile.write("AACC,20110112,6.29,6.51,6.21,6.4,16400\n")
            csvfile.write("AACOU,20110112,9.9,9.98,9.9,9.98,1300\n")
            csvfile.write("AACOW,20110112,0.35,0.35,0.35,0.35,700\n")

    def tearDown(self):
        """Clean up the generated files."""
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)
        if os.path.exists(schema_file):
            os.remove(schema_file)
        if os.path.exists(values_file):
            os.remove(values_file)

    def test_schema_file_generation(self):
        """Test if the schema file is generated correctly."""
        etl_process(self.test_csv, schema_file, values_file)

        # Check if the schema file exists
        self.assertTrue(os.path.exists(schema_file))

        # Validate the contents of the schema file
        with open(schema_file, "r") as schema:
            content = schema.read()
            self.assertIn(f"CREATE TABLE `{TABLE_NAME}`", content)
            self.assertIn("`ticker` varchar", content)
            self.assertIn("`date` int", content)
            self.assertIn("`open` decimal", content)
            self.assertIn("ENGINE=InnoDB DEFAULT CHARSET=latin1", content)

    def test_values_file_generation(self):
        """Test if the values file is generated correctly."""
        etl_process(self.test_csv, schema_file, values_file)

        # Check if the values file exists
        self.assertTrue(os.path.exists(values_file))

        # Validate the contents of the values file
        with open(values_file, "r") as values:
            content = values.read()
            self.assertIn("INSERT INTO nasdaq_prices", content)
            self.assertIn("VALUES ('AAC', '20110112', '9.73', '9.73', '9.73', '9.73', '200');", content)
            self.assertIn("INSERT INTO nasdaq_prices", content)
            self.assertIn("VALUES ('AACC', '20110112', '6.29', '6.51', '6.21', '6.4', '16400');", content)
            

if __name__ == "__main__":
    unittest.main()