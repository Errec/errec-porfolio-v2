const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');

const sourceHtml = fs.readFileSync('src/html/index.html', 'utf8');
const sourceJs = fs.readFileSync('src/js/main.js', 'utf8');

test('primary navigation anchors reference in-page sections', () => {
  assert.match(sourceHtml, /class="header__link-skills" href="#skills"/);
  assert.match(sourceHtml, /class="header__link-work" href="#work"/);
  assert.match(sourceHtml, /class="header__link-about" href="#about"/);
});

test('contact form includes required fields and minimum message length', () => {
  assert.match(sourceHtml, /id="input-email"[^>]*type="email"[^>]*required/);
  assert.match(sourceHtml, /id="input-name"[^>]*type="text"[^>]*required/);
  assert.match(sourceHtml, /id="input-message"[^>]*minlength="20"[^>]*required/);
  assert.match(sourceHtml, /id="about-form"[^>]*action="https:\/\/formspree\.io\/f\/xblrwggz"/);
});

test('external profile links keep security rel attributes and labels', () => {
  const socialAnchors = sourceHtml.match(/<a href="https:\/\/(github\.com|codepen\.io|linkedin\.com|www\.freecodecamp\.com)[^>]*>/g);
  assert.ok(socialAnchors && socialAnchors.length >= 4);
  socialAnchors.forEach((anchor) => {
    assert.match(anchor, /rel="noopener noreferrer"/);
    assert.match(anchor, /aria-label="/);
  });
});

test('main runtime still initializes form checks on DOMContentLoaded', () => {
  assert.match(sourceJs, /document\.addEventListener\('DOMContentLoaded'/);
  assert.match(sourceJs, /checkForm\(\);/);
});
