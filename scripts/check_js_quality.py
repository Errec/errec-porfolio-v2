from pathlib import Path
import re

content = Path('src/js/main.js').read_text()

checks = {
    'uses_scroll_to_sections_once': content.count('scrollToSections();') == 1,
    'no_duplicate_sections_map': content.count("'.header__link-skills': '.main-skills'") == 1,
    'no_inline_handler_reference': 'runMyFunction' not in Path('index.html').read_text(),
}

failed = [name for name, ok in checks.items() if not ok]
for name, ok in checks.items():
    print(f"{name}: {'PASS' if ok else 'FAIL'}")

if failed:
    raise SystemExit(1)
