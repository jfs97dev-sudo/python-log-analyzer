import pytest

from log_analyzer import analyze_logs


def test_analyze_logs_counts_severity_levels(tmp_path, monkeypatch, capsys):
    """Check that log entries are counted correctly."""
    log_file = tmp_path / "application.log"
    log_file.write_text(
        "INFO Application started\n"
        "WARNING High memory usage\n"
        "ERROR Database connection failed\n"
        "INFO Application recovered\n",
        encoding="utf-8",
    )

    monkeypatch.setattr("builtins.input", lambda _: "4")

    analyze_logs(str(log_file))
    output = capsys.readouterr().out

    assert "Total lines: 4" in output
    assert "INFO: 2" in output
    assert "WARNING: 1" in output
    assert "ERROR: 1" in output


def test_analyze_logs_with_empty_file(tmp_path, monkeypatch, capsys):
    """Check that an empty file produces zero counts."""
    log_file = tmp_path / "empty.log"
    log_file.write_text("", encoding="utf-8")

    monkeypatch.setattr("builtins.input", lambda _: "4")

    analyze_logs(str(log_file))
    output = capsys.readouterr().out

    assert "Total lines: 0" in output
    assert "INFO: 0" in output
    assert "WARNING: 0" in output
    assert "ERROR: 0" in output


@pytest.mark.parametrize(
    ("option", "severity", "expected_message"),
    [
        ("1", "INFO", "Application started"),
        ("2", "WARNING", "High memory usage"),
        ("3", "ERROR", "Database connection failed"),
    ],
)
def test_analyze_logs_displays_selected_severity(
    tmp_path, monkeypatch, capsys, option, severity, expected_message
):
    """Check that the selected severity is displayed."""
    log_file = tmp_path / "application.log"
    log_file.write_text(
        "INFO Application started\n"
        "WARNING High memory usage\n"
        "ERROR Database connection failed\n",
        encoding="utf-8",
    )

    monkeypatch.setattr("builtins.input", lambda _: option)

    analyze_logs(str(log_file))
    output = capsys.readouterr().out

    assert f"{severity} LOGS" in output
    assert expected_message in output
    assert "Total log entries displayed: 1" in output


def test_analyze_logs_with_no_matching_severity(tmp_path, monkeypatch, capsys):
    """Check the output when the selected severity has no entries."""
    log_file = tmp_path / "application.log"
    log_file.write_text(
        "INFO Application started\n",
        encoding="utf-8",
    )

    monkeypatch.setattr("builtins.input", lambda _: "3")

    analyze_logs(str(log_file))
    output = capsys.readouterr().out

    assert "No ERROR logs found." in output
    assert "Total log entries displayed: 0" in output


def test_analyze_logs_invalid_menu_option(tmp_path, monkeypatch, capsys):
    """Check that invalid menu selections are rejected."""
    log_file = tmp_path / "application.log"
    log_file.write_text(
        "INFO Application started\n",
        encoding="utf-8",
    )

    monkeypatch.setattr("builtins.input", lambda _: "9")

    analyze_logs(str(log_file))
    output = capsys.readouterr().out

    assert "ERROR: Invalid option." in output


def test_analyze_logs_exit_option(tmp_path, monkeypatch, capsys):
    """Check that option 4 exits without displaying individual logs."""
    log_file = tmp_path / "application.log"
    log_file.write_text(
        "ERROR Database connection failed\n",
        encoding="utf-8",
    )

    monkeypatch.setattr("builtins.input", lambda _: "4")

    analyze_logs(str(log_file))
    output = capsys.readouterr().out

    assert "Analysis completed." in output
    assert "ERROR LOGS" not in output


def test_analyze_logs_with_large_file(tmp_path, monkeypatch, capsys):
    """Check that a file containing 10000 entries is analyzed correctly."""
    log_file = tmp_path / "large.log"

    lines = []
    for i in range(10000):
        if i % 3 == 0:
            lines.append(f"INFO Event {i}")
        elif i % 3 == 1:
            lines.append(f"WARNING Event {i}")
        else:
            lines.append(f"ERROR Event {i}")

    log_file.write_text("\n".join(lines) + "\n", encoding="utf-8")

    monkeypatch.setattr("builtins.input", lambda _: "4")

    analyze_logs(str(log_file))
    output = capsys.readouterr().out

    assert "Total lines: 10000" in output
    assert "INFO: 3334" in output
    assert "WARNING: 3333" in output
    assert "ERROR: 3333" in output


def test_analyze_logs_with_missing_file(tmp_path):
    """Check that opening a nonexistent file raises FileNotFoundError."""
    log_file = tmp_path / "does_not_exist.log"

    with pytest.raises(FileNotFoundError):
        analyze_logs(str(log_file))
