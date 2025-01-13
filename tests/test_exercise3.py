"""
GCD-2024_PAC4 Exercise3 Tests
"""

import unittest
from unittest.mock import patch
import os
import io
import pandas as pd
from orbea_monegros.exercise1 import exercise1
from orbea_monegros.exercise2 import exercise2
from orbea_monegros.exercise3 import exercise3, minutes_002040


class TestExercise3(unittest.TestCase):
    """
    Test suite for the exercise3 function.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test dataset for synthetic data and load real data
        if available.
        """
        cls.synthetic_data = pd.DataFrame({
            "dorsal": [101, 102, 103, 104, 105],
            "biker": ["Rider1", "Rider2", "Rider3", "Rider4", "Rider5"],
            "club": ["ClubA", "ClubB", "ClubA", "ClubC", "ClubB"],
            "time": ["00:10:15", "00:30:45", "01:50:30", "02:15:10",
                     "00:59:50"]
        })
        cls.real_data_path = os.path.join("data", "dataset.csv")
        if os.path.exists(cls.real_data_path):
            cls.real_data_loaded = True
        else:
            cls.real_data_loaded = False

    def test_minutes_002040(self):
        """
        Test the minutes_002040 function for grouping time correctly.
        """
        self.assertEqual(minutes_002040("00:10:15"), "00:00",
                         "Time grouping is incorrect for 10 minutes.")
        self.assertEqual(minutes_002040("00:30:45"), "00:20",
                         "Time grouping is incorrect for 30 minutes.")
        self.assertEqual(minutes_002040("00:50:00"), "00:40",
                         "Time grouping is incorrect for 50 minutes.")
        self.assertEqual(minutes_002040("01:00:00"), "01:00",
                         "Time grouping is incorrect for exact hour.")

    @patch("orbea_monegros.exercise3.plt.show")
    @patch("orbea_monegros.exercise3.plt.savefig")
    def test_exercise3_synthetic(self, mock_savefig, mock_show):
        # pylint: disable=unused-argument
        """
        Test the main exercise3 function with synthetic data.
        """
        df_grouped = exercise3(self.synthetic_data, print_results=False)

        # Verify the DataFrame output structure
        self.assertListEqual(
            list(df_grouped.columns),
            ["time_grouped", "cyclist_count"],
            ("Output DataFrame should have columns 'time_grouped' and "
             "'cyclist_count'.")
        )

        # Verify the grouped DataFrame contents
        expected_grouped_data = pd.DataFrame({
            "time_grouped": ["00:00", "00:20", "00:40", "01:40", "02:00"],
            "cyclist_count": [1, 1, 1, 1, 1]
        })
        pd.testing.assert_frame_equal(
            df_grouped.reset_index(drop=True),
            expected_grouped_data,
            "The grouped DataFrame contents do not match expected results."
        )

        # Verify that matplotlib savefig was called twice
        self.assertEqual(mock_savefig.call_count, 2,
                         "Expected two calls to savefig (one for each plot).")

    def test_empty_dataframe(self):
        """
        Test the behavior of exercise3 with an empty DataFrame.
        """
        empty_df = pd.DataFrame(columns=["dorsal", "biker", "club", "time"])
        grouped_df = exercise3(empty_df, print_results=False)
        self.assertTrue(grouped_df.empty,
                        "Output should be an empty DataFrame when input is "
                        "empty.")

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_exercise3_prints(self, mock_stdout):
        """
        Test the print outputs of exercise3 when print_results=True.
        """
        exercise3(self.synthetic_data, print_results=True)

        output = mock_stdout.getvalue()
        self.assertIn("First 15 rows of the grouped times DataFrame:",
                      output,
                      "The output does not contain the expected print " +
                      "statements.")
        self.assertIn("Grouped DataFrame:", output,
                      "The output does not contain the expected grouped " +
                      "DataFrame print.")

    def test_exercise3_generic_exception(self):
        """
        Test exercise3 for handling generic exceptions.
        """
        with self.assertRaises(Exception):
            exercise3(None, print_results=False)

    @unittest.skipUnless(os.path.exists("data/dataset.csv"),
                         "Real data file is missing.")
    def test_exercise3_real_data(self):
        """
        Test exercise3 with real data from data/dataset.csv,
        using exercise1 and exercise2 for preparation.
        """
        # Run Exercise 1 to load the dataset
        df = exercise1(self.real_data_path, print_results=False)

        # Run Exercise 2 to anonymize and clean the dataset
        df_cleaned = exercise2(df, print_results=False)

        # Run Exercise 3 to group the data by time
        df_grouped = exercise3(df_cleaned, print_results=False)

        # Verify that the DataFrame is grouped correctly
        self.assertListEqual(
            list(df_grouped.columns),
            ["time_grouped", "cyclist_count"],
            ("The grouped DataFrame should have columns 'time_grouped' and "
             "'cyclist_count'.")
        )

        # Verify that the DataFrame contains data
        self.assertGreater(len(df_grouped), 0,
                           "The grouped DataFrame should not be empty.")

        print("\nTest with real data executed successfully.\n")


if __name__ == "__main__":
    unittest.main()
