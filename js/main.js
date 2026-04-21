document.addEventListener('DOMContentLoaded', () => {
  if (window.Navbar) window.Navbar.init();
  if (window.Animations) window.Animations.init();
  if (window.ContactForm) window.ContactForm.init();

  const langCookie = document.cookie.split('; ').find(row => row.startsWith('googtrans='));
  const lang = langCookie ? langCookie.split('/')[2] : 'en';
  const active = document.querySelector(`.lang-${lang}`);
  if (active) active.classList.add('active');
});
