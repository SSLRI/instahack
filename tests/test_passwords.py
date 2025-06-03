import os
import sys

# Ensure the project root is on sys.path for importing main
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from main import load_passwords


def test_load_passwords_creates_default(tmp_path):
    file_path = tmp_path / "custom_pw.txt"
    assert not file_path.exists()
    passwords = load_passwords(str(file_path))
    assert file_path.exists()
    assert passwords == ["123456", "password", "qwerty", "letmein", "admin"]
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    assert lines == passwords
