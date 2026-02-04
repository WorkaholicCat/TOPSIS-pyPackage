# TOPSIS-pyPackage
Topsis-Py (Python CLI Package)

A command-line based Python implementation of the TOPSIS method
(Technique for Order Preference by Similarity to Ideal Solution)
used for solving Multi-Criteria Decision Making (MCDM) problems.

This package focuses on correct theoretical implementation,
simple CLI usage, and readiness for academic and PyPI deployment.

| Aspect         | Details                                  |
| -------------- | ---------------------------------------- |
| Methodology    | Classical TOPSIS algorithm               |
| Access Mode    | Command Line Interface                   |
| Input Format   | CSV decision matrix                      |
| Error Handling | Strong validation for inputs & arguments |
| Output         | Ranked alternatives with TOPSIS scores   |
| Documentation  | Explained theory and process flow        |

## Understanding TOPSIS
TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)
is a popular approach in Multi-Criteria Decision Making (MCDM).

## Fundamental Principle
An optimal alternative is one that:
-Has the minimum distance from the ideal best solution
-Has the maximum distance from the ideal worst solution

### Installation Guide
Install directly from PyPI using:
pip install Topsis-Aartha-102302941

### How to use
python topsis.py <input_csv> <weights> <impacts> <output_csv>

## Constraints & Assumptions

-Only numerical data is supported
-No missing or null values allowed
-All weights must be positive numbers
-Impacts must be specified as + or -
-----------------------------------------

### License Information
This project is distributed under the MIT License.
