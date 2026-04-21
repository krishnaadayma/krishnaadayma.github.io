window.ContactForm = (() => {
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  function setMessage(el, text, type) {
    if (!el) return;
    el.textContent = text;
    el.className = type ? type : '';
  }

  function init() {
    const form = document.getElementById('contact-form');
    const message = document.getElementById('form-message');
    if (!form) return;

    form.addEventListener('submit', (event) => {
      event.preventDefault();
      const formData = new FormData(form);
      const name = String(formData.get('name') || '').trim();
      const email = String(formData.get('email') || '').trim();
      const text = String(formData.get('message') || '').trim();

      if (!name || !email || !text) {
        setMessage(message, 'Please complete all fields.', 'error');
        return;
      }

      if (!emailPattern.test(email)) {
        setMessage(message, 'Please enter a valid email address.', 'error');
        return;
      }

      setMessage(message, 'Message sent successfully. Thank you!', 'success');
      form.reset();
    });
  }

  return { init };
})();
