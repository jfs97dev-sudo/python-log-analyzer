import sys


def analyze_logs(file_path):
    total_lines = 0
    info_count = 0
    warning_count = 0
    error_count = 0

    # Store log lines by severity level.
    info_logs = []
    warning_logs = []
    error_logs = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            total_lines += 1

            if "INFO" in line:
                info_count += 1
                info_logs.append(line.rstrip())

            elif "WARNING" in line:
                warning_count += 1
                warning_logs.append(line.rstrip())

            elif "ERROR" in line:
                error_count += 1
                error_logs.append(line.rstrip())

    # Display the summary.
    print("\n========== LOG SUMMARY ==========\n")
    print(f"Total lines: {total_lines}")
    print(f"INFO: {info_count}")
    print(f"WARNING: {warning_count}")
    print(f"ERROR: {error_count}")

    # Ask which severity level the user wants to review.
    print("\nWhich logs would you like to review?")
    print("1. INFO")
    print("2. WARNING")
    print("3. ERROR")
    print("4. Exit without displaying logs")

    option = input("\nSelect an option (1-4): ").strip()

    # Select the corresponding log entries.
    if option == "1":
        selected_logs = info_logs
        level = "INFO"

    elif option == "2":
        selected_logs = warning_logs
        level = "WARNING"

    elif option == "3":
        selected_logs = error_logs
        level = "ERROR"

    elif option == "4":
        print("Analysis completed.")
        return

    else:
        print("ERROR: Invalid option.")
        return

    # Display the selected log entries.
    print(f"\n========== {level} LOGS ==========\n")

    if selected_logs:
        for log in selected_logs:
            print(log)
    else:
        print(f"No {level} logs found.")

    print(f"\nTotal log entries displayed: {len(selected_logs)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_analyzer.py <file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        analyze_logs(file_path)

    except FileNotFoundError:
        print(f"ERROR: File '{file_path}' was not found.")
        sys.exit(1)

    except OSError as error:
        print(f"ERROR: Unable to read the file: {error}")
        sys.exit(1)
