"""
GCD-2024_PAC4 setup.py
"""

from setuptools import setup, find_packages

setup(
    name="orbea_monegros",
    version="1.0.0",
    description="Paquete Python Orbea Monegros 2024.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Jordi Balcells Saenz",
    author_email="jbalcellss@uoc.edu",
    url="https://github.com/jbalcellssUOC/GCD-PCD_Pac4.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pandas>=1.3.0", "numpy>=1.21.0", "matplotlib>=3.4.0"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    license="MIT",
    keywords="orbea monegros ciclismo análisis datos",
    entry_points={
        "console_scripts": [
            "orbea-analysis=orbea_monegros.main:main",
        ],
    },
)
