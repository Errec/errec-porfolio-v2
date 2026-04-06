# Release & Versioning Notes

This project uses a simple changelog-first release process for a static portfolio.

## Source of truth
- `CHANGELOG.md` is the release history source of truth.
- Each release entry must describe user-visible and platform-impacting changes.

## Changelog format
- Use date-based headings in UTC: `## YYYY-MM-DD`.
- Keep entries concise and grouped by outcome (security, accessibility, build, content, performance).
- Prefer action verbs (`Added`, `Improved`, `Fixed`, `Removed`, `Changed`).

## When to add a new release entry
Create a new `CHANGELOG.md` section when at least one of these is true:
- Security headers/CSP/runtime policies changed.
- Accessibility behavior or checks changed.
- Build/CI tooling changed.
- Public-facing content/pages changed.
- Performance-sensitive assets or rendering behavior changed.

## Pre-release checklist
- Ensure source files in `src/` are reflected in generated artifacts (`npm run build`).
- Run quality gates:
  - `npm run check:js`
  - `npm run check:a11y:ci`
  - `npm run check:format`
  - `npm run lint`
  - `npm test`
- Confirm roadmap/task status updates are committed when applicable.

## Release commit guidance
- Keep release commits focused on one logical milestone.
- Include changelog update in the same PR as the shipped change whenever possible.
- Reference related roadmap sections in the PR summary for traceability.
