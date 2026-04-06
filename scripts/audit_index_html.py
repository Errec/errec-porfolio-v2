from html.parser import HTMLParser
from pathlib import Path
import json


class TagCounter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.total_tags = 0
        self.svg_tags = 0
        self.script_tags = 0
        self.meta_tags = 0

    def handle_starttag(self, tag, attrs):
        self.total_tags += 1
        if tag == "svg":
            self.svg_tags += 1
        if tag == "script":
            self.script_tags += 1
        if tag == "meta":
            self.meta_tags += 1


def audit_file(path: Path):
    html = path.read_text(encoding="utf-8")
    parser = TagCounter()
    parser.feed(html)
    parser.close()

    return {
        "file": str(path),
        "bytes": path.stat().st_size,
        "total_tags": parser.total_tags,
        "svg_tags": parser.svg_tags,
        "script_tags": parser.script_tags,
        "meta_tags": parser.meta_tags,
    }


def main():
    source = audit_file(Path("src/html/index.html"))
    artifact = audit_file(Path("index.html"))
    report = {
        "source": source,
        "artifact": artifact,
        "note": "Lower byte and tag counts generally improve parse cost and maintainability.",
    }

    output = Path("reports/index-audit.json")
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Wrote {output}")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
