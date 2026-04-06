# Project Improvement Task Roadmap

This roadmap converts the latest review into concrete implementation tasks.

## Phase 1 — Quick wins (Week 1)

### 1) Accessibility hardening
- [x] Add explicit form labels (screen-reader friendly) for contact inputs.
- [x] Add `aria-invalid` state handling for email/name/message validation.
- [ ] Add per-field helper/error messages and map with `aria-describedby`.
- [x] Run automated a11y checks (axe/Lighthouse) and fix critical issues.

### 2) Presentation consistency
- [x] Remove repeated inline `style` attributes from service/article/case pages.
- [x] Introduce shared `.content-page__main` style utility in CSS.
- [x] Migrate remaining one-off styles to reusable classes.

### 3) Production cleanliness
- [x] Remove non-essential production analytics console logging.
- [x] Add optional debug flag for local analytics troubleshooting.

### Current implementation sequence (doable tasks)
1. [ ] Add per-field helper/error elements in the contact form markup with dedicated IDs.
2. [ ] Extend form validation to write errors per field and keep `aria-invalid` updated on blur/input.
3. [x] Add an opt-in analytics debug mode (`?analyticsDebug=1`) persisted in localStorage.
4. [x] Run automated a11y checks and address critical issues from the report.
5. [ ] Add unit tests for validation logic to protect the new per-field behavior.

## Phase 2 — Reliability & quality (Week 2)

### 4) Automated testing foundation
- [x] Add unit tests for validation logic and utility behavior (debounce/throttle).
- [ ] Add Playwright smoke tests for navigation + contact form behavior.
- [x] Add accessibility CI gate (axe/Lighthouse threshold).

### 5) Maintainable source structure
- [x] Keep human-readable source HTML/CSS files and generate minified artifacts in build.
- [x] Add formatter/linter configuration for HTML/CSS/JS consistency.

## Phase 3 — Performance & platform hardening (Week 3)

### 6) Frontend performance
- [x] Audit and reduce `index.html` DOM/markup size.
- [ ] Move heavy decorative SVG/icon markup to reusable sprite strategy where feasible.
- [ ] Add modern image formats and verify dimensions for all project assets.

### 7) Security and policy maturity
- [x] Review CSP against analytics/runtime integrations and tighten allowlists.
- [x] Add privacy note for form/analytics data handling.

## Phase 4 — Governance (Week 4)

### 8) Team workflow
- [x] Add CONTRIBUTING guide with style, naming, and review checklist.
- [x] Add checklist-driven PR template (a11y, security, performance, tests).
- [x] Add release/versioning notes aligned with CHANGELOG usage.

---

## Definition of done for this roadmap
- No inline layout styles in content pages.
- Contact form has accessible labels + validity state handling.
- CI includes lint + syntax + functional smoke tests + accessibility checks.
- Source files remain readable; production artifacts are generated.
