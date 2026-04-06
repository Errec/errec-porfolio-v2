# Project Improvement Task Roadmap

This roadmap converts the latest review into concrete implementation tasks.

## Phase 1 — Quick wins (Week 1)

### 1) Accessibility hardening
- [x] Add explicit form labels (screen-reader friendly) for contact inputs.
- [x] Add `aria-invalid` state handling for email/name/message validation.
- [ ] Add per-field helper/error messages and map with `aria-describedby`.
- [ ] Run automated a11y checks (axe/Lighthouse) and fix critical issues.

### 2) Presentation consistency
- [x] Remove repeated inline `style` attributes from service/article/case pages.
- [x] Introduce shared `.content-page__main` style utility in CSS.
- [ ] Migrate remaining one-off styles to reusable classes.

### 3) Production cleanliness
- [x] Remove non-essential production analytics console logging.
- [ ] Add optional debug flag for local analytics troubleshooting.

## Phase 2 — Reliability & quality (Week 2)

### 4) Automated testing foundation
- [ ] Add unit tests for validation logic and utility behavior (debounce/throttle).
- [ ] Add Playwright smoke tests for navigation + contact form behavior.
- [ ] Add accessibility CI gate (axe/Lighthouse threshold).

### 5) Maintainable source structure
- [ ] Keep human-readable source HTML/CSS files and generate minified artifacts in build.
- [ ] Add formatter/linter configuration for HTML/CSS/JS consistency.

## Phase 3 — Performance & platform hardening (Week 3)

### 6) Frontend performance
- [ ] Audit and reduce `index.html` DOM/markup size.
- [ ] Move heavy decorative SVG/icon markup to reusable sprite strategy where feasible.
- [ ] Add modern image formats and verify dimensions for all project assets.

### 7) Security and policy maturity
- [ ] Review CSP against analytics/runtime integrations and tighten allowlists.
- [ ] Add privacy note for form/analytics data handling.

## Phase 4 — Governance (Week 4)

### 8) Team workflow
- [ ] Add CONTRIBUTING guide with style, naming, and review checklist.
- [ ] Add checklist-driven PR template (a11y, security, performance, tests).
- [ ] Add release/versioning notes aligned with CHANGELOG usage.

---

## Definition of done for this roadmap
- No inline layout styles in content pages.
- Contact form has accessible labels + validity state handling.
- CI includes lint + syntax + functional smoke tests + accessibility checks.
- Source files remain readable; production artifacts are generated.
