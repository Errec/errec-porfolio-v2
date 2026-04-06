# Personal Portfolio

Static portfolio website deployed on Vercel.

## Tech stack
- HTML/CSS/Vanilla JavaScript
- Production assets (`css/main.min.css`, `js/bundle.min.js`)
- Source JavaScript in `src/js/main.js`
- Vercel security headers config (`vercel.json`)

## Project structure
- `src/`: human-readable source files (`html`, `css`, `js`)
- `index.html`, `css/main.min.css`, `js/bundle.min.js`: generated/distributed artifacts
- `scripts/`: build + quality automation
- `tests/`: unit and smoke checks
- `docs/`: governance/process notes
- `reports/`: generated audit/check reports

## Prerequisites
- Node.js 20+
- Python 3.10+ (used by the build and audit scripts)

## Development workflow
1. Install dependencies:
   ```bash
   npm install
   ```
2. Build distributable assets and sitemaps:
   ```bash
   npm run build
   ```
3. Run quality checks:
   ```bash
   npm run check:js
   npm run check:a11y:ci
   npm run check:format
   npm run audit:index
   npm run audit:images
   ```
4. Run repository lint checks and tests:
   ```bash
   npm run lint
   npm test
   ```
5. Optional syntax validation:
   ```bash
   node --check src/js/main.js
   node --check js/bundle.min.js
   ```

## Deployment
Deployed on Vercel.


## CI
- GitHub Actions workflow: `.github/workflows/ci.yml`
- Full local equivalent:
  ```bash
  npm run ci:check
  ```
