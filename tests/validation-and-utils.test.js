const test = require('node:test');
const assert = require('node:assert/strict');

const {
  debounce,
  throttle,
  validateContactFormValues,
  CONTACT_FORM_ERROR_MESSAGES,
} = require('../src/js/main.js');

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

test('validateContactFormValues returns valid state for valid inputs', () => {
  const result = validateContactFormValues({
    email: 'person@example.com',
    name: 'Jane',
    message: 'This message has more than twenty characters.',
    isEmailNativeValid: true,
  });

  assert.equal(result.isEmailValid, true);
  assert.equal(result.isNameValid, true);
  assert.equal(result.isMessageValid, true);
  assert.deepEqual(result.errors, {
    email: '',
    name: '',
    message: '',
  });
});

test('validateContactFormValues returns specific errors for invalid fields', () => {
  const result = validateContactFormValues({
    email: ' ',
    name: '',
    message: 'too short',
    isEmailNativeValid: false,
  });

  assert.equal(result.isEmailValid, false);
  assert.equal(result.isNameValid, false);
  assert.equal(result.isMessageValid, false);
  assert.deepEqual(result.errors, {
    email: CONTACT_FORM_ERROR_MESSAGES.email,
    name: CONTACT_FORM_ERROR_MESSAGES.name,
    message: CONTACT_FORM_ERROR_MESSAGES.message,
  });
});

test('debounce delays execution for trailing calls', async () => {
  let count = 0;
  const debounced = debounce(() => {
    count += 1;
  }, 30);

  debounced();
  debounced();
  debounced();
  assert.equal(count, 0);

  await sleep(50);
  assert.equal(count, 1);
});

test('throttle limits calls to one invocation within wait period', async () => {
  let count = 0;
  const throttled = throttle(() => {
    count += 1;
  }, 40);

  throttled();
  throttled();
  throttled();

  await sleep(20);
  assert.equal(count, 0);

  await sleep(40);
  assert.equal(count, 1);
});
