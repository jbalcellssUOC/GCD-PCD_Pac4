"""
Exercise 1 Module
This module contains the implementation of Exercise 1 for GCD-2024 PAC4.
"""

# Library imports
import pandas as pd
from orbea_monegros.utils import load_dataset


def exercise1(dataset_path: str,
              print_results: bool) -> pd.DataFrame:

    """
    Executes the operations for Exercise 1:
        1. Imports the dataset into a DataFrame.
        2. Displays the first 5 rows of the DataFrame.
        3. Indicates how many cyclists participated in the event.
        4. Shows the columns of the DataFrame.

    Args:
        dataset_path (str): Path to the dataset file.
        print_results (bool): If true print results

    Returns:
        pd.Dataframe: Loaded Dataframe
    """

    try:
        # Step 1: Import the dataset into a DataFrame
        df: pd.DataFrame = load_dataset(dataset_path, delimiter=";")

        if print_results:
            # Step 2: Show First 5 rows
            print("\nFirst 5 rows of the dataset:\n")
            print(df.head())
            # Step 3: Show total cyclists who participated
            print(f"\nCyclists who participated in the event: {len(df)}")
            # Step 4: Show Dataframe columns
            print(f"Columns of the DataFrame: {df.columns.tolist()}\n")

        return df

    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"Ex1, an unexpected error occurred: {e}")
        raise
