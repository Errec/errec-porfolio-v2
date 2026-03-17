from pathlib import Path

SRC = Path('src/js/main.js')
DEST = Path('js/bundle.min.js')

DEST.write_text(SRC.read_text())
print(f'Wrote {DEST} from {SRC}')
