(() => {
  'use strict';

  document.querySelectorAll('[data-project-switcher]').forEach((switcher) => {
    const summary = switcher.querySelector('summary');

    document.addEventListener('click', (event) => {
      if (switcher.open && !switcher.contains(event.target)) switcher.open = false;
    });

    switcher.addEventListener('keydown', (event) => {
      if (event.key !== 'Escape' || !switcher.open) return;
      event.preventDefault();
      switcher.open = false;
      summary.focus();
    });
  });
})();
