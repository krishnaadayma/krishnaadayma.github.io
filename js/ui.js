/* ==================================================================================
   UI.JS - User Interface Interactions
   ================================================================================== */

function initializeUI() {
    // Language toggle buttons
    const btnEN = document.querySelector('.lang-en');
    const btnIT = document.querySelector('.lang-it');
    
    if (btnEN) {
        btnEN.addEventListener('click', () => window.setLanguage('en'));
    }
    if (btnIT) {
        btnIT.addEventListener('click', () => window.setLanguage('it'));
    }
    
    // Highlight active language
    const currentLanguage = getCurrentLanguage();
    document.querySelectorAll('#custom-translate-widget a').forEach(el => {
        el.classList.remove('active');
    });
    
    const activeEl = document.querySelector(`.lang-${currentLanguage}`);
    if (activeEl) {
        activeEl.classList.add('active');
    }
    
    console.log('✓ UI initialized');
}
