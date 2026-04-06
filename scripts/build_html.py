from pathlib import Path
import re


SOURCE = Path("src/html/index.html")
DESTINATION = Path("index.html")


def minify_html(html: str) -> str:
    # Remove indentation/newlines between tags while preserving text content.
    collapsed = "".join(line.strip() for line in html.splitlines())
    collapsed = re.sub(r">\s+<", "><", collapsed)
    return f"{collapsed}\n"


def main():
    if not SOURCE.exists():
        raise FileNotFoundError(f"Source HTML file not found: {SOURCE}")

    minified_html = minify_html(SOURCE.read_text(encoding="utf-8"))
    DESTINATION.write_text(minified_html, encoding="utf-8")
    print(f"Wrote {DESTINATION} from {SOURCE}")


if __name__ == "__main__":
    main()
