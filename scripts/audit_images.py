from pathlib import Path
import json
import re
import struct


IMAGE_PATTERNS = ["img/*", "favicon/*"]


def parse_png_dimensions(path: Path):
    with path.open("rb") as f:
        signature = f.read(8)
        if signature != b"\x89PNG\r\n\x1a\n":
            return None
        _length = f.read(4)
        chunk_type = f.read(4)
        if chunk_type != b"IHDR":
            return None
        width, height = struct.unpack(">II", f.read(8))
        return {"width": width, "height": height}


def parse_jpeg_dimensions(path: Path):
    with path.open("rb") as f:
        data = f.read()
    if not data.startswith(b"\xff\xd8"):
        return None
    i = 2
    while i < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        i += 2
        if marker in {0xD8, 0xD9}:
            continue
        length = struct.unpack(">H", data[i:i + 2])[0]
        if marker in {0xC0, 0xC2}:
            height = struct.unpack(">H", data[i + 3:i + 5])[0]
            width = struct.unpack(">H", data[i + 5:i + 7])[0]
            return {"width": width, "height": height}
        i += length
    return None


def parse_svg_dimensions(path: Path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    view_box_match = re.search(r'viewBox="([^"]+)"', text)
    width_match = re.search(r'width="([^"]+)"', text)
    height_match = re.search(r'height="([^"]+)"', text)
    result = {}
    if view_box_match:
        result["viewBox"] = view_box_match.group(1)
    if width_match:
        result["width"] = width_match.group(1)
    if height_match:
        result["height"] = height_match.group(1)
    return result


def collect_images():
    images = []
    for pattern in IMAGE_PATTERNS:
        for file_path in sorted(Path(".").glob(pattern)):
            if file_path.is_file():
                images.append(file_path)
    return images


def main():
    image_files = collect_images()
    entries = []
    modern_candidates = []

    for file_path in image_files:
        suffix = file_path.suffix.lower()
        entry = {
            "file": str(file_path),
            "bytes": file_path.stat().st_size,
            "format": suffix.lstrip("."),
        }

        if suffix == ".png":
            dimensions = parse_png_dimensions(file_path)
            if dimensions:
                entry.update(dimensions)
            modern_candidates.append(str(file_path))
        elif suffix in {".jpg", ".jpeg"}:
            dimensions = parse_jpeg_dimensions(file_path)
            if dimensions:
                entry.update(dimensions)
            modern_candidates.append(str(file_path))
        elif suffix == ".svg":
            entry.update(parse_svg_dimensions(file_path))

        entries.append(entry)

    report = {
        "images_scanned": len(entries),
        "modern_format_candidates": modern_candidates,
        "entries": entries,
        "note": "Candidates list identifies PNG/JPEG assets that can be converted to WebP/AVIF.",
    }

    out = Path("docs/image-assets-report.json")
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Wrote {out} ({len(entries)} assets)")


if __name__ == "__main__":
    main()
