from pathlib import Path

BASE = 'https://errec.vercel.app'

services = [
    '/services/frontend-architecture',
    '/services/iam-frontend-security',
    '/services/devsecops-ui-delivery',
]
articles = [
    '/articles/secure-authentication-ux-react',
    '/articles/frontend-devsecops-checklist',
]
projects = [
    '/',
    '/case-studies/enterprise-modernization',
    '/case-studies/iam-ciam-implementation',
]


def build_urlset(paths, changefreq='monthly', priority='0.8'):
    rows = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path in paths:
        p = '1.0' if path == '/' else priority
        cf = 'weekly' if path == '/' else changefreq
        rows += [
            '  <url>',
            f'    <loc>{BASE}{path}</loc>',
            f'    <changefreq>{cf}</changefreq>',
            f'    <priority>{p}</priority>',
            '  </url>',
        ]
    rows.append('</urlset>')
    return '\n'.join(rows) + '\n'

Path('sitemap-services.xml').write_text(build_urlset(services, 'monthly', '0.8'))
Path('sitemap-articles.xml').write_text(build_urlset(articles, 'monthly', '0.7'))
Path('sitemap-projects.xml').write_text(build_urlset(projects, 'weekly', '0.9'))
print('Sitemaps generated')
