window.Navbar = (() => {
  function init() {
    const navbar = document.querySelector('.navbar');
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    const sectionLinks = [...document.querySelectorAll('.nav-links a[href^="#"]')];
    const sections = sectionLinks.map((link) => document.querySelector(link.getAttribute('href'))).filter(Boolean);

    if (menuToggle && navLinks) {
      menuToggle.addEventListener('click', () => {
        const isOpen = navLinks.classList.toggle('open');
        menuToggle.setAttribute('aria-expanded', String(isOpen));
      });

      navLinks.querySelectorAll('a').forEach((link) => {
        link.addEventListener('click', () => {
          navLinks.classList.remove('open');
          menuToggle.setAttribute('aria-expanded', 'false');
        });
      });
    }

    document.addEventListener('scroll', () => {
      if (navbar) navbar.classList.toggle('is-scrolled', window.scrollY > 10);

      if (sections.length) {
        let current = null;
        sections.forEach((section) => {
          if (section.getBoundingClientRect().top <= 120) current = section;
        });

        if (current) {
          sectionLinks.forEach((link) => {
            link.classList.toggle('active', link.getAttribute('href') === `#${current.id}`);
          });
        }
      }
    }, { passive: true });
  }

  return { init };
})();
