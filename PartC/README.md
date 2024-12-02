# Integrate forensics by modifying 5 Python methods of choice in `fuzz.py`

The `fuzz.py` script automatically fuzzes 5 Python methods to identify any bugs, crashes, or unexpected behavior.

## Purpose of the Code:
The code performs fuzz testing on five Python methods or functionalities:
1. **String splitting (split).
2. **String stripping (strip).
3. **Integer conversion (int).
4. **List sorting (sorted).
5. **Dictionary key retrieval (dict.get).

The program logs each test's details (timestamp, test ID, method name, inputs, output, or exceptions) into `fuzz_forensics.log` for analysis.

## Methods Being Fuzzed:d
1. **`fuzz_split`**  
Tests `str.split()` with random strings and separators (e.g., space, comma, or None). Handles normal output and logs exceptions.

2. **`fuzz_strip`**  
Tests `str.strip()` with random strings and characters (e.g., whitespace or None). Logs both results and exceptions.

3. **`fuzz_int`**  
Tests `int()` with random strings, valid and invalid for conversion to integers. Logs exceptions for invalid inputs.

4. **`fuzz_list_sort`**  
Tests sorting on mixed-type lists. Logs `TypeError` for incompatible comparisons between types (e.g., string vs. integer).

5. **`fuzz_dict_get`**  
Tests dictionary `get()` with random dictionaries and keys, logging output or errors.

## Results:
Any bugs or unexpected behavior discovered will be logged into a `fuzz_report.log` file for easy tracking.

<img width="1500" alt="Screenshot 2024-11-14 at 10 54 35 AM" src="https://github.com/user-attachments/assets/e7c7f141-a66e-4b4a-b9ce-c001b7e76478">

<img width="auto" alt="Screenshot 2024-11-14 at 10 54 35 AM" src="https://github.com/user-attachments/assets/6101faa2-879f-49d9-9c52-b429d97ee967">