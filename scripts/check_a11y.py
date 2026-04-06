from html.parser import HTMLParser
from pathlib import Path
import argparse
import json
import sys


HTML_GLOBS = [
    "index.html",
    "services/*.html",
    "articles/*.html",
    "case-studies/*.html",
]


class A11yParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.labels_for = set()
        self.controls = []
        self.images = []
        self.aria_describedby = []
        self.aria_labelledby = []
        self.accessible_name_targets = []
        self.current_tag_stack = []
        self.h1_count = 0
        self.has_html_lang = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self.current_tag_stack.append(tag)

        element_id = attrs_dict.get("id")
        if element_id:
            self.ids.add(element_id)

        if tag == "html":
            self.has_html_lang = bool(attrs_dict.get("lang", "").strip())

        if tag == "h1":
            self.h1_count += 1

        if tag == "label" and attrs_dict.get("for"):
            self.labels_for.add(attrs_dict["for"])

        if tag in {"input", "textarea", "select"}:
            input_type = attrs_dict.get("type", "").lower()
            if tag == "input" and input_type in {"hidden", "submit", "button", "reset"}:
                return
            self.controls.append(
                {
                    "tag": tag,
                    "id": attrs_dict.get("id"),
                    "name": attrs_dict.get("name"),
                    "aria-label": attrs_dict.get("aria-label", "").strip(),
                }
            )

        if tag == "img":
            self.images.append({"src": attrs_dict.get("src", ""), "alt": attrs_dict.get("alt")})

        if attrs_dict.get("aria-describedby"):
            self.aria_describedby.append(attrs_dict["aria-describedby"])

        if attrs_dict.get("aria-labelledby"):
            self.aria_labelledby.append(attrs_dict["aria-labelledby"])

        if tag in {"a", "button"}:
            self.accessible_name_targets.append(
                {
                    "tag": tag,
                    "aria-label": attrs_dict.get("aria-label", "").strip(),
                    "text": "",
                }
            )

    def handle_endtag(self, tag):
        if self.current_tag_stack and self.current_tag_stack[-1] == tag:
            self.current_tag_stack.pop()

    def handle_data(self, data):
        if not self.current_tag_stack:
            return
        current = self.current_tag_stack[-1]
        if current in {"a", "button"} and self.accessible_name_targets:
            self.accessible_name_targets[-1]["text"] += data.strip()


def expand_html_files():
    files = []
    for pattern in HTML_GLOBS:
        files.extend(Path(".").glob(pattern))
    return sorted(set(files))


def collect_errors_for_file(path):
    parser = A11yParser()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.close()
    errors = []

    if not parser.has_html_lang:
        errors.append("Missing lang attribute on <html>.")

    if parser.h1_count != 1:
        errors.append(f"Expected exactly one <h1>, found {parser.h1_count}.")

    for control in parser.controls:
        has_id_label = bool(control["id"] and control["id"] in parser.labels_for)
        has_aria_label = bool(control["aria-label"])
        if not has_id_label and not has_aria_label:
            control_name = control["id"] or control["name"] or control["tag"]
            errors.append(f"Form control '{control_name}' is missing an associated label.")

    for img in parser.images:
        if img["alt"] is None:
            errors.append(f"Image '{img['src']}' is missing alt text.")

    for value in parser.aria_describedby:
        for ref in value.split():
            if ref not in parser.ids:
                errors.append(f"aria-describedby reference '{ref}' does not exist.")

    for value in parser.aria_labelledby:
        for ref in value.split():
            if ref not in parser.ids:
                errors.append(f"aria-labelledby reference '{ref}' does not exist.")

    for target in parser.accessible_name_targets:
        if not target["aria-label"] and not target["text"]:
            errors.append(f"<{target['tag']}> element appears to have no accessible name.")

    return errors


def main():
    parser = argparse.ArgumentParser(description="Run static accessibility checks.")
    parser.add_argument("--max-errors", type=int, default=0, help="Maximum allowed accessibility errors.")
    parser.add_argument("--report", type=str, default="", help="Optional JSON report output path.")
    args = parser.parse_args()

    html_files = expand_html_files()
    if not html_files:
        print("No HTML files found for accessibility checks.")
        return 1

    all_errors = []
    for file_path in html_files:
        file_errors = collect_errors_for_file(file_path)
        for error in file_errors:
            all_errors.append(f"{file_path}: {error}")

    report = {
        "pages_scanned": len(html_files),
        "error_count": len(all_errors),
        "max_errors": args.max_errors,
        "errors": all_errors,
    }

    if args.report:
        Path(args.report).write_text(json.dumps(report, indent=2), encoding="utf-8")

    if len(all_errors) > args.max_errors:
        print("A11Y CHECK FAILED")
        print(f"- Total errors: {len(all_errors)} (max allowed: {args.max_errors})")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print(
        f"A11Y CHECK PASSED ({len(html_files)} pages scanned, "
        f"errors: {len(all_errors)}, threshold: {args.max_errors})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
