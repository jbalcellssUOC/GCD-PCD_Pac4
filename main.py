"""
GCD-2024_PAC4 Main Script

This script organizes and executes the PAC4 exercises.
"""

import argparse
import sys
import pandas as pd

from orbea_monegros.exercise1 import exercise1
from orbea_monegros.exercise2 import exercise2


def run_exercise1(dataset_path: str,
                  print_results: bool = False) -> pd.DataFrame:
    """ Execute exercise1 """

    result: dict = exercise1(dataset_path, print_results)
    return result


def run_exercise2(df: pd.DataFrame,
                  print_results: bool = False) -> pd.DataFrame:
    """ Execute exercise2 """

    result = exercise2(df, print_results)
    return result


class ExerciseRunner:
    """
    Class to manage the execution of exercises and shared state.
    """

    def __init__(self):
        self.dataset = None

    def execute_exercise(self, index, dataset_path, exercises) -> None:

        """
        Executes a specific exercise.

        Parameters:
            index (int): The exercise index to execute.
            dataset_path (str): Path to the dataset file.
            exercises (list): List of exercise functions.

        Returns:
            Any: The result of the executed exercise.
        """

        if index == 1:
            print(f"\n--- Running Exercise {index} ---\n")
            self.dataset = exercises[index](dataset_path, True)
            return self.dataset
        else:
            if index == 2:
                print("\n--- Running Exercise 1 ---")
                self.dataset = exercises[1](dataset_path, False)
                print(f"--- Running Exercise {index} ---\n")
                self.dataset = exercises[index](self.dataset, True)
                return self.dataset

        print(f"\n--- Running Exercise {index} ---\n")
        return exercises[index](self.dataset)


def check_arguments(args, exercises) -> str:
    """
    Validate and process the command-line arguments.

    Parameters:
        args (Namespace): Parsed arguments from argparse.
        exercises (list): List of exercise functions.

    Returns:
        tuple: A tuple containing the dataset path (str)
        and the exercise index or 'all'.

    Raises:
        SystemExit: If arguments are invalid.
    """
    if not args.dataset:
        sys.exit(
            "ERROR: Dataset path is required. Use -d or --dataset to "
            "specify it."
        )

    if args.exercise is not None:
        if args.exercise < 1 or args.exercise >= len(exercises):
            sys.exit(
                f"ERROR: Invalid exercise number. Choose between "
                f"1 and {len(exercises) - 1}."
            )
        return args.dataset, args.exercise

    return args.dataset, "all"


def main():

    """
    Main function to execute the requested exercises based on
    command-line arguments.
    """

    # List of exercise functions
    exercises = [None, run_exercise1, run_exercise2]

    # Argument validation
    parser = argparse.ArgumentParser(description="GCD-2024 PAC4 Runner")
    parser.add_argument(
        "-d",
        "--dataset",
        type=str,
        required=True,
        help="Path to dataset file required for running exercises.",
    )
    parser.add_argument(
        "-e",
        "--exercise",
        type=int,
        help="Specify the exercise number to run (default: run all).",
    )

    # Parse & Validate arguments
    args = parser.parse_args()
    dataset_path, exercise_requested = check_arguments(args, exercises)

    # Create exercises runner instance
    runner = ExerciseRunner()
    if exercise_requested == "all":
        print("\nExecuting all exercises...\n")
        for i in range(1, len(exercises)):
            runner.execute_exercise(i, dataset_path, exercises)
    else:
        runner.execute_exercise(exercise_requested, dataset_path, exercises)


# Set script name
if __name__ == "__main__":
    main()
