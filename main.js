/**
 * ==================================================================================
 *  MAIN APPLICATION SCRIPT (main.js)
 * ==================================================================================
 *  This file contains all the dynamic functionality for the portfolio page,
 *  including animations, the live news feed, and scroll-triggered events.
 *  It is loaded by index.html to keep the main file clean and organized.
 */

/**
 * This is the master function that runs all page-specific scripts.
 * It is designed to run only after the DOM is ready, and in the case of a delayed
 * start, it can wait for other libraries (like Google Translate) to finish.
 */
function runPageScripts() {

    /**
     * Sub-function 1: Intersection Observer Setup
     * This observer is responsible for triggering animations as elements scroll into view.
     * It handles the 'fade-in' effect and the language proficiency progress bars.
     */
    function initializeScrollObserver() {
        // Configuration for the observer: trigger when 20% of the element is visible.
        const observerOptions = {
            threshold: 0.2
        };

        // The callback function that executes when an observed element enters the viewport.
        const observerCallback = (entries) => {
            entries.forEach(entry => {
                // If the element is intersecting (i.e., visible)...
                if (entry.isIntersecting) {
                    // Add the 'visible' class to trigger the CSS fade-in animation.
                    entry.target.classList.add('visible');

                    // Check if the element is a progress bar.
                    const progressBar = entry.target.querySelector('.progress-bar');
                    if (progressBar) {
                        // If it is, set its width to the value stored in its 'data-width' attribute.
                        progressBar.style.width = progressBar.dataset.width;
                    }

                    // Once the animation is triggered, we no longer need to observe this element.
                    observer.unobserve(entry.target);
                }
            });
        };

        // Create the new IntersectionObserver.
        const observer = new IntersectionObserver(observerCallback, observerOptions);

        // Find all elements that need to be observed and start observing them.
        const elementsToAnimate = document.querySelectorAll('.fade-in, .language-item');
        elementsToAnimate.forEach(element => observer.observe(element));
    }

    /**
     * Sub-function 2: Live News Feed from RSS2JSON
     * This function fetches data from two different news feeds, combines them, sorts them by
     * date, and displays the most recent articles in the "Bilateral Economic Intelligence" card.
     */
    async function initializeNewsFeed() {
        const insightsContainer = document.getElementById('insights-container');
        const liveIndicator = document.getElementById('live-indicator');
        const insightsTitle = document.getElementById('insights-title');

        // Defensive check: If the required HTML elements don't exist, exit the function.
        if (!insightsContainer || !liveIndicator || !insightsTitle) {
            console.error("News feed elements not found. Aborting news feed initialization.");
            return;
        }

        // The base URL for the RSS-to-JSON conversion service.
        const RSS_BASE_URL = 'https://api.rss2json.com/v1/api.json?rss_url=';

        // The specific Google News RSS feeds to be fetched.
        const italyFeedUrl = `${RSS_BASE_URL}https://news.google.com/rss/search?q=italy+economy+business&hl=en-US&gl=US&ceid=US:en`;
        const indiaFeedUrl = `${RSS_BASE}https://news.google.com/rss/search?q=india+economy+business&hl=en-US&gl=US&ceid=US:en`;

        try {
            // Fetch both feeds simultaneously for better performance.
            const [italyResponse, indiaResponse] = await Promise.all([
                fetch(italyFeedUrl),
                fetch(indiaFeedUrl)
            ]);

            // Check if the network requests were successful.
            if (!italyResponse.ok || !indiaResponse.ok) {
                throw new Error('Network response was not ok.');
            }

            // Parse the JSON data from the responses.
            const italyData = await italyResponse.json();
            const indiaData = await indiaResponse.json();

            // Check if the API calls were successful.
            if (italyData.status !== 'ok' || indiaData.status !== 'ok') {
                throw new Error('RSS2JSON API status was not "ok".');
            }

            // Combine the news items from both feeds into a single array.
            const combinedItems = [...(italyData.items || []), ...(indiaData.items || [])];

            if (combinedItems.length === 0) {
                throw new Error('No news items were found from the feeds.');
            }

            // Sort the combined array by publication date, newest first.
            combinedItems.sort((a, b) => new Date(b.pubDate) - new Date(a.pubDate));

            // Clear the "loading..." message.
            insightsContainer.innerHTML = '';
            // Make the live indicator dot visible.
            liveIndicator.style.display = 'inline-block';

            // Take the 4 newest articles and display them.
            const articlesToDisplay = combinedItems.slice(0, 4);
            articlesToDisplay.forEach(item => {
                const articleCard = document.createElement('div');
                articleCard.className = 'card fade-in'; // Re-use the card and fade-in styles.
                articleCard.style.margin = '0'; // Override default card margins if necessary.

                const title = item.title ? item.title.replace(/<[^>]*>/g, "") : "Untitled Article";
                const source = item.author || "Google News";
                
                articleCard.innerHTML = `
                    <h4>
                        <a href="${item.link}" target="_blank" rel="noopener noreferrer" style="color: var(--text-primary); text-decoration: none; font-size: 1rem;">
                            ${title}
                        </a>
                    </h4>
                    <p style="font-size: 0.8rem; margin-bottom: 0;">Source: ${source}</p>
                `;
                insightsContainer.appendChild(articleCard);
            });

        } catch (error) {
            // If anything goes wrong, display an error message.
            console.error('Bilateral news feed fetch failed:', error);
            insightsTitle.textContent = "Intelligence Feed"; // Change title to reflect the error
            liveIndicator.style.display = 'none'; // Hide the live dot
            insightsContainer.innerHTML = '<p style="text-align:left; grid-column: 1 / -1;">Live intelligence feed is currently unavailable. Please check back later.</p>';
        }
    }

    /**
     * Sub-function 3: Header Particle Animation
     * Initializes the Particles.js animation in the header if the library is loaded.
     */
    function initializeParticles() {
        if (typeof particlesJS !== 'undefined') {
            particlesJS('particles-js', {
                "particles": {"number":{"value":60,"density":{"enable":true,"value_area":800}},"color":{"value":"#A0A0A0"},"shape":{"type":"circle"},"opacity":{"value":0.4,"random":true},"size":{"value":2,"random":true},"line_linked":{"enable":true,"distance":150,"color":"#4a5568","opacity":0.2,"width":1},"move":{"enable":true,"speed":1,"direction":"none","out_mode":"out"}},
                "interactivity": {"events":{"onhover":{"enable":true,"mode":"grab"}}},
                "retina_detect":true
            });
        }
    }

    /**
     * Sub-function 4: About Section Globe Animation
     * Initializes the Three.js rotating wireframe globe if the library is loaded.
     */
    function initializeGlobe() {
        const globeCanvas = document.getElementById('globe-canvas');
        if (globeCanvas && typeof THREE !== 'undefined') {
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({ canvas: globeCanvas, alpha: true });
            const globe = new THREE.Mesh(new THREE.SphereGeometry(1.5, 32, 32), new THREE.MeshBasicMaterial({ color: 0xA0A0A0, wireframe: true }));
            scene.add(globe);
            camera.position.z = 2.5;

            function animate() {
                requestAnimationFrame(animate);
                globe.rotation.y += 0.001; // Slow rotation
                renderer.render(scene, camera);
            }
            animate();

            // Make the globe responsive to the size of its container.
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

    /**
     * Sub-function 5: Set Active Language in UI
     * Reads the Google Translate cookie and applies the 'active' class to the button.
     */
    function highlightActiveLanguage() {
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
    
    // --- MASTER EXECUTION BLOCK ---
    // Calls all the necessary sub-functions in order.
    highlightActiveLanguage();
    initializeScrollObserver();
    initializeNewsFeed();
    initializeParticles();
    initializeGlobe();
}

// --- GLOBAL INITIALIZER ---
// This is the single entry point. It waits for the window to be fully loaded, then
// waits an additional 500ms for maximum stability before running the scripts.
// This definitively solves all animation conflicts with Google Translate.
window.onload = () => {
    setTimeout(runPageScripts, 500);
};
