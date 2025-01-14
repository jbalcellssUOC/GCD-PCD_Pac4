# Contributing to the Orbea Monegros PAC4 Python Package

Thank you for your interest in contributing to the Orbea Monegros PAC4 project! Your help is essential for improving and growing this package. Follow this guide to contribute effectively.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Repository Structure](#repository-structure)
3. [Contribution Guidelines](#contribution-guidelines)
4. [Reporting Issues](#reporting-issues)
5. [Submitting Changes (Pull Requests)](#submitting-changes-pull-requests)
6. [Code Style](#code-style)
7. [Contact](#contact)

---

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jbalcellssUOC/GCD-PCD_Pac4.git
   cd GCD-PCD_Pac4
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   .\venv\Scripts\activate    # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run tests to ensure everything works:**
   ```bash
   pytest tests/
   ```

---

## Repository Structure

- `orbea_monegros/`: Contains the main package code.
- `tests/`: Includes unit tests.
- `data/`: Dataset files required for analysis.
- `README.md`: General project documentation.
- `setup.py`: File for packaging and distributing the project.
- `CONTRIBUTING.md`: Guide for contributing to the project.
- `requirements.txt`: Project dependencies.

---

## Contribution Guidelines

1. **Be respectful**: This is a collaborative space. Be kind and patient with other contributors.
2. **Create a branch for your contribution**:
   ```bash
   git checkout -b feature/new-feature
   ```
3. **Write tests for any new functionality**.
4. **Provide clear documentation**: Add or update documentation if you introduce significant changes.

---

## Reporting Issues

If you encounter an issue or have a suggestion, please create an [issue on GitHub](https://github.com/jbalcellssUOC/GCD-PCD_Pac4/issues) with:

- A detailed description of the issue or suggestion.
- Steps to reproduce the issue (if applicable).
- Screenshots or code examples (if relevant).

---

## Submitting Changes (Pull Requests)

1. **Ensure your branch is up-to-date**:
   ```bash
   git pull origin main
   ```

2. **Commit your changes with clear messages**:
   ```bash
   git add .
   git commit -m "Clear description of the change made"
   ```

3. **Submit your Pull Request**:
   - Go to the repository page on GitHub.
   - Click "Compare & Pull Request."
   - Provide a detailed description of the changes made.

4. **Await review**: A collaborator will review your PR and provide feedback if needed.

---

## Code Style

- Follow the coding style guidelines from [PEP 8](https://peps.python.org/pep-0008/).
- Use docstrings to document functions and classes.
- Ensure your code passes linting checks:
  ```bash
  flake8 orbea_monegros
  ```

---

## Contact

If you have any questions, feel free to reach out:

- Author: Jordi Balcells Saenz
- Email: [jbalcellss@uoc.edu](mailto:jbalcellss@uoc.edu)
- Repository: [Orbea Monegros PAC4 on GitHub](https://github.com/jbalcellssUOC/GCD-PCD_Pac4.git)

Thank you for contributing! ❤️
