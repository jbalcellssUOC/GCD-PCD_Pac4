"""
GCD-2024_PAC4 Exercise4 Tests
"""

import unittest
from unittest.mock import patch
import io
import pandas as pd

from orbea_monegros.exercise4 import exercise4, clean_club


class TestExercise4(unittest.TestCase):
    """
    Test suite for the exercise4 function and clean_club helper.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test datasets.
        """
        cls.synthetic_data = pd.DataFrame({
            "dorsal": [1, 2, 3, 4, 5, 6, 7],
            "biker": [
                "Rider1", "Rider2", "Rider3", "Rider4", "Rider5", "Rider6",
                "Rider7"
            ],
            "club": [
                "C.C. Alfinden", "Independiente", "GEIC Carcalin",
                "C.C. Independiente", "Orbea Sport CLUB", "Garri Bikes",
                "BIZIKLETA.COM"
            ],
            "time": [
                "00:30:00", "01:10:00", "02:20:00", "03:30:00", "04:40:00",
                "05:50:00", "06:00:00"
            ]
        })

    def test_clean_club(self):
        """
        Test the clean_club function with various inputs.
        """
        self.assertEqual(clean_club("C.C. Alfinden"), "ALFINDEN",
                         "C.C. prefix not cleaned correctly.")
        self.assertEqual(clean_club("Independiente"), "INDEPENDIENTE",
                         "Independiente not formatted correctly.")
        self.assertEqual(clean_club("Garri Bikes"), "GARRI BIKES",
                         "Regular club name should not change.")
        self.assertEqual(clean_club("C.C. Independiente"), "INDEPENDIENTE",
                         "C.C. prefix with Independiente not cleaned.")
        self.assertEqual(clean_club(None), "INDEPENDIENTE",
                         "Non-string input not handled correctly.")

    def test_exercise4_output(self):
        """
        Test the exercise4 function for correct processing and
        output structure.
        """
        df_cleaned = exercise4(self.synthetic_data, print_results=False)

        # Verify that 'club_clean' column exists
        self.assertIn("club_clean",
                      df_cleaned.columns,
                      "The 'club_clean' column was not added to the " +
                      "DataFrame.")

        # Verify that cleaned clubs match expected results
        expected_club_clean = [
            "ALFINDEN", "INDEPENDIENTE", "GEIC CARCALIN", "INDEPENDIENTE",
            "ORBEA SPORT", "GARRI BIKES", "BIZIKLETA.COM"
        ]
        self.assertListEqual(df_cleaned["club_clean"].tolist(),
                             expected_club_clean,
                             "Cleaned clubs do not match expected results.")

    def test_exercise4_grouping(self):
        """
        Test the grouping functionality of exercise4.
        """
        df_cleaned = exercise4(self.synthetic_data, print_results=False)
        grouped_df = df_cleaned.groupby("club_clean").size().reset_index(
            name="participant_count").sort_values(
                by="participant_count", ascending=False)

        # Sort both DataFrames for consistent comparison
        grouped_df = grouped_df.sort_values(
            by=["club_clean"]).reset_index(
                drop=True)

        expected_grouped = pd.DataFrame({
            "club_clean": [
                "ALFINDEN", "BIZIKLETA.COM",
                "GARRI BIKES", "GEIC CARCALIN",
                "INDEPENDIENTE", "ORBEA SPORT"
            ],
            "participant_count": [1, 1, 1, 1, 2, 1]
        }).sort_values(by=["club_clean"]).reset_index(drop=True)

        pd.testing.assert_frame_equal(
            grouped_df,
            expected_grouped,
            "Grouped results do not match expected DataFrame."
        )

    def test_empty_dataframe(self):
        """
        Test exercise4 with an empty DataFrame.
        """
        empty_df = pd.DataFrame(columns=["dorsal", "biker", "club", "time"])
        result_df = exercise4(empty_df, print_results=False)
        self.assertTrue(result_df.empty,
                        "Output should be an empty DataFrame.")

    def test_exercise4_prints(self):
        """
        Test the print outputs of exercise4 when print_results=True.
        """
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            exercise4(self.synthetic_data,
                      print_results=True)

            output = mock_stdout.getvalue()

            # Check print outputs
            self.assertIn("First 15 rows of the DataFrame with " +
                          "cleaned clubs:",
                          output)
            self.assertIn("Grouped DataFrame with participant counts:",
                          output)

    def test_exercise4_exception(self):
        """
        Test exception handling in exercise4.
        """
        with self.assertRaises(Exception):
            exercise4(None, print_results=False)


if __name__ == "__main__":
    unittest.main()
