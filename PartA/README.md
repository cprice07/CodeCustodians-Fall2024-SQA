The `pre-commit` hook in this project serves as an automated code security checker. It performs the following tasks:
1. Detects any staged Python files during a commit.
2. Runs security scans on these files using `bandit`.
3. Outputs any security issues found into a `bandit_report.csv` file.
4. Blocks commits if security vulnerabilities are detected, prompting developers to review and resolve issues before committing.

## Example Usage

### Commit Blocking Example
<img width="542" alt="Screenshot 2024-10-31 at 12 20 59 PM" src="https://github.com/user-attachments/assets/482e3744-d242-44fb-a7c1-9dc74d5fb4d0">


### Bandit Report Example
<img width="1527" alt="Screenshot 2024-10-31 at 12 22 15 PM" src="https://github.com/user-attachments/assets/a9b78e49-32b3-4fe7-86a2-400a820e8dbc">
