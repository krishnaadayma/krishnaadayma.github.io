window.Animations = (() => {
  function init() {
    const animated = document.querySelectorAll('[data-animate]');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
          setTimeout(() => entry.target.classList.add('visible'), index * 80);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.18 });

    animated.forEach(el => observer.observe(el));

    const hero = document.querySelector('.hero');
    if (hero) {
      document.addEventListener('scroll', () => {
        hero.style.backgroundPositionY = `${window.scrollY * 0.2}px`;
      }, { passive: true });
    }
  }

  return { init };
})();
