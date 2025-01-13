"""
Exercise 2 Module
This module contains the implementation of Exercise 2 for GCD-2024 PAC4.
"""


import pandas as pd
from faker import Faker

fake = Faker()  # Initialize Faker instance


def name_surname(df: pd.DataFrame) -> pd.DataFrame:

    """
    Anonymizes the 'biker' column in Dataframe.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with 'biker' column anonymized.
    """

    df = df.copy()
    df['biker'] = df['biker'].apply(
        lambda _: f"{fake.first_name()} {fake.last_name()}")

    return df


def exercise2(df: pd.DataFrame,
              print_results: bool) -> pd.DataFrame:

    """
    Processes the Dataframe to anonymize bikers.

    Args:
        df (pd.DataFrame): Dataframe to process.
        print_results (bool): Whether to print results or not.

    Returns:
        pd.Dataframe: Processed Dataframe
    """

    try:
        # Step 1: Anonymize the 'biker' column
        df_anonymized = name_surname(df)

        # Step 2: Remove cyclists with time '00:00:00'
        df_cleaned = df_anonymized[df_anonymized['time'] != '00:00:00']

        # Step 3: Get data for dorsal = 1000
        cyclist_1000 = df_cleaned[df_cleaned['dorsal'] == 1000]

        if print_results:
            print(f"\nCyclists in anonymized DataFrame: "
                  f"{len(df_anonymized)}\n")
            print("First 5 rows in anonymized DataFrame:\n")
            print(df_anonymized.head())
            print(f"\nCyclists after cleaning: {len(df_cleaned)}\n")
            print("First 5 rows of the cleaned DataFrame:\n")
            print(df_cleaned.head())
            print("\nData for cyclist with dorsal=1000:\n")
            print(cyclist_1000, "\n")

        return df_cleaned   # Return processed Dataframe

    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"Ex2, an unexpected error occurred: {e}")
        raise
