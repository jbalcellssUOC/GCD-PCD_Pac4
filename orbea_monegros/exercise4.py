"""
Exercise 4 Module
This module contains the implementation of Exercise 4 for GCD-2024 PAC4.
"""

import re
import pandas as pd


def clean_club(club: str) -> str:

    """
    Cleans cycling club name according to patterns.

    Args:
        club (str): Club name.

    Returns:
        str: Cleaned club name.
    """

    if not isinstance(club, str):
        return "INDEPENDIENTE"

    # 1 Step, convert names to uppercase
    club = club.upper()

    # 2 step, replace some pattern values with nothing
    replace_values = [
        'PEÑA CICLISTA', 'PENYA CICLISTA', 'AGRUPACIÓN CICLISTA',
        'AGRUPACION CICLISTA', 'AGRUPACIÓ CICLISTA',
        'AGRUPACIO CICLISTA', 'CLUB CICLISTA', 'CLUB'
    ]
    for value in replace_values:
        club = club.replace(value, '')

    # Replace patterns at the beginning
    replace_start_patterns = [
        r'^C\.C\.\s*', r'^C\.C\s*', r'^CC\s*', r'^C\.D\.\s*', r'^C\.D\s*',
        r'^CD\s*', r'^A\.C\.\s*', r'^A\.C\s*', r'^AC\s*', r'^A\.D\.\s*',
        r'^A\.D\s*', r'^AD\s*', r'^A\.E\.\s*', r'^A\.E\s*', r'^AE\s*',
        r'^AD\\.\\s*', r'^AD\.\s*', r'^AD\s*',
        r'^E\.C\.\s*', r'^E\.C\s*', r'^EC\s*', r'^S\.C\.\s*', r'^S\.C\s*',
        r'^SC\s*', r'^S\.D\.\s*', r'^S\.D\s*', r'^SD\s*'
    ]
    for pattern in replace_start_patterns:
        club = re.sub(pattern, '', club)

    # Replace patterns at the end of the string
    replace_end_patterns = [
        r'\bT\.T\.\b', r'\bT\.T\b', r'\bTT\b', r'\bT\.E\.\b', r'\bT\.E\b',
        r'\bTE\b', r'\bC\.C\.\b', r'\bC\.C\b', r'\bCC\b', r'\bC\.D\.\b',
        r'\bC\.D\b', r'\bCD\b', r'\bA\.D\.\b', r'\bA\.D\b', r'\bAD\b',
        r'\bA\.D\.\b', r'\bA\.D\b',
        r'\bA\.C\.\b', r'\bA\.C\b', r'\bAC\b'
    ]
    for pattern in replace_end_patterns:
        club = re.sub(pattern, '', club)

    # Additional - clean dot's
    club = re.sub(r'^\.\s*', '', club)
    club = re.sub(r'\.\s*$', '', club)

    # Strip whitespace from the beginning and end of strings
    club = club.strip()
    return club if club else "INDEPENDIENTE"


def exercise4(df: pd.DataFrame, print_results: bool) -> pd.DataFrame:

    """
    Cleans club names and creates a new grouped DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.
        print_results (bool): Whether to print results or not.

    Returns:
        pd.DataFrame: DataFrame grouped by cleaned club names.
    """
    try:
        df = df.copy()

        # Clean club names
        df['club_clean'] = df['club'].apply(clean_club)

        if print_results:
            # Print the first 15 rows of the updated DataFrame
            print("\nFirst 15 rows of the DataFrame with cleaned clubs:\n")
            with pd.option_context('display.max_colwidth', None):
                print(df.head(15), "\n")

        # Group by club_clean names and count participants
        grouped_df = df.groupby(
            'club_clean').size().reset_index(
                name='participant_count')

        # Sort by participant count (descending order)
        grouped_df = grouped_df.sort_values(
            by='participant_count',
            ascending=False)

        if print_results:
            print("\nGrouped DataFrame with participant counts:\n")
            print(grouped_df, "\n")

        return df

    except Exception as e:
        print(f"Ex4, an unexpected error occurred: {e}")
        raise
