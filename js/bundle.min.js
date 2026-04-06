const debounce = (fn, wait, options = {}) => {
  let timeout;
  let lastCall = 0;
  const { leading = false, trailing = true, maxWait } = options;

  const later = (context, args) => {
    const elapsed = Date.now() - lastCall;
    if (elapsed < wait && elapsed >= 0) {
      timeout = setTimeout(later, wait - elapsed, context, args);
      return;
    }

    timeout = null;
    if (trailing && !(leading && !maxWait)) {
      fn.apply(context, args);
    }
  };

  return function debounced(...args) {
    lastCall = Date.now();
    const callNow = leading && !timeout;

    if (!timeout) {
      timeout = setTimeout(later, wait, this, args);
    }

    if (callNow) {
      fn.apply(this, args);
    }
  };
};

const throttle = (fn, wait, options = {}) => debounce(fn, wait, { ...options, maxWait: wait });

const scrollToSections = () => {
  const sections = {
    '.header__link-skills': '#skills',
    '.header__link-work': '#work',
    '.header__link-about': '#about',
  };

  Object.entries(sections).forEach(([triggerSelector, targetSelector]) => {
    const trigger = document.querySelector(triggerSelector);
    const target = document.querySelector(targetSelector);

    if (!trigger || !target) return;

    trigger.addEventListener('click', (event) => {
      event.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
      target.focus({ preventScroll: true });
    });
  });
};

const parallaxAboutBg = () => {
  const bg = document.getElementById('about-parallax-img');
  const about = document.getElementById('about');
  if (!bg || !about) return;

  const onScroll = () => {
    if (window.scrollY + window.innerHeight - about.clientHeight / 1.2 > about.offsetTop) {
      bg.classList.add('main-about__paralax-wrapper--exit');
      window.removeEventListener('scroll', onScroll);
    }
  };

  window.addEventListener('scroll', onScroll);
};

const animatePin = () => {
  const pin = document.getElementById('footer-pin');
  if (!pin) return;

  const onScroll = debounce(() => {
    const nearBottom = window.scrollY + window.innerHeight >= document.documentElement.offsetHeight - 10;
    pin.classList.toggle('footer__pin--enter', nearBottom);
  }, 200);

  window.addEventListener('scroll', onScroll);
};

const heroAnimation = () => {
  const box = document.getElementById('box-wrapper');
  const right = document.getElementById('right-hand');
  const left = document.getElementById('left-hand');
  const hero = document.getElementById('hero');
  if (!box || !right || !left || !hero) return;

  const onScroll = throttle(() => {
    if (window.scrollY + window.innerHeight - hero.clientHeight / 2.4 > hero.offsetTop) {
      left.classList.add('main-hero__left-hand--move');
      right.classList.add('main-hero__right-hand--move');
      box.classList.add('hero__box--state-1');
      window.removeEventListener('scroll', onScroll);
    }
  }, 250);

  window.addEventListener('scroll', onScroll);
};

const svgHover = () => {
  const grid = document.getElementById('skills-grid');
  if (!grid) return;

  grid.addEventListener('mouseover', (event) => {
    if (event.target !== grid) {
      event.target.classList.remove('main-skills__svg--fill');
    }
  });

  grid.addEventListener('mouseout', (event) => {
    if (event.target !== grid) {
      event.target.classList.add('main-skills__svg--fill');
    }
  });
};

const workGridAnimation = () => {
  const items = document.querySelectorAll('.main-work__item');

  const onScroll = throttle(() => {
    items.forEach((item, index) => {
      const shouldAnimate = window.scrollY - item.offsetTop > -150 && window.innerWidth < 720;
      if (shouldAnimate && item.classList.contains('main-work__item--grow')) {
        item.classList.remove('main-work__item--grow');
        if (index >= items.length - 1) {
          window.removeEventListener('scroll', onScroll);
        }
      }
    });
  }, 200);

  window.addEventListener('scroll', onScroll);
};

const checkForm = () => {
  const message = document.getElementById('input-message');
  const email = document.getElementById('input-email');
  const name = document.querySelector('input[name="name"]');
  const form = document.getElementById('about-form');
  const status = document.getElementById('form-status');
  const button = document.getElementById('input-btn');
  const emailError = document.getElementById('input-email-error');
  const nameError = document.getElementById('input-name-error');
  const messageError = document.getElementById('input-message-error');
  if (!message || !email || !name || !form || !status || !button || !emailError || !nameError || !messageError) return;

  const fieldDefinitions = {
    email: {
      element: email,
      errorElement: emailError,
      isValid: (value) => Boolean(value.trim()) && email.checkValidity(),
      errorMessage: 'Please enter a valid email address.',
    },
    name: {
      element: name,
      errorElement: nameError,
      isValid: (value) => Boolean(value.trim()),
      errorMessage: 'Please enter your name.',
    },
    message: {
      element: message,
      errorElement: messageError,
      isValid: (value) => value.trim().length >= 20,
      errorMessage: 'Please provide at least 20 characters about your project.',
    },
  };

  const markFieldValidity = (field, isValid) => {
    field.setAttribute('aria-invalid', String(!isValid));
  };

  const setFieldError = (errorElement, text = '') => {
    errorElement.textContent = text;
  };

  const validateField = (fieldKey) => {
    const field = fieldDefinitions[fieldKey];
    const value = field.element.value;
    const isValid = field.isValid(value);

    markFieldValidity(field.element, isValid);
    setFieldError(field.errorElement, isValid ? '' : field.errorMessage);

    return isValid;
  };

  const validateAllFields = () => {
    const validationState = {
      isEmailValid: validateField('email'),
      isNameValid: validateField('name'),
      isMessageValid: validateField('message'),
    };

    return validationState;
  };

  const setStatus = (text, isError = false) => {
    status.textContent = text;
    status.classList.toggle('main-about__form-status--error', isError);
    status.classList.toggle('main-about__form-status--success', !isError && text.length > 0);
  };

  Object.entries(fieldDefinitions).forEach(([fieldKey, field]) => {
    field.element.addEventListener('blur', () => {
      validateField(fieldKey);
    });

    field.element.addEventListener('input', () => {
      if (field.element.getAttribute('aria-invalid') === 'true') {
        validateField(fieldKey);
      }
    });
  });

  form.addEventListener('submit', (event) => {
    const { isEmailValid, isNameValid, isMessageValid } = validateAllFields();

    if (!isEmailValid || !isNameValid || !isMessageValid) {
      event.preventDefault();
      setStatus('Please provide a valid email, your name, and a message with at least 20 characters.', true);
      return;
    }

    button.disabled = true;
    button.setAttribute('aria-busy', 'true');
    setStatus('Sending your message...');
  });
};

const setupSmoothScrollPolyfill = () => {
  if ('scrollBehavior' in document.documentElement.style) return;

  const easeInOutQuad = (currentTime, start, change, duration) => {
    const time = currentTime / (duration / 2);
    if (time < 1) return (change / 2) * time * time + start;
    const normalized = time - 1;
    return (-change / 2) * (normalized * (normalized - 2) - 1) + start;
  };

  const smoothScrollTo = (element) => {
    const startY = window.scrollY;
    const targetY = element.getBoundingClientRect().top + startY;
    const distance = targetY - startY;
    let startTime;

    const step = (timestamp) => {
      if (!startTime) startTime = timestamp;
      const elapsed = timestamp - startTime;
      const y = easeInOutQuad(elapsed, startY, distance, 468);
      window.scrollTo(0, y);

      if (elapsed < 468) {
        requestAnimationFrame(step);
      } else {
        window.scrollTo(0, targetY);
      }
    };

    requestAnimationFrame(step);
  };

  window.scrollBy = (x, y) => smoothScrollTo({
    getBoundingClientRect: () => ({ top: window.scrollY + y - window.scrollY }),
  });

  const nativeScrollIntoView = Element.prototype.scrollIntoView;
  Element.prototype.scrollIntoView = function scrollIntoViewWithFallback(options = { behavior: 'auto' }) {
    if (options.behavior === 'smooth') {
      smoothScrollTo(this);
      return;
    }
    nativeScrollIntoView.call(this, options);
  };
};


const setupConversionTracking = () => {
  const isAnalyticsDebugEnabled = () => {
    try {
      const params = new URLSearchParams(window.location.search);
      const debugParam = params.get('analyticsDebug');

      if (debugParam === '1' || debugParam === 'true') {
        window.localStorage.setItem('analytics-debug', 'true');
      }

      if (debugParam === '0' || debugParam === 'false') {
        window.localStorage.removeItem('analytics-debug');
      }

      return window.localStorage.getItem('analytics-debug') === 'true';
    } catch (error) {
      return false;
    }
  };

  const debugEnabled = isAnalyticsDebugEnabled();
  const trackedLinks = document.querySelectorAll('[data-track]');
  trackedLinks.forEach((link) => {
    link.addEventListener('click', () => {
      const eventName = link.getAttribute('data-track');

      if (debugEnabled) {
        console.debug('[analytics-debug] Tracking event:', eventName, link);
      }

      if (window.gtag) {
        window.gtag('event', eventName, { event_category: 'engagement' });
      }
      if (window.plausible) {
        window.plausible(eventName);
      }
    });
  });
};

document.addEventListener('DOMContentLoaded', () => {
  parallaxAboutBg();
  animatePin();
  heroAnimation();
  svgHover();
  workGridAnimation();
  checkForm();
  scrollToSections();
  setupSmoothScrollPolyfill();
  setupConversionTracking();
});
