
# Project Activity Report

## Part A - Corah Price

### 1. Activities Done
   - **Research and Planning**: Conducted background research on secure coding practices and identified potential vulnerabilities in Python applications.
   - **Implementation of Pre-Commit Hook**: Developed a `pre-commit` Git hook to automate security checks using the `bandit` tool, ensuring that all Python files are scanned for vulnerabilities before being committed.
   - **Testing**: Tested the hook on various Python files to validate its effectiveness in identifying security weaknesses. Adjusted configurations based on initial results.
   - **Created README File**: Created a README file that outlines project activities, setup instructions, and example usage to ensure that all team members can easily understand and utilize the project.

### 2. Lessons Learned
   - **Importance of Automation**: Automating security checks significantly reduced the likelihood of introducing vulnerabilities into the codebase. It highlighted the value of integrating security practices into the development workflow.
   - **Tool Limitations**: Encountered limitations with the `bandit` tool, such as false positives. This experience emphasized the need for manual review processes in conjunction with automated tools to ensure a comprehensive security strategy.

---

## Part B - Corah Price

### 1. Activities Done
   - **Created `fuzz.py` Script**: Developed a Python script (`fuzz.py`) that automatically fuzzes 5 Python methods to identify any bugs or unexpected behavior. The methods included were `int()`, `list.append()`, `open()`, `json.loads()`, and `str.replace()`.
   - **Method Selection**: Carefully chose methods that cover a variety of Python functionality, including type conversions, file operations, string manipulations, and JSON parsing. This choice ensures a broad test of the codebase.

### 2. Lessons Learned
   - **Bug Discovery and Reporting**: The fuzzing script successfully discovered bugs and unexpected behaviors, which were immediately recorded in a structured format (`fuzz_report.log`). This enabled quick identification of areas that required attention and fixes.
   - **Handling Complex Bugs**: Some of the issues discovered during fuzzing were difficult to reproduce consistently, especially those that involved certain edge cases. Future fuzzing scripts could benefit from more advanced techniques, such as pattern matching or heuristics, to pinpoint the exact cause of inconsistencies.
   - **Expanding Method Coverage**: While five methods were a good starting point, there is potential to expand fuzzing to more complex methods or entire code modules. Fuzzing more methods would help ensure broader code coverage and identify additional edge cases.

---

## Part C - Ayush Singh

### 1. Activities Done
   - **Enhanced fuzz.py for Fuzz Testing**: Modified the existing fuzz.py script to test five additional Python functionalities:-
   String splitting `(split)`
   String stripping `(strip)`
   Integer conversion `(int)`
   List sorting `(sorted)`
   Dictionary key retrieval `(dict.get)`
   - Implemented detailed logging to `fuzz_forensics.log`, capturing timestamps, method names, inputs, outputs, and exceptions.
   - Created `fuzz_report.log` to track and analyze bugs discovered during fuzz testing.

### 2. Lessons Learned
   - **Importance of Detailed Logging**: Comprehensive logs were invaluable in identifying and reproducing issues.
   - **Testing Edge Cases**: Realized the significance of robust test cases for detecting unexpected behaviors.
   
---

## Part D - Ayush Singh

### 1. Activities Done
   - **Integrated Codacy Analysis CLI with GitHub Actions**: Added a GitHub Actions workflow to automate code quality checks using Codacy. Configured the workflow to run on every push, ensuring consistent analysis of the codebase.
   - Created .github/workflows/codacy-analysis.yaml to define the CI pipeline.
   - Configured the pipeline to checkout the code and run Codacy Analysis CLI.

### 2. Lessons Learned
   - **CI Benefits**: Automating code quality checks reduces manual effort and ensures adherence to coding standards.
   - **Tool Usage**: Gained experience in configuring and using Codacy and GitHub Actions for continuous integration.
