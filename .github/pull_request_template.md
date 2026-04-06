## Summary
- Describe what changed and why.

## Related roadmap/task
- Link the roadmap item or issue addressed.

## Validation
- [ ] `npm run build`
- [ ] `npm run check:js`
- [ ] `npm run check:a11y:ci`
- [ ] `npm run check:format`
- [ ] `npm run lint`
- [ ] `npm test`

## Review checklist
### Accessibility
- [ ] Semantic structure and labels remain valid.
- [ ] Keyboard/focus behavior is preserved.
- [ ] `check:a11y:ci` passes with zero errors.

### Security
- [ ] No unsafe inline scripts/eval introduced.
- [ ] CSP/headers reviewed if runtime integrations changed.
- [ ] Form/data-handling changes include privacy impact review.

### Performance
- [ ] No unnecessary asset bloat introduced.
- [ ] Images and static assets are optimized for the change scope.
- [ ] Heavy DOM/SVG additions are justified.

### Tests and quality
- [ ] New/changed behavior is covered by tests or checks.
- [ ] Build artifacts regenerated from `src/` when applicable.
- [ ] Documentation/roadmap status updated when task status changed.
