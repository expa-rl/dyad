/* Adapted from the Academic Project Page Template / ExpA page. */
(() => {
  'use strict';

  const scrollButton = document.getElementById('scroll-to-top');
  const copyButton = document.getElementById('copy-bibtex');
  const citation = document.getElementById('bibtex-code');
  const status = document.getElementById('copy-status');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let resetCopy;

  const overviewVideo = document.getElementById('overview-video');
  const overviewPlay = document.getElementById('overview-play');
  const overviewStatus = document.getElementById('overview-video-status');
  if (overviewVideo && overviewPlay && overviewStatus) {
    const syncOverviewPlay = () => {
      overviewPlay.hidden = !overviewVideo.paused || Boolean(overviewVideo.error);
    };
    const showOverviewError = () => {
      overviewPlay.hidden = true;
      overviewStatus.hidden = false;
    };
    overviewVideo.addEventListener('play', syncOverviewPlay);
    overviewVideo.addEventListener('pause', syncOverviewPlay);
    overviewVideo.addEventListener('ended', syncOverviewPlay);
    overviewVideo.addEventListener('error', showOverviewError);
    overviewVideo.querySelector('source')?.addEventListener('error', showOverviewError);
    overviewPlay.addEventListener('click', async () => {
      try {
        await overviewVideo.play();
        overviewVideo.focus({ preventScroll: true });
      } catch (error) {
        if (error.name === 'AbortError') syncOverviewPlay();
        else showOverviewError();
      }
    });
    if (overviewVideo.error) showOverviewError();
    else syncOverviewPlay();
  }

  const carousel = document.querySelector('[data-capability-carousel]');
  if (carousel) {
    const slides = [...carousel.querySelectorAll('.capability-slide')];
    const selection = carousel.querySelector('[data-selection]');
    let selected = 0;
    const showSlide = (index) => {
      selected = (index + slides.length) % slides.length;
      slides.forEach((slide, i) => { slide.hidden = i !== selected; });
      selection.replaceChildren(
        document.createTextNode(`Trained on ${slides[selected].dataset.environment} `),
        Object.assign(document.createElement('span'), {
          className: 'figure-count', textContent: `${selected + 1} / ${slides.length}`,
        }),
      );
    };
    carousel.querySelector('[data-previous]').addEventListener('click', () => showSlide(selected - 1));
    carousel.querySelector('[data-next]').addEventListener('click', () => showSlide(selected + 1));
    carousel.addEventListener('keydown', (event) => {
      if (event.key !== 'ArrowLeft' && event.key !== 'ArrowRight') return;
      event.preventDefault();
      showSlide(selected + (event.key === 'ArrowRight' ? 1 : -1));
    });
    carousel.querySelector('.figure-controls').hidden = false;
    showSlide(0);
  }

  const video = document.getElementById('approach-video');
  const videoSource = document.getElementById('approach-video-source');
  const videoFallback = document.getElementById('approach-video-fallback');
  const videoStatus = document.getElementById('approach-video-status');
  const videoLink = document.getElementById('approach-video-link');
  const videoSrc = video?.dataset.videoSrc?.trim();

  if (video && videoSource && videoFallback && videoSrc) {
    const showFallback = () => {
      video.hidden = true;
      videoFallback.hidden = false;
      if (videoStatus) videoStatus.textContent = 'Video unavailable. Explore the architecture below.';
    };
    video.addEventListener('error', showFallback);
    videoSource.addEventListener('error', showFallback);
    videoSource.src = videoSrc;
    if (videoLink) {
      videoLink.href = videoSrc;
      videoLink.textContent = 'Open the MP4 video';
    }
    videoFallback.hidden = true;
    video.hidden = false;
    video.load();
  }

  if (scrollButton) {
    const updateScrollButton = () => {
      const visible = window.scrollY > 300;
      scrollButton.classList.toggle('visible', visible);
      scrollButton.tabIndex = visible ? 0 : -1;
    };
    window.addEventListener('scroll', updateScrollButton, { passive: true });
    scrollButton.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: reducedMotion.matches ? 'instant' : 'smooth' });
      document.getElementById('paper-title')?.focus({ preventScroll: true });
    });
    updateScrollButton();
  }

  function copyWithSelection(text) {
    const field = document.createElement('textarea');
    field.value = text;
    field.setAttribute('readonly', '');
    field.style.position = 'fixed';
    field.style.left = '-9999px';
    document.body.appendChild(field);
    field.select();
    let copied = false;
    try {
      copied = document.execCommand('copy');
    } finally {
      field.remove();
      copyButton?.focus({ preventScroll: true });
    }
    if (!copied) throw new Error('Clipboard access unavailable');
  }

  if (copyButton && citation && status) {
    copyButton.addEventListener('click', async () => {
      clearTimeout(resetCopy);
      try {
        const text = citation.textContent.trim();
        try {
          if (!navigator.clipboard?.writeText) throw new Error('Clipboard API unavailable');
          await navigator.clipboard.writeText(text);
        } catch {
          copyWithSelection(text);
        }
        copyButton.classList.add('copied');
        copyButton.querySelector('.copy-text').textContent = 'Copied!';
        status.textContent = 'Citation copied to clipboard.';
      } catch {
        copyButton.classList.remove('copied');
        copyButton.querySelector('.copy-text').textContent = 'Copy';
        status.textContent = 'Please select the citation and copy it manually.';
      }
      resetCopy = setTimeout(() => {
        copyButton.classList.remove('copied');
        copyButton.querySelector('.copy-text').textContent = 'Copy';
        status.textContent = '';
      }, 2500);
    });
  }
})();
