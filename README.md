# Personal Portfolio

Static portfolio website deployed on Vercel.

## Tech stack
- HTML/CSS/Vanilla JavaScript
- Production assets (`css/main.min.css`, `js/bundle.min.js`)
- Source JavaScript in `src/js/main.js`
- Vercel security headers config (`vercel.json`)

## Project structure
- `src/js/main.js`: maintainable JavaScript source
- `js/bundle.min.js`: distributed JavaScript bundle
- `scripts/build_js.py`: build step to refresh bundle from source
- `scripts/check_js_quality.py`: lightweight quality checks
- `docs/`: review and planning notes

## Development workflow
1. Build JS bundle from source:
   ```bash
   npm run build:js
   ```
2. Run quality checks:
   ```bash
   npm run check:js
   ```
3. Run repository lint checks:
   ```bash
   npm run lint
   ```
4. Optional syntax validation:
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
