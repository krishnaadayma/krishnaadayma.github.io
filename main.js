/**
 * ==================================================================================
 *  MAIN APPLICATION SCRIPT (main.js) - TRULY CORRECTED VERSION
 * ==================================================================================
 *  This version restores the code that was incorrectly deleted in the previous
 *  version. It will now correctly orchestrate all page logic and animations.
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
        const btnEN = document.querySelector('.lang-en');
        const btnIT = document.querySelector('.lang-it');
        if (btnEN) btnEN.addEventListener('click', () => window.setLanguage('en'));
        if (btnIT) btnIT.addEventListener('click', () => window.setLanguage('it'));
        
        let currentLanguage = 'en';
        const googleTranslateCookie = document.cookie.split('; ').find(row => row.startsWith('googtrans='));
        if (googleTranslateCookie) { 
            currentLanguage = googleTranslateCookie.split('/')[2]; 
        }
        
        document.querySelectorAll('#custom-translate-widget a').forEach(el => el.classList.remove('active'));
        const activeLanguageElement = document.querySelector(`.lang-${currentLanguage}`);
        if (activeLanguageElement) { 
            activeLanguageElement.classList.add('active'); 
        }
    }

    function initializeScrollObserver() {
        const observerOptions = { threshold: 0.2 };
        const observerCallback = (entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    if (entry.target.matches('.language-item')) {
                        const progressBar = entry.target.querySelector('.progress-bar');
                        if (progressBar) progressBar.style.width = progressBar.dataset.width;
                    }
                    observer.unobserve(entry.target);
                }
            });
        };
        const observer = new IntersectionObserver(observerCallback, observerOptions);
        document.querySelectorAll('.fade-in, .skills-grid .card, .language-item').forEach(el => observer.observe(el));
    }

    async function initializeNewsFeed() {
        const insightsContainer = document.getElementById('insights-container');
        const liveIndicator = document.getElementById('live-indicator');
        const insightsTitle = document.getElementById('insights-title');
        if (!insightsContainer || !liveIndicator || !insightsTitle) return;

        const newsFileUrl = `news.json?v=${new Date().getTime()}`;
        try {
            const response = await fetch(newsFileUrl);
            if (!response.ok) throw new Error(`Network error: ${response.status}`);
            
            const allItems = await response.json();
            if (!Array.isArray(allItems) || allItems.length === 0) throw new Error('News file is empty or invalid.');
            
            const articlesToDisplay = allItems.slice(0, 4);
            insightsContainer.innerHTML = '';
            insightsTitle.textContent = "Bilateral Economic Intelligence";
            liveIndicator.style.display = 'inline-block';
            
            articlesToDisplay.forEach(item => {
                const articleCard = document.createElement('div');
                articleCard.className = 'card fade-in';
                articleCard.style.padding = 'var(--space-md)';
                const title = item.title || "Untitled Article";
                const source = item.author || "Google News";
                const link = item.link || "#";
                articleCard.innerHTML = `<h4><a href="${link}" target="_blank" rel="noopener noreferrer" style="color: var(--text-primary); text-decoration: none; font-size: 1rem;">${title}</a></h4><p style="font-size: 0.8rem; margin-bottom: 0;">Source: ${source}</p>`;
                insightsContainer.appendChild(articleCard);
            });
        } catch (error) {
            console.error('News feed init failed:', error);
            insightsTitle.textContent = "Intelligence Feed";
            liveIndicator.style.display = 'none';
            insightsContainer.innerHTML = '<p style="text-align:left; grid-column: 1 / -1;">Live feed is currently unavailable.</p>';
        }
    }

    // --- ORCHESTRATION ---
    initializeUI();
    initializeScrollObserver();
    initializeNewsFeed();
    
    if (typeof runAdvancedAnimations === 'function') {
        runAdvancedAnimations();
    } else {
        console.error("Advanced animations script ('animations.js') not found or failed to load.");
    }
}

window.onload = () => {
    setTimeout(runPageScripts, 500);
};
