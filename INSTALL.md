# Installation of the Orbea Monegros PAC4 Package

This document outlines the steps required to install and configure the **Orbea Monegros PAC4** package in your development or production environment.

---

## Prerequisites

Ensure you meet the following prerequisites before proceeding:

1. **Python 3.10 or higher** installed. Verify your version with:
   ```bash
   python --version
   ```

2. **pip** (Python's package manager) installed. Verify it with:
   ```bash
   pip --version
   ```

3. Optionally, install **virtualenv** to create a virtual environment:
   ```bash
   pip install virtualenv
   ```

4. Access to the project repository on GitHub:
   [https://github.com/jbalcellssUOC/GCD-PCD_Pac4.git](https://github.com/jbalcellssUOC/GCD-PCD_Pac4.git)

---

## Installation

### 1. Clone the repository

First, clone the project repository from GitHub:

```bash
git clone https://github.com/jbalcellssUOC/GCD-PCD_Pac4.git
cd GCD-PCD_Pac4
```

### 2. Create a virtual environment (recommended)

To avoid dependency conflicts, it is recommended to use a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```
- On Windows:
  ```bash
  .\venv\Scripts\activate
  ```

### 3. Install dependencies

Once inside the virtual environment, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Install the package in editable mode

To work with the package in development, install it in editable mode:

```bash
pip install -e .
```

---

## Running Tests

To ensure everything is working correctly, run the included tests:

```bash
pytest tests/
```

---

## Using the Package

After installation, you can use the package from any script or directly from the command line:

### Import in a script:

```python
from orbea_monegros import main
main()
```

### Terminal Command:

If an executable script was defined in `setup.py`, run:

```bash
orbea-analysis
```

---

## Uninstallation

To uninstall the package, simply run:

```bash
pip uninstall orbea-monegros
```

If you also want to remove the virtual environment, simply delete the `venv/` folder:

```bash
rm -rf venv  # On macOS/Linux
del venv     # On Windows
```

---

That's it! You are now ready to use and develop with the **Orbea Monegros PAC4** package.