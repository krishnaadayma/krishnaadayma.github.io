/**
 * ==================================================================================
 *  MAIN APPLICATION SCRIPT (main.js) - DEFINITIVE VERSION 2.0
 * ==================================================================================
 *  This version includes the final correction for the news feed display.
 *  It correctly targets the title element to show the live indicator and handles
 *  all data fetching from the local 'news.json' file.
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

    async function initializeNewsFeed() {
        const insightsContainer = document.getElementById('insights-container');
        const liveIndicator = document.getElementById('live-indicator');
        const insightsTitle = document.getElementById('insights-title');

        if (!insightsContainer || !liveIndicator || !insightsTitle) {
            console.error('A required news feed element was not found.');
            return;
        }

        const newsFileUrl = `news.json?v=${new Date().getTime()}`;

        try {
            const response = await fetch(newsFileUrl);
            if (!response.ok) {
                throw new Error(`Network response was not ok. Status: ${response.status}`);
            }
            
            const allItems = await response.json();
            if (!Array.isArray(allItems) || allItems.length === 0) {
                throw new Error('news.json file is empty, invalid, or not an array.');
            }

            const articlesToDisplay = allItems.slice(0, 4);
            
            insightsContainer.innerHTML = ''; // Clear the "Accessing..." or "Unavailable" message
            
            // --- DEFINITIVE FIX ---
            // The title and live indicator are updated here, in the success path.
            insightsTitle.textContent = "Bilateral Economic Intelligence";
            liveIndicator.style.display = 'inline-block';

            const observer = new IntersectionObserver(entries => {
                entries.forEach(e => {
                    if (e.isIntersecting) {
                        e.target.classList.add('visible');
                        observer.unobserve(e.target);
                    }
                });
            }, { threshold: 0.2 });

            articlesToDisplay.forEach(item => {
                const articleCard = document.createElement('div');
                articleCard.className = 'card fade-in';
                articleCard.style.padding = 'var(--space-md)';
                
                const title = item.title || "Untitled Article";
                const source = item.author || "Google News";
                const link = item.link || "#";

                articleCard.innerHTML = `<h4><a href="${link}" target="_blank" rel="noopener noreferrer" style="color: var(--text-primary); text-decoration: none; font-size: 1rem;">${title}</a></h4><p style="font-size: 0.8rem; margin-bottom: 0;">Source: ${source}</p>`;
                insightsContainer.appendChild(articleCard);
                observer.observe(articleCard);
            });

        } catch (error) {
            console.error('Failed to initialize news feed from news.json:', error);
            // This is the fallback state if the fetch fails for any reason.
            insightsTitle.textContent = "Intelligence Feed";
            liveIndicator.style.display = 'none';
            insightsContainer.innerHTML = '<p style="text-align:left; grid-column: 1 / -1;">Live feed is currently unavailable.</p>';
        }
    }

    function initializeParticles() {
        if (typeof particlesJS !== 'undefined') {
            particlesJS('particles-js', {"particles":{"number":{"value":60,"density":{"enable":true,"value_area":800}},"color":{"value":"#A0A0A0"},"shape":{"type":"circle"},"opacity":{"value":0.4,"random":true},"size":{"value":2,"random":true},"line_linked":{"enable":true,"distance":150,"color":"#4a5568","opacity":0.2,"width":1},"move":{"enable":true,"speed":1}},"interactivity":{"events":{"onhover":{"enable":true,"mode":"grab"}}},"retina_detect":true});
        }
    }

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

    initializeUI();
    initializeScrollObserver();
    initializeNewsFeed();
    initializeParticles();
    initializeGlobe();
}

window.onload = () => {
    setTimeout(runPageScripts, 500);
};
