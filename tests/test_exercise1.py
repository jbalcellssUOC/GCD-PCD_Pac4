"""
GCD-2024_PAC4 Exercise1 Tests
"""

import unittest
import os
import tempfile

from orbea_monegros.exercise1 import exercise1


class TestExercise1(unittest.TestCase):
    """
    Test suite for the exercise1 function.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up a temporary directory and dataset file before running tests.
        """
        cls.tmp_dir = tempfile.TemporaryDirectory()
        cls.test_file = os.path.join(cls.tmp_dir.name, "test_dataset.csv")

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
        # Save the dataset as a CSV file
        with open(cls.test_file, "w", encoding="utf-8") as f:
            f.write(test_data)

    @classmethod
    def tearDownClass(cls):
        """
        Remove the temporary directory after running tests.
        """
        cls.tmp_dir.cleanup()

    def test_exercise1(self):
        """
        Test the exercise1 function with the temporary dataset.
        """
        # Call the function
        result = exercise1(self.test_file)

        # Assertions
        self.assertEqual(
            result["num_cyclists"], 9, "The number of cyclists should be 9"
        )
        self.assertListEqual(
            result["columns"],
            ["dorsal", "biker", "club", "time"],
            "The columns do not match the expected values",
        )
        self.assertEqual(
            len(result["head"]), 5, "The head should contain the first 5 rows"
        )


if __name__ == "__main__":
    unittest.main()
