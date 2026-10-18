# Python Log Analyzer

A command-line tool written in Python to analyze log files and review
messages by severity level.

This project was created to practice Python programming, Linux,
Git, GitHub, and DevOps automation.

## Features

- Read log files from the command line.
- Count INFO, WARNING, and ERROR messages.
- Display a summary of the analyzed file.
- Select a severity level to review matching log entries.
- Handle missing files and file access errors.
- Use exit codes to indicate execution failures.

## Requirements

- Python 3.10 or later.
- Git.
- A terminal (Linux, macOS, or Windows).

No external Python packages are currently required.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/jfs97dev-sudo/python-log-analyzer.git
cd python-log-analyzer
```

### 2. Create a virtual environment

Linux and macOS:

```bash
python3 -m venv .venv
```

Windows:

```powershell
py -m venv .venv
```

### 3. Activate the virtual environment

Linux and macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

### 4. Verify Python

```bash
python --version
```

No additional dependencies need to be installed.

## Usage

Run the analyzer by providing the path to a log file:

```bash
python log_analyzer.py sample_logs.txt
```

You can also analyze the larger example:

```bash
python log_analyzer.py logs_random.txt
```

The program displays a summary and asks which severity level you want
to review.

Available options:

1. INFO
2. WARNING
3. ERROR
4. Exit without displaying logs

### Analyze another file

You can provide the path to any readable text log file:

```bash
python log_analyzer.py /path/to/application.log
```

Replace `/path/to/application.log` with the actual path to your file.

## Example Output

For `sample_logs.txt`, the expected summary is:

```text
========== LOG SUMMARY ==========

Total lines: 6
INFO: 3
WARNING: 1
ERROR: 2
```

## Project Structure

```text
python-log-analyzer/
├── log_analyzer.py
├── sample_logs.txt
├── logs_random.txt
├── README.md
└── .gitignore
```

## Current Limitations

- Severity levels are detected using simple text matching.
- Each execution allows the user to review one severity level.

## Future Improvements

- Add automated tests with pytest.
- Improve severity detection.
- Add command-line options for filtering logs.
- Generate reports that can be saved to a file.

## Author

GitHub: [jfs97dev-sudo](https://github.com/jfs97dev-sudo)

