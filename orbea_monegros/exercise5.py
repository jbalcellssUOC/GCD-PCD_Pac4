"""
Exercise 5 Module
This module contains the implementation of Exercise 5 for GCD-2024 PAC4.
"""

import pandas as pd


def exercise5(df: pd.DataFrame, print_results: bool) -> None:

    """
    Analyzes the UCSC club data to answer specific questions.

    Args:
        df (pd.DataFrame): Input cleaned club DataFrame.
        print_results (bool): Whether to print results or not.

    Returns:
        dict: A dictionary with the results for the analysis.
    """

    try:
        df = df.copy()  # Copy Dataframe

        # Filter UCSC cyclists
        ucsc_cyclists = df[df['club_clean'] == 'UCSC']

        # Identify UCSC cyclist with the best time
        ucsc_cyclists = ucsc_cyclists.copy()
        ucsc_cyclists.loc[:,
                          'time_in_seconds'] = ucsc_cyclists[
                              'time'].apply(
                                  lambda x: sum(
                                      int(t) * 60 ** i for i,
                                      t in enumerate(
                                          reversed(
                                              x.split(':')))))

        best_cyclist = ucsc_cyclists.loc[
            ucsc_cyclists['time_in_seconds'].idxmin()]

        # Calculate position and percentage
        df['time_in_seconds'] = df['time'].apply(
            lambda x:
                sum(int(t) * 60 ** i for i,
                    t in enumerate(reversed(
                        x.split(':'))))
        )
        df_sorted = df.sort_values(
            by='time_in_seconds').reset_index(
                drop=True)
        best_cyclist_position = df_sorted[
            df_sorted['time_in_seconds'] == best_cyclist[
                'time_in_seconds']].index[0] + 1
        total_cyclists = len(df_sorted)
        percentage = (best_cyclist_position / total_cyclists) * 100

        if print_results:
            print("\nCyclists from UCSC club:\n")
            print(ucsc_cyclists)

            print("\nBest cyclist in UCSC club:\n")
            print(best_cyclist)

            print("\nPosition of the best UCSC cyclist: " +
                  f"{best_cyclist_position}")
            print(f"Percentage over the total: {percentage:.2f}%\n")

        return None

    except Exception as e:
        print(f"Ex5, an unexpected error occurred: {e}")
        raise
