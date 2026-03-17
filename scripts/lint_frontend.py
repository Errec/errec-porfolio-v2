import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

errors = []
html = Path('index.html').read_text()

anchors = re.findall(r'<a\b[^>]*>', html)
for tag in anchors:
    if 'target="_blank"' in tag and 'rel="noopener noreferrer"' not in tag and 'rel="noreferrer noopener"' not in tag:
        errors.append(f'Missing secure rel in target=_blank anchor: {tag[:120]}')

if re.search(r'\son\w+="', html):
    errors.append('Inline event handlers found in index.html')

manifest = json.loads(Path('favicon/site.webmanifest').read_text())
if not manifest.get('name'):
    errors.append('favicon/site.webmanifest missing non-empty name')
if not manifest.get('short_name'):
    errors.append('favicon/site.webmanifest missing non-empty short_name')

ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
for sitemap in ['sitemap-services.xml', 'sitemap-articles.xml', 'sitemap-projects.xml']:
    root = ET.parse(sitemap).getroot()
    if len(root.findall('sm:url', ns)) == 0:
        errors.append(f'{sitemap} has zero url entries')

# Keep HTML payload under a basic threshold for this static site
index_size_kb = Path('index.html').stat().st_size / 1024
if index_size_kb > 250:
    errors.append(f'index.html too large ({index_size_kb:.1f}KB) - consider externalizing inline assets')

if errors:
    print('LINT FAILED')
    for err in errors:
        print('-', err)
    sys.exit(1)

print('LINT PASSED')
