"""
Exercise 1 Module
This module contains the implementation of Exercise 1 for GCD-2024 PAC4.
"""

# Library imports
import pandas as pd
from orbea_monegros.utils import load_dataset


def exercise1(dataset_path: str) -> dict:
    """
    Executes the operations for Exercise 1:
        1. Imports the dataset into a DataFrame.
        2. Displays the first 5 rows of the DataFrame.
        3. Indicates how many cyclists participated in the event.
        4. Shows the columns of the DataFrame.

    Args:
        dataset_path (str): The path to the dataset file.

    Returns:
        dict: A dictionary containing the results of the operations:
            - "head": First 5 rows of the DataFrame as a list of dicts.
            - "num_cyclists": Number of cyclists who participated.
            - "columns": List of column names in the DataFrame.
    """
    try:
        # Import the dataset into a DataFrame
        df: pd.DataFrame = load_dataset(dataset_path, delimiter=";")

        # Show First 5 rows
        print("\nFirst 5 rows of the dataset:\n")
        print(df.head())
        head = df.head().to_dict(orient="records")

        # Show total of cyclists who participated
        num_cyclists: int = len(df)
        print(f"\nCyclists who participated in the event: {num_cyclists}")

        # Show all DataFrame columns
        columns: list[str] = df.columns.tolist()
        print(f"\nColumns of the DataFrame: {columns}")

        # Return results
        return {
            "head": head,
            "num_cyclists": num_cyclists,
            "columns": columns,
        }

    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"An unexpected error occurred: {e}")
        raise
