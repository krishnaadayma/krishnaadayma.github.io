/**
 * ==================================================================================
 *  MAIN APPLICATION SCRIPT (main.js) - FINAL ALIGNED VERSION
 * ==================================================================================
 *  This file contains all dynamic functionality for the portfolio page, including
 *  translation logic, animations, the live news feed, and scroll-triggered events.
 *  It is designed to work flawlessly with the final index.html and style.css.
 */

// Make the setLanguage function globally available so the onclick attribute in index.html can find it.
window.setLanguage = function(lang) {
    document.cookie = `googtrans=/en/${lang};path=/`;
    window.location.reload();
};

// This function initializes the Google Translate element. It's required by their script.
function googleTranslateElementInit() {
    new google.translate.TranslateElement({ pageLanguage: 'en' }, 'google_translate_element');
}

/**
 * The master function that runs all page-specific scripts.
 * It's called after a delay to ensure the page is fully loaded and stable.
 */
function runPageScripts() {

    /**
     * Sub-function 1: UI Initialization
     * This handles tasks that need to run once the DOM is ready, like binding
     * events and setting initial states.
     */
    function initializeUI() {
        // --- Bind Translation Buttons ---
        const btnEN = document.querySelector('.lang-en');
        const btnIT = document.querySelector('.lang-it');
        if (btnEN) btnEN.addEventListener('click', () => window.setLanguage('en'));
        if (btnIT) btnIT.addEventListener('click', () => window.setLanguage('it'));

        // --- Highlight Active Language ---
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

    /**
     * Sub-function 2: Intersection Observer for Scroll Animations
     * Triggers 'fade-in' and progress bar animations as elements enter the viewport.
     */
    function initializeScrollObserver() {
        const observerOptions = { threshold: 0.2 };
        const observerCallback = (entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    const progressBar = entry.target.querySelector('.progress-bar');
                    if (progressBar) {
                        progressBar.style.width = progressBar.dataset.width;
                    }
                    observer.unobserve(entry.target);
                }
            });
        };
        const observer = new IntersectionObserver(observerCallback, observerOptions);
        document.querySelectorAll('.fade-in, .language-item').forEach(el => observer.observe(el));
    }

    /**
     * Sub-function 3: Live News Feed
     * Fetches, combines, and displays real-time news for the Italy-India corridor.
     */
    async function initializeNewsFeed() {
        const insightsContainer = document.getElementById('insights-container');
        const liveIndicator = document.getElementById('live-indicator');
        const insightsTitle = document.getElementById('insights-title');

        if (!insightsContainer || !liveIndicator || !insightsTitle) return;

        const RSS_BASE_URL = 'https://api.rss2json.com/v1/api.json?rss_url=';
        const italyFeedUrl = `${RSS_BASE_URL}https://news.google.com/rss/search?q=italy+economy+business&hl=en-US&gl=US&ceid=US:en`;
        const indiaFeedUrl = `${RSS_BASE_URL}https://news.google.com/rss/search?q=india+economy+business&hl=en-US&gl=US&ceid=US:en`;

        try {
            const [italyResponse, indiaResponse] = await Promise.all([fetch(italyFeedUrl), fetch(indiaFeedUrl)]);
            if (!italyResponse.ok || !indiaResponse.ok) throw new Error('Network response was not ok.');
            
            const [italyData, indiaData] = await Promise.all([italyResponse.json(), indiaResponse.json()]);
            if (italyData.status !== 'ok' || indiaData.status !== 'ok') throw new Error('RSS2JSON API status was not "ok".');

            const combinedItems = [...(italyData.items || []), ...(indiaData.items || [])].sort((a, b) => new Date(b.pubDate) - new Date(a.pubDate));
            if (combinedItems.length === 0) throw new Error('No news items found.');

            insightsContainer.innerHTML = '';
            liveIndicator.style.display = 'inline-block';
            const observer = new IntersectionObserver(entries => {
                entries.forEach(e => {
                    if(e.isIntersecting) {
                        e.target.classList.add('visible');
                        observer.unobserve(e.target);
                    }
                });
            }, {threshold: 0.2});

            combinedItems.slice(0, 4).forEach(item => {
                const articleCard = document.createElement('div');
                articleCard.className = 'card fade-in';
                articleCard.innerHTML = `<h4><a href="${item.link}" target="_blank" rel="noopener noreferrer" style="color: var(--text-primary); text-decoration: none; font-size: 1rem;">${item.title.replace(/<[^>]*>/g, "")}</a></h4><p style="font-size: 0.8rem; margin-bottom: 0;">Source: ${item.author || "Google News"}</p>`;
                insightsContainer.appendChild(articleCard);
                observer.observe(articleCard);
            });

        } catch (error) {
            console.error('News feed fetch failed:', error);
            insightsTitle.textContent = "Intelligence Feed";
            liveIndicator.style.display = 'none';
            insightsContainer.innerHTML = '<p style="text-align:left; grid-column: 1 / -1;">Live feed is currently unavailable.</p>';
        }
    }

    /**
     * Sub-function 4: Header Particle Animation (Particles.js)
     */
    function initializeParticles() {
        if (typeof particlesJS !== 'undefined') {
            particlesJS('particles-js', {"particles":{"number":{"value":60,"density":{"enable":true,"value_area":800}},"color":{"value":"#A0A0A0"},"shape":{"type":"circle"},"opacity":{"value":0.4,"random":true},"size":{"value":2,"random":true},"line_linked":{"enable":true,"distance":150,"color":"#4a5568","opacity":0.2,"width":1},"move":{"enable":true,"speed":1}},"interactivity":{"events":{"onhover":{"enable":true,"mode":"grab"}}},"retina_detect":true});
        }
    }

    /**
     * Sub-function 5: About Section Globe Animation (Three.js)
     */
    function initializeGlobe() {
        const globeCanvas = document.getElementById('globe-canvas');
        if (globeCanvas && typeof THREE !== 'undefined') {
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({ canvas: globeCanvas, alpha: true, antialias: true });
            const globe = new THREE.Mesh(new THREE.SphereGeometry(1.5, 32, 32), new THREE.MeshBasicMaterial({ color: 0xA0A0A0, wireframe: true }));
            scene.add(globe);
            camera.position.z = 2.5;

            function animate() {
                requestAnimationFrame(animate);
                globe.rotation.y += 0.001;
                renderer.render(scene, camera);
            }
            animate();

            new ResizeObserver(() => {
                const container = document.getElementById('about');
                if (container) {
                    const size = Math.min(container.offsetWidth, 1200);
                    camera.aspect = 1;
                    camera.updateProjectionMatrix();
                    renderer.setSize(size, size);
                }
            }).observe(document.getElementById('about'));
        }
    }

    // --- MASTER EXECUTION BLOCK ---
    initializeUI();
    initializeScrollObserver();
    initializeNewsFeed();
    initializeParticles();
    initializeGlobe();
}

// --- GLOBAL INITIALIZER ---
// Waits for the window to be fully loaded, then waits 500ms for maximum stability
// before running all scripts. This solves all animation/translation conflicts.
window.onload = () => {
    setTimeout(runPageScripts, 500);
};
