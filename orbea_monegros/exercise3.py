"""
Exercise 3 Module
This module contains the implementation of Exercise 3 for GCD-2024 PAC4.
"""

# from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt


def minutes_002040(time_str: str) -> str:

    """
    Groups time in hh:mm:ss format in 20 minutes groups.

    Args:
        time_str (str): Time in the format hh:mm:ss.

    Returns:
        str: Time grouped (00, 20, or 40).
    """

    # Parsetime
    hours, minutes, _ = map(int, time_str.split(':'))

    # Group minutes into buckets of 20
    if minutes < 20:
        grouped_minutes = "00"
    elif minutes < 40:
        grouped_minutes = "20"
    else:
        grouped_minutes = "40"

    return f"{hours:02}:{grouped_minutes}"  # Return the grouped time


def exercise3(df: pd.DataFrame,
              print_results: bool) -> pd.DataFrame:

    """
    Adds a grouped time column to the DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.
        print_results (bool): Whether to print results or not.

    Returns:
        pd.DataFrame: DataFrame with an additional 'time_grouped' column.
    """

    try:
        df = df.copy()  # Copy Dataframe

        # Apply minutes_002040 function
        df['time_grouped'] = df['time'].apply(minutes_002040)

        # Group by 'time_grouped' and count cyclists
        grouped_df = df.groupby(
            'time_grouped').size().reset_index(name='cyclist_count')

        # Generate, show and save histogram
        plt.figure(figsize=(10, 6))
        plt.bar(grouped_df['time_grouped'],
                grouped_df['cyclist_count'],
                color='skyblue')
        plt.title('Histogram of cyclists by Time Groups')
        plt.xlabel('Time Group')
        plt.ylabel('Number of Cyclists')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # filename = f"img/Histograma_{timestamp}.png"
        filename = "img/histograma.png"
        plt.savefig(filename)

        # Generate, show and save scatter plot
        plt.figure(figsize=(10, 6))
        plt.plot(grouped_df['time_grouped'],
                 grouped_df['cyclist_count'],
                 marker='^',
                 color='blue',
                 linestyle='-',
                 linewidth=1.5)
        plt.title('Scatter Plot with Line of Cyclists by Time Groups')
        plt.xlabel('Time Group')
        plt.ylabel('Number of Cyclists')
        plt.grid(True, linestyle='--', alpha=0.7)
        # scatter_filename = f"img/ScatterPlot_{timestamp}.png"
        scatter_filename = "img/scatterplot.png"
        plt.savefig(scatter_filename)

        if print_results:
            # Print the first 15 rows of the updated DataFrame
            print("\nFirst 15 rows of the grouped times DataFrame:\n")
            print(df.head(15), "\n")

            # Print goruped Dataframe
            print("\nGrouped DataFrame:\n")
            print(grouped_df, "\n")

            # Print historgram information
            print(f"Historgram saved as: {filename}")
            plt.show()

            # Print scatter plot information
            print(f"ScatterPlot saved as: {scatter_filename}\n")
            plt.show()

        return grouped_df

    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"Ex3, an unexpected error occurred: {e}")
        raise
