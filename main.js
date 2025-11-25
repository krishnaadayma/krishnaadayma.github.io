/**
 * ==================================================================================
 *  MAIN APPLICATION SCRIPT - Complete Version
 * ==================================================================================
 */

window.setLanguage = function(lang) {
    document.cookie = `googtrans=/en/${lang};path=/`;
    window.location.reload();
};

function googleTranslateElementInit() {
    new google.translate.TranslateElement({ pageLanguage: 'en' }, 'google_translate_element');
}

function runPageScripts() {

    // --- UI Initialization ---
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

    // --- Scroll Animations ---
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

    // --- Live News Feed ---
    async function initializeNewsFeed() {
        const insightsContainer = document.getElementById('insights-container');
        const liveIndicator = document.getElementById('live-indicator');
        const insightsTitle = document.getElementById('insights-title');
        
        if (!insightsContainer || !liveIndicator || !insightsTitle) {
            console.log('News feed elements not found on this page.');
            return;
        }

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
                articleCard.innerHTML = `
                    <h4><a href="${link}" target="_blank" rel="noopener noreferrer" style="color: var(--text-primary); text-decoration: none; font-size: 1rem;">${title}</a></h4>
                    <p style="color: var(--text-muted); font-size: 0.85rem; margin-top: 0.5rem;">Source: ${source}</p>
                `;
                insightsContainer.appendChild(articleCard);
                observer.observe(articleCard);
            });
        } catch (error) {
            console.error('News feed init failed:', error);
            insightsTitle.textContent = "Intelligence Feed";
            liveIndicator.style.display = 'none';
            insightsContainer.innerHTML = '<p style="text-align: center; grid-column: 1 / -1; color: var(--text-muted);">Live feed is currently unavailable.</p>';
        }
    }

    // --- Particles.js Background ---
    function initializeParticles() {
        if (typeof particlesJS !== 'undefined' && document.getElementById('particles-js')) {
            particlesJS('particles-js', {
                particles: {
                    number: { value: 60, density: { enable: true, value_area: 800 } },
                    color: { value: "#A0A0A0" },
                    shape: { type: "circle" },
                    opacity: { value: 0.4, random: true },
                    size: { value: 2, random: true },
                    line_linked: { enable: true, distance: 150, color: "#4a5568", opacity: 0.3, width: 1 },
                    move: { enable: true, speed: 1, direction: "none", random: true, out_mode: "out" }
                },
                interactivity: {
                    detect_on: "canvas",
                    events: { onhover: { enable: true, mode: "grab" }, resize: true },
                    modes: { grab: { distance: 140, line_linked: { opacity: 0.6 } } }
                },
                retina_detect: true
            });
        }
    }

    // --- 3D Globe ---
    function initializeGlobe() {
        const globeCanvas = document.getElementById('globe-canvas');
        if (globeCanvas && typeof THREE !== 'undefined') {
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({ canvas: globeCanvas, alpha: true, antialias: true });
            renderer.setSize(300, 300);
            
            const globe = new THREE.Mesh(
                new THREE.SphereGeometry(1.5, 32, 32), 
                new THREE.MeshBasicMaterial({ color: 0xA0A0A0, wireframe: true, transparent: true, opacity: 0.3 })
            );
            scene.add(globe);
            camera.position.z = 3.5;

            function animate() {
                requestAnimationFrame(animate);
                globe.rotation.y += 0.002;
                renderer.render(scene, camera);
            }
            animate();
        }
    }

    // --- Run All Initializations ---
    initializeUI();
    initializeScrollObserver();
    initializeNewsFeed();
    initializeParticles();
    initializeGlobe();
}

window.onload = () => {
    setTimeout(runPageScripts, 300);
};
