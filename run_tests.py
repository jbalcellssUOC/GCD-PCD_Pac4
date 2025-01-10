"""
GCD-2024_PAC4 Test Runner with HTML Report

This script discovers and executes all test cases defined
in the "tests" directory
and generates an HTML report using HtmlTestRunner.

Features:
- Automatically discovers all test files matching the pattern "test_*.py".
- Generates a structured HTML report in the "tests_reports" directory.
- Ensures the report directory is created if it does not exist.

How to Use:
- Place your test files in the "tests" directory with filenames
starting with "test_".
- Run this script to execute the tests and generate the report.
"""

import unittest
import os
import HtmlTestRunner

# Main function to execute the test suite
if __name__ == "__main__":
    # Define the test directory and report output directory
    TEST_DIR = "./tests"
    REPORT_DIR = "./tests_reports"

    # Ensure the report directory exists
    os.makedirs(REPORT_DIR, exist_ok=True)

    # Discover all test cases in the specified directory
    suite = unittest.TestLoader().discover(
        start_dir=TEST_DIR,
        pattern="test_*.py"
    )

    # Configure HtmlTestRunner for generating the HTML report
    runner = HtmlTestRunner.HTMLTestRunner(
        output=REPORT_DIR,
        report_name="PAC4_Tests_Reports",
        report_title="GCD-2024 PAC4 Test Suite Report",
        verbosity=2,
    )

    # Run the discovered test suite
    runner.run(suite)
