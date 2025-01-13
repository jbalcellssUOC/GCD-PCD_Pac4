"""
GCD-2024_PAC4 Exercise2 Tests
"""

import unittest
import pandas as pd

from orbea_monegros.exercise2 import exercise2


class TestExercise2(unittest.TestCase):
    """
    Test suite for the exercise2 function.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up a temporary directory and dataset file before running tests.
        """
        cls.test_data = pd.DataFrame({
            "dorsal": [4515, 2017, 1000, 1469, 4536, 1810],
            "biker": [
                "Christopher Bauer", "Mary White", "Anonymized Biker",
                "Joshua Klein", "Maurice Castro", "Michael Baker"
            ],
            "club": [
                "Independiente", "Independiente", "Independiente",
                "Independiente", "Independiente", "EL BICHO"
            ],
            "time": ["00:00:00", "01:20:15", "00:00:00",
                     "02:15:30", "00:00:00", "01:05:00"]
        })

    def test_exercise2_anonymization(self):
        """
        Test that the 'biker' column is anonymized in the output DataFrame.
        """
        df_processed = exercise2(self.test_data, print_results=False)
        anonymized_bikers = df_processed['biker'].tolist()
        for name in anonymized_bikers:
            # Check if names are valid Faker-generated names (not from input)
            self.assertNotIn(name, self.test_data['biker'].tolist(),
                             "Biker names should be anonymized.")

    def test_exercise2_remove_zero_time(self):
        """
        Test that rows with '00:00:00' in the 'time' column are removed.
        """
        df_processed = exercise2(self.test_data, print_results=False)
        self.assertFalse(
            (df_processed['time'] == "00:00:00").any(),
            "Rows with '00:00:00' time should be removed."
        )

    def test_exercise2_cyclist_1000(self):
        """
        Test that cyclist with dorsal=1000 is included in the processing.
        """
        df_processed = exercise2(self.test_data, print_results=False)
        cyclist_1000 = df_processed[df_processed['dorsal'] == 1000]
        self.assertTrue(
            cyclist_1000.empty,
            "Cyclist with dorsal=1000 should be excluded if their " +
            "time is '00:00:00'."
        )

    def test_exercise2_output_structure(self):
        """
        Test that the structure of the output DataFrame remains unchanged.
        """
        df_processed = exercise2(self.test_data, print_results=False)
        self.assertListEqual(
            list(df_processed.columns),
            ["dorsal", "biker", "club", "time"],
            "Output DataFrame should have the same columns as the input."
        )
        self.assertGreaterEqual(
            len(self.test_data), len(df_processed),
            "The number of rows in the processed DataFrame should be " +
            "less or equal to the input."
        )


if __name__ == "__main__":
    unittest.main()
