# Code Review & Improvement Options

## Current strengths
- Good baseline SEO metadata in `index.html` (canonical, OpenGraph, Twitter, JSON-LD).
- Static architecture keeps operational complexity low.
- Core interactions are lightweight and dependency-free in `js/bundle.min.js`.

## High-impact improvement options

### Option A — Security hardening (recommended first)
1. Add `rel="noopener noreferrer"` to every `target="_blank"` link.
2. Remove inline `onclick` and move to JS event listeners only.
3. Add a strict Content Security Policy (via Vercel headers) and remove inline analytics script.
4. Upgrade from legacy Universal Analytics (`analytics.js`, `UA-*`) to GA4 or privacy-friendly analytics.
5. Add security headers: `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`, `Strict-Transport-Security`.

### Option B — Code quality and maintainability
1. Keep source files (`src/js`, `src/css`) and generate minified artifacts in build step.
2. Add ESLint + Prettier + Stylelint and basic CI checks.
3. Replace duplicated scroll-to-section wiring with one reusable function (already partially present, but duplicated call exists).
4. Remove dead/legacy code hooks (e.g., undefined `runMyFunction()` inline reference).
5. Introduce simple folder conventions (`/src`, `/public`, `/docs`) and a build script.

### Option C — UX/accessibility polish
1. Ensure icon-only social links include accessible labels (`aria-label`).
2. Add visible focus styles and keyboard test pass for all interactive elements.
3. Improve form validation (email pattern + message length + inline errors instead of `alert`).
4. Add `autocomplete` attributes (`email`, `name`) and submit-state feedback.
5. Reduce oversized inline SVG payload in HTML by moving to optimized external sprite.

### Option D — Professional productization
1. Expand from single-page to structured routes (`/services`, `/case-studies`, `/articles`).
2. Fill empty service/article sitemaps and automate sitemap generation.
3. Add project impact metrics and measurable outcomes in each case study.
4. Introduce lighthouse budgets and monitor in CI.
5. Add a changelog/release notes discipline and better README quality.

## Notable findings (evidence-driven)
- Multiple external links with `target="_blank"` are missing secure `rel` attributes.
- Contact form button contains inline `onclick="runMyFunction()"` while JS handles click separately.
- Manifest has empty `name` and `short_name`.
- Sitemap index references services/articles sitemap files that currently have no URLs.
- README has spelling issues and minimal setup documentation.

## Suggested implementation roadmap

### Phase 1 (1–2 days)
- Security link/headers cleanup.
- Form validation and inline handler removal.
- README professionalism pass.

### Phase 2 (3–5 days)
- Build pipeline + unminified source introduction.
- Linting + CI checks.
- SVG/image optimization.

### Phase 3 (1–2 weeks)
- Multi-page architecture for SEO discoverability.
- Case studies + services pages.
- Automated sitemap + analytics/event tracking improvements.
