"""
GCD-2024_PAC4 utils and helpers.

This module provides reusable utility functions to be used across the
application. These functions aim to reduce redundancy and improve code
maintainability by centralizing common operations into a single location.

Utility modules like this one are essential for adhering to the DRY
(Don't Repeat Yourself) principle. By consolidating frequently used
logic here, we can ensure that updates or bug fixes are applied
consistently wherever these utilities are utilized. This promotes cleaner,
more modular, and maintainable code throughout the application.
"""

import pandas as pd


def load_dataset(file_path: str, delimiter: str = ",") -> pd.DataFrame:
    """
    Load a dataset from a file into Pandas DataFrame.

    Args:
        file_path (str): The path to the file.
        delimiter (str): Delimiter used in the file. Defaults to ','.

    Returns:
        pd.DataFrame: Loaded dataset as a Pandas DataFrame.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty or invalid.
        ValueError: Malformed data in dataset.
        Exception: General error occurred.
    """
    try:
        # Use 'with' to open the file safely
        with open(file_path, "r", encoding="utf-8") as file:
            df = pd.read_csv(file, delimiter=delimiter)

        # Validate the delimiter by checking column count
        if df.empty or len(df.columns) < 2:
            raise ValueError(
                f"Invalid delimiter '{delimiter}' used for file '{file_path}'."
            )

        return df

    except FileNotFoundError as e:
        print(f"Error: The file '{file_path}' was not found.")
        raise e
    except pd.errors.EmptyDataError as e:
        print(f"Error: The file '{file_path}' is empty or invalid.")
        raise e
    except ValueError as e:
        print(f"Error: {e}")
        raise e
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise
