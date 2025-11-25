/**
 * ==================================================================================
 *  MAIN APPLICATION SCRIPT (main.js) - HEAVY ANIMATION ORCHESTRATOR
 * ==================================================================================
 *  This file handles core page logic and now calls the 'animations.js' script
 *  to run all the advanced visual effects, keeping the codebase clean.
 */

window.setLanguage = function(lang) {
    document.cookie = `googtrans=/en/${lang};path=/`;
    window.location.reload();
};

function googleTranslateElementInit() {
    new google.translate.TranslateElement({ pageLanguage: 'en' }, 'google_translate_element');
}

function runPageScripts() {

    function initializeUI() {
        // ... (UI initialization code remains the same)
    }

    function initializeScrollObserver() {
        const observerOptions = { threshold: 0.2 };
        const observerCallback = (entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    // Handle progress bars
                    if (entry.target.matches('.language-item')) {
                        const progressBar = entry.target.querySelector('.progress-bar');
                        if (progressBar) progressBar.style.width = progressBar.dataset.width;
                    }
                    observer.unobserve(entry.target);
                }
            });
        };
        const observer = new IntersectionObserver(observerCallback, observerOptions);
        // Observe all .fade-in elements AND the new skills-grid cards
        document.querySelectorAll('.fade-in, .skills-grid .card, .language-item').forEach(el => observer.observe(el));
    }

    async function initializeNewsFeed() {
        // ... (News feed logic remains the same)
    }

    // --- ORCHESTRATION ---
    initializeUI();
    initializeScrollObserver();
    initializeNewsFeed();
    
    // **NEW:** Run all the heavy animations from the dedicated script
    if (typeof runAdvancedAnimations === 'function') {
        runAdvancedAnimations();
    } else {
        console.error("Advanced animations script not found.");
    }
}

window.onload = () => {
    // Add a specific class to the skills grid to target the 3D animation
    const skillsGrid = document.querySelector('#skills .grid-container');
    if (skillsGrid) {
        skillsGrid.classList.add('skills-grid');
    }
    setTimeout(runPageScripts, 500);
};
