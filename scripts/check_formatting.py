from pathlib import Path
import sys


TARGET_GLOBS = [
    "*.html",
    "*.md",
    "*.json",
    "*.xml",
    "*.txt",
    "src/**/*.js",
    "src/**/*.css",
    "services/**/*.html",
    "articles/**/*.html",
    "case-studies/**/*.html",
    "scripts/**/*.py",
]

EXCLUDED_DIRS = {".git", "node_modules"}


def list_target_files():
    files = set()
    for pattern in TARGET_GLOBS:
        for file_path in Path(".").glob(pattern):
            if file_path.is_file() and not any(part in EXCLUDED_DIRS for part in file_path.parts):
                files.add(file_path)
    return sorted(files)


def has_mixed_line_endings(text):
    return "\r\n" in text or "\r" in text


def check_file(path):
    content = path.read_text(encoding="utf-8")
    errors = []

    if has_mixed_line_endings(content):
        errors.append("must use LF line endings only")

    lines = content.split("\n")
    for index, line in enumerate(lines[:-1], start=1):
        if "\t" in line:
            errors.append(f"line {index}: contains tab character")
        if line.endswith(" "):
            errors.append(f"line {index}: has trailing whitespace")

    if content and not content.endswith("\n"):
        errors.append("missing final newline")

    return errors


def main():
    files = list_target_files()
    all_errors = []

    for file_path in files:
        file_errors = check_file(file_path)
        for error in file_errors:
            all_errors.append(f"{file_path}: {error}")

    if all_errors:
        print("FORMAT CHECK FAILED")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print(f"FORMAT CHECK PASSED ({len(files)} files scanned)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
