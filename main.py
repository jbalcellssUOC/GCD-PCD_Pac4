"""
GCD-2024_PAC4 Main Script

This script organizes and executes the PAC4 exercises.
"""

import argparse
import sys
import pandas as pd

from orbea_monegros.exercise1 import exercise1
from orbea_monegros.exercise2 import exercise2
from orbea_monegros.exercise3 import exercise3
from orbea_monegros.exercise4 import exercise4
from orbea_monegros.exercise5 import exercise5


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


def run_exercise3(df: pd.DataFrame,
                  print_results: bool = False) -> pd.DataFrame:
    """ Execute exercise3 """

    result = exercise3(df, print_results)
    return result


def run_exercise4(df: pd.DataFrame,
                  print_results: bool = False) -> pd.DataFrame:
    """ Execute exercise4 """

    result = exercise4(df, print_results)
    return result


def run_exercise5(df: pd.DataFrame,
                  print_results: bool = False) -> None:
    """ Execute exercise5 """

    exercise5(df, print_results)
    return None


class ExerciseRunner:
    """
    Class to manage the execution of exercises and shared state.
    """

    def __init__(self):
        self.original_dataset = None
        self.clean_dataset = None
        self.grouped_dataset = None
        self.cleanclub_dataset = None

    def ensure_dependencies(self, index, dataset_path, exercises):

        """
        Ensure the necessary dependencies are loaded for
        the given exercise index.

        Parameters:
            index (int): Exercise index.
            dataset_path (str): Path to the dataset file.
            exercises (list): List of exercise functions.
        """

        if index >= 1 and self.original_dataset is None:
            print("\n--- Running Exercise 1 ---")
            self.original_dataset = exercises[1](dataset_path, False)

        if index >= 2 and self.clean_dataset is None:
            print("\n--- Running Exercise 2 ---")
            self.clean_dataset = exercises[2](self.original_dataset, False)

        if index >= 4 and self.cleanclub_dataset is None:
            print("\n--- Running Exercise 4 ---")
            self.cleanclub_dataset = exercises[4](self.clean_dataset, False)

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

        self.ensure_dependencies(index, dataset_path, exercises)

        if index == 1:
            self.original_dataset = exercises[index](dataset_path, True)
        elif index == 2:
            self.clean_dataset = exercises[index](self.original_dataset, True)
        elif index == 3:
            self.grouped_dataset = exercises[index](self.clean_dataset, True)
        elif index == 4:
            self.cleanclub_dataset = exercises[index](self.clean_dataset, True)
        elif index == 5:
            exercises[index](self.cleanclub_dataset, True)


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
    exercises = [None,
                 run_exercise1,
                 run_exercise2,
                 run_exercise3,
                 run_exercise4,
                 run_exercise5,
                 ]

    # Parse & Validate arguments
    parser = argparse.ArgumentParser(description="GCD-2024 PAC4 Runner")
    parser.add_argument(
        "-d",
        "--dataset",
        type=str,
        required=True,
        help="[Mandatory] Path to dataset file required for " +
        "running exercises.",
    )
    parser.add_argument(
        "-e",
        "--exercise",
        type=int,
        help="[Optional] Specify the exercise number " +
        "to run (default: run all).",
    )
    args = parser.parse_args()
    dataset_path, exercise_requested = check_arguments(args, exercises)

    # Create exercises runner instance
    runner = ExerciseRunner()
    if exercise_requested == "all":
        print("\n... Execute all exercises ...")
        for i in range(1, len(exercises)):
            runner.execute_exercise(i, dataset_path, exercises)
    else:
        runner.execute_exercise(exercise_requested, dataset_path, exercises)


if __name__ == "__main__":
    main()
