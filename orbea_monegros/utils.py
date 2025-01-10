"""
GCD-2024_PAC4 utils and helpers
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
        Exception: General error ocurred
    """
    try:
        return pd.read_csv(file_path, delimiter=delimiter)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty or invalid.")
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"An unexpected error occurred: {e}")
        raise
