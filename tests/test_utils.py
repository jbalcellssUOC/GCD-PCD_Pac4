"""
GCD-2024_PAC4 Utils Tests
"""

import os
import tempfile
import unittest
import pandas as pd
import HtmlTestRunner
from orbea_monegros.utils import load_dataset


class TestUtils(unittest.TestCase):
    """
    Test suite for the load_dataset function.
    """

    def create_test_file(self,
                         directory: str,
                         filename: str,
                         content: str) -> str:
        """
        Helper function to create a test file in a given directory.

        Args:
            directory (str): The directory where the file will be created.
            filename (str): The name of the file to create.
            content (str): The content to write to the file.

        Returns:
            str: The full path to the created file.
        """
        file_path = os.path.join(directory, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return file_path

    def test_load_dataset_success(self):
        """
        Test loading a valid dataset with the correct delimiter.
        """
        with tempfile.TemporaryDirectory() as tmp_dir:
            test_data = """dorsal;biker;club;time
4515;Christopher Bauer;Independiente;00:00:00
2017;Mary White;Independiente;00:00:00
"""
            test_file = self.create_test_file(tmp_dir,
                                              "valid_dataset.csv",
                                              test_data)
            df = load_dataset(test_file, delimiter=";")

            # Assertions
            self.assertEqual(len(df), 2, "The dataset should contain 2 rows.")
            self.assertListEqual(
                df.columns.tolist(),
                ["dorsal", "biker", "club", "time"],
                "The columns do not match the expected values.",
            )

    def test_load_dataset_invalid_delimiter(self):
        """
        Test loading a valid dataset with an incorrect delimiter.
        """
        with tempfile.TemporaryDirectory() as tmp_dir:
            test_data = """dorsal;biker;club;time
4515;Christopher Bauer;Independiente;00:00:00
2017;Mary White;Independiente;00:00:00
"""
            test_file = self.create_test_file(tmp_dir,
                                              "invalid_delimiter.csv",
                                              test_data)

            with self.assertRaises(ValueError):
                load_dataset(test_file, delimiter=",")

    def test_load_dataset_file_not_found(self):
        """
        Test loading a dataset from a nonexistent file.
        """
        with self.assertRaises(FileNotFoundError):
            load_dataset("nonexistent_file.csv", delimiter=";")

    def test_load_dataset_empty_file(self):
        """
        Test loading an empty dataset.
        """
        with tempfile.TemporaryDirectory() as tmp_dir:
            test_file = self.create_test_file(tmp_dir,
                                              "empty_dataset.csv",
                                              "")

            with self.assertRaises(pd.errors.EmptyDataError):
                load_dataset(test_file, delimiter=";")

    def test_load_dataset_malformed_file(self):
        """
        Test loading a dataset with malformed content.
        """
        with tempfile.TemporaryDirectory() as tmp_dir:
            test_data = """dorsal,biker,club
4515,Christopher Bauer
2017,Mary White,Independiente,ExtraColumn
"""
            test_file = self.create_test_file(tmp_dir,
                                              "malformed_dataset.csv",
                                              test_data)

            with self.assertRaises(pd.errors.ParserError):
                load_dataset(test_file, delimiter=",")


if __name__ == "__main__":
    REPORT_DIR = os.path.abspath("./coverage")
    os.makedirs(REPORT_DIR, exist_ok=True)

    runner = HtmlTestRunner.HTMLTestRunner(
        output=REPORT_DIR,
        report_name="LoadDatasetTests",
        report_title="Test Report for Load Dataset"
    )
    unittest.main(testRunner=runner)
