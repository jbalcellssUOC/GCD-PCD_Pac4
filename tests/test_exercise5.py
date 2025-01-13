"""
GCD-2024_PAC4 Exercise5 Tests
"""

import unittest
import pandas as pd
from unittest.mock import patch
import io

from orbea_monegros.exercise5 import exercise5


class TestExercise5(unittest.TestCase):
    """
    Test suite for the exercise5 function.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up test data for Exercise5.
        """
        cls.synthetic_data = pd.DataFrame({
            "dorsal": [1, 2, 3, 4, 5],
            "biker": [
                "Rider1", "Rider2", "Rider3", "Rider4", "Rider5"
            ],
            "club_clean": [
                "UCSC", "UCSC", "ClubA", "ClubB", "UCSC"
            ],
            "time": [
                "01:10:00", "01:20:00", "02:30:00", "02:40:00", "00:50:00"
            ]
        })

    def test_exercise5_best_cyclist(self):
        """
        Test identification of the best UCSC cyclist.
        """
        # Mock print_results=False
        exercise5(self.synthetic_data, print_results=False)

        # Filter UCSC cyclists
        ucsc_cyclists = self.synthetic_data[
            self.synthetic_data['club_clean'] == 'UCSC'].copy()

        # Add time_in_seconds for sorting
        ucsc_cyclists['time_in_seconds'] = ucsc_cyclists['time'].apply(
            lambda x: sum(int(t) * 60 ** i for i, t in enumerate(
                reversed(x.split(':'))))
        )

        # Identify best cyclist
        best_cyclist = ucsc_cyclists.loc[
            ucsc_cyclists['time_in_seconds'].idxmin()]

        self.assertEqual(
            best_cyclist['time'], "00:50:00",
            "The best UCSC cyclist was not identified correctly."
        )
        self.assertEqual(
            best_cyclist['dorsal'], 5,
            "The dorsal number of the best UCSC cyclist is incorrect."
        )

    def test_exercise5_position_and_percentage(self):
        """
        Test calculation of position and percentage for the
        best UCSC cyclist.
        """
        df = self.synthetic_data.copy()
        df['time_in_seconds'] = df['time'].apply(
            lambda x: sum(int(t) * 60 ** i for i, t in enumerate(
                reversed(x.split(':'))))
        )
        df_sorted = df.sort_values(
            by='time_in_seconds').reset_index(
                drop=True)

        # Identify best UCSC cyclist
        ucsc_cyclists = df[df['club_clean'] == 'UCSC'].copy()
        ucsc_cyclists['time_in_seconds'] = ucsc_cyclists['time'].apply(
            lambda x: sum(int(t) * 60 ** i for i, t in enumerate(
                reversed(x.split(':'))))
        )
        best_cyclist = ucsc_cyclists.loc[
            ucsc_cyclists['time_in_seconds'].idxmin()]
        best_cyclist_position = df_sorted[
            df_sorted['time_in_seconds'] == best_cyclist['time_in_seconds']
        ].index[0] + 1

        total_cyclists = len(df_sorted)
        percentage = (best_cyclist_position / total_cyclists) * 100

        self.assertEqual(
            best_cyclist_position, 1,
            "The position of the best UCSC cyclist is incorrect."
        )
        self.assertAlmostEqual(
            percentage, 20.0,
            places=2,
            msg="The percentage of the best UCSC cyclist is incorrect."
        )

    def test_empty_dataframe(self):
        """
        Test exercise5 with an empty DataFrame.
        """
        empty_df = pd.DataFrame(columns=["dorsal", "biker", "club_clean",
                                         "time"])
        with self.assertRaises(Exception,
                               msg="The function should raise an error for " +
                               "empty DataFrame."):
            exercise5(empty_df, print_results=False)

    def test_exercise5_prints(self):
        """
        Test the print outputs of exercise5 when print_results=True.
        """
        test_data = {
            "dorsal": [1, 2, 3],
            "biker": ["Cyclist A", "Cyclist B", "Cyclist C"],
            "club_clean": ["UCSC", "UCSC", "OTHER"],
            "time": ["01:30:00", "01:20:00", "02:00:00"]
        }
        df = pd.DataFrame(test_data)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            exercise5(df, print_results=True)
            output = mock_stdout.getvalue()
            self.assertIn("Cyclists from UCSC club:", output)
            self.assertIn("Best cyclist in UCSC club:", output)
            self.assertIn("Position of the best UCSC cyclist:", output)
            self.assertIn("Percentage over the total:", output)


if __name__ == "__main__":
    unittest.main()
