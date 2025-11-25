/* ==================================================================================
   TRANSLATE.JS - Google Translate & Language Toggle
   ================================================================================== */

// Set language cookie and reload
window.setLanguage = function(lang) {
    document.cookie = `googtrans=/en/${lang};path=/`;
    window.location.reload();
};

// Google Translate initialization callback
function googleTranslateElementInit() {
    new google.translate.TranslateElement({ 
        pageLanguage: 'en' 
    }, 'google_translate_element');
}

// Get current language from cookie
function getCurrentLanguage() {
    const cookie = document.cookie
        .split('; ')
        .find(row => row.startsWith('googtrans='));
    
    if (cookie) {
        const parts = cookie.split('/');
        return parts[2] || 'en';
    }
    return 'en';
}
