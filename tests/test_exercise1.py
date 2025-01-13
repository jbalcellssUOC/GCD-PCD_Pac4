"""
GCD-2024_PAC4 Exercise1 Tests
"""

import tempfile
import unittest
import os
import pandas as pd

from orbea_monegros.exercise1 import exercise1


class TestExercise1(unittest.TestCase):
    """
    Test suite for the exercise1 function.
    """

    def test_exercise1(self):
        """
        Test the exercise1 function with a temporary dataset.
        """
        test_data = """dorsal;biker;club;time
4515;Christopher Bauer;Independiente;00:00:00
2017;Mary White;Independiente;00:00:00
116;Melissa Olson;Independiente;00:00:00
1469;Joshua Klein;Independiente;00:00:00
4536;Maurice Castro;Independiente;00:00:00
1810;Michael Baker;EL BICHO ;00:00:00
1247;Chad Chase;Independiente;00:00:00
4625;Jonathan Caldwell;Independiente;00:00:00
91;Roberto Powell;Independiente;00:00:00
"""

        # Use 'with' to manage TemporaryDirectory
        with tempfile.TemporaryDirectory() as tmp_dir:
            test_file = os.path.join(tmp_dir, "test_dataset.csv")

            # Save the dataset as a CSV file
            with open(test_file, "w", encoding="utf-8") as f:
                f.write(test_data)

            # Call the function
            df = exercise1(test_file, print_results=False)

            # Assertions
            self.assertIsInstance(df, pd.DataFrame, "The result should be " +
                                  "a DataFrame")
            self.assertEqual(len(df), 9, "The number of rows (cyclists) " +
                             "should be 9")
            self.assertListEqual(
                list(df.columns),
                ["dorsal", "biker", "club", "time"],
                "The columns do not match the expected values",
            )
            self.assertEqual(
                len(df.head()), 5, "The head of the DataFrame should " +
                "contain 5 rows"
            )


if __name__ == "__main__":
    unittest.main()
