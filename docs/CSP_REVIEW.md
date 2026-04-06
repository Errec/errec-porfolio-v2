# CSP Review (2026-04-06)

This document records the latest CSP review aligned with current runtime integrations.

## Scope reviewed
- Static site assets (`index.html`, `css/main.min.css`, `js/bundle.min.js`)
- Form submission endpoint (Formspree)
- Optional analytics hooks in `src/js/main.js` (`window.gtag`, `window.plausible`)

## Policy decisions
- Keep `script-src 'self'` to disallow third-party script injection by default.
- Tighten `img-src` from broad `https:` to `https://errec.vercel.app` plus `data:`.
- Expand `connect-src` with explicit allowlist entries for known integrations:
  - `https://formspree.io`
  - `https://www.google-analytics.com`
  - `https://plausible.io`
- Add explicit defensive directives:
  - `frame-src 'none'`
  - `manifest-src 'self'`
  - `media-src 'self'`
  - `worker-src 'self'`

## Result
The CSP in `vercel.json` now uses narrower host allowlists while preserving expected runtime behavior for form submissions and optional analytics event transport.
