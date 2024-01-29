# Project Title

## Purpose
This project serves as a tool for error analysis, specifically designed for processing and analyzing data related to a certain system. It includes functions to load data, judge errors, and perform error analysis, with the capability to output results to CSV files.

## Usage
1. **Load Data:**
   - Use the `load_data` function to fetch data from a specified URL based on certain conditions.
   - The function supports different types of data such as program, copy, and trigger information.

2. **Error Analysis:**
   - Utilize the `error_analysis` function to analyze errors in the loaded data.
   - The analysis includes identifying issues in program, copy, and trigger data and categorizing problems based on specific conditions.

3. **CSV Output:**
   - The `error_analysis_to_csv` function allows you to save the error analysis results to CSV files.
   - You can specify a single day or a date range for the analysis.

## Dependencies
- Python 3.x
- pandas
- json
- requests
- datetime
- warnings
- os

## Author
[YUKAI LIAO]


