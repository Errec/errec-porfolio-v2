# SEO + Indexation Checkup (2026)

## Current status implemented in this patch

- Added stronger metadata (`title`, description, canonical, robots, OpenGraph, Twitter cards).
- Added JSON-LD graph with `Person`, `WebSite`, and `Occupation` (Prompt Engineer).
- Added crawler-friendly `robots.txt` allowing major search + AI crawlers.
- Added sitemap index architecture (`sitemap.xml` + split sitemap files).
- Added IndexNow key file (`/32f8f4846f294b048536fd6f8fdf2cb1.txt`).

## Gaps that still block "#1 for head terms"

1. **Keyword strategy is too broad if targeting generic terms**
   - Terms like "web developer" and "cyber security" are extremely competitive.
   - Priority should be niche intersections: `React IAM Authentication`, `Frontend Security Engineer`, `DevOps Prompt Engineering`.

2. **Single-page architecture limits topical authority**
   - You need dedicated indexable URLs for projects, services, and long-form technical guides.
   - Hashed anchors (`#projects`) do not build robust indexable clusters.

3. **Backlink authority and mentions are still required**
   - Technical SEO is necessary but not sufficient for top positions.
   - Need citations from reputable domains (guest posts, talks, OSS docs, interviews).

4. **No live content publication cadence**
   - Google favors freshness and depth for emerging intersections (AI + DevSecOps + frontend security).

## Best-practice roadmap (next 90 days)

### 1) Content architecture

- Create indexable pages:
  - `/projects`
  - `/services`
  - `/articles`
  - `/articles/react-iam-authentication`
  - `/articles/devops-prompt-engineering`
  - `/articles/frontend-security-checklist`

### 2) Structured data expansion

- Keep `Person` as the root identity graph.
- Add per-page schemas:
  - `Article` for guides.
  - `SoftwareSourceCode` for technical code/project pages.
  - `Service` for consulting offerings.

### 3) Indexation workflow

- Submit sitemap index in Google Search Console + Bing Webmaster Tools.
- Implement an automatic IndexNow ping when deploying new URLs.
  - Endpoint pattern:
    - `https://api.indexnow.org/indexnow?url=<URL>&key=32f8f4846f294b048536fd6f8fdf2cb1&keyLocation=https://errec.vercel.app/32f8f4846f294b048536fd6f8fdf2cb1.txt`

### 4) Internal linking (hub & spoke)

- Create a pillar page:
  - `Secure Web Development with React and Identity Platforms`
- Every spoke article must:
  - link back to pillar,
  - link to 2-3 sibling spokes,
  - include a short author bio tied to your `Person` entity.

### 5) Performance targets (Core Web Vitals)

- LCP: under 1.5s on mobile.
- CLS: under 0.1.
- INP: under 200ms.

## Realistic ranking goals

- **Head terms**: unlikely short-term.
- **Intersection terms**: realistic path to page 1 and featured AI citations.
- **LinkedIn discoverability**: improved by consistent Name/Title/SameAs signals across website + LinkedIn + GitHub.
