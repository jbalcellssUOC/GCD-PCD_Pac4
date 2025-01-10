"""
GCD-2024_PAC4 excercises code
"""

# Library imports
import pandas as pd
from orbea_monegros.utils import load_dataset


def sample_func():
    """
    GCD-2024_PACsss4 excercises code
    """
    print("Test")  # Sin snake_case ni docstring


def exercise1(dataset_path: str) -> None:
    """
    Performs the following operations:

        1. Imports the dataset into a DataFrame.
        2. Displays the first 5 rows of the DataFrame.
        3. Indicates how many cyclists participated in the event.
        4. Shows the columns of the DataFrame.

    Returns:
        None
    """
    try:
        # Import the dataset into a DataFrame without any
        # special option or argument
        df: pd.DataFrame = load_dataset(dataset_path, delimiter=";")

        # Show First 5 rows
        print("\nFirst 5 rows of the dataset:\n")
        print(df.head())

        # Show total of cyclists who participated
        num_ciclistas: int = len(df)
        print(f"\nCyclists who participated in the event: {num_ciclistas}")

        # Show all DataFrame columns
        columnas: list[str] = df.columns.tolist()
        print(f"\nColumns of the DataFrame: {columnas}")
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"An unexpected error occurred: {e}")
        raise


if __name__ == "__main__":
    exercise1("")
