# Python Log Analyzer

A command-line tool written in Python to analyze log files and review
messages by severity level.

## Features

- Read log files from the command line.
- Count INFO, WARNING, and ERROR messages.
- Display a summary of the analyzed file.
- Select a severity level to review matching log entries.
- Handle missing files and file access errors.
- Use exit codes to indicate execution failures.

## Requirements

- Python 3.14 or compatible Python 3 version.

## Usage

Run the analyzer by providing the path to a log file:


python log_analyzer.py sample_logs.txt
