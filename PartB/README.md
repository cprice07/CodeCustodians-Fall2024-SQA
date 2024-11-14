# Fuzzing with `fuzz.py`

The `fuzz.py` script automatically fuzzes 5 Python methods of your choice to identify any bugs, crashes, or unexpected behavior.

## How it works:
1. **Fuzzes 5 Python methods** randomly by generating various inputs.
2. **Reports any discovered bugs** or unexpected behavior during the fuzzing process.
3. The results of the fuzz testing, including any issues found, will be logged into a `fuzz_report.csv` file for review.

## Methods Being Fuzzed:
1. **`int()`**  
   Converts strings to integers. Fuzzing tests how it handles invalid inputs like non-numeric strings, empty strings, or special characters.

2. **`list.append()`**  
   Appends to a list. This test includes appending a `None` value, appending a list to another list, or appending large objects.

3. **`open()`**  
   Opens a file. Tests edge cases such as invalid file paths, non-existent files, and incorrect file modes.

4. **`json.loads()`**  
   Parses JSON strings. This test checks how the method handles malformed JSON, such as missing quotes or extra commas.

5. **`str.replace()`**  
   Replaces substrings in a string. Fuzzing includes replacing substrings that don’t exist or using unusual data types.

## Results:
Any bugs or unexpected behavior discovered will be logged into a `fuzz_report.csv` file for easy tracking

<img width="1501" alt="Screenshot 2024-11-14 at 10 54 35 AM" src="https://github.com/user-attachments/assets/7f7e4b2f-dbcf-401a-8046-47e8935b0198">

