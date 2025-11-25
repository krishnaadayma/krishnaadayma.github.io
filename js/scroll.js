/* ==================================================================================
   SCROLL.JS - Scroll Observer & Animations
   ================================================================================== */

function initializeScrollObserver() {
    if (!CONFIG.FEATURES.animations) return;
    
    const observerOptions = { 
        threshold: CONFIG.ANIMATION.scrollThreshold 
    };
    
    const observerCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                
                // Animate progress bars for language items
                if (entry.target.matches('.language-item')) {
                    const progressBar = entry.target.querySelector('.progress-bar');
                    if (progressBar) {
                        progressBar.style.width = progressBar.dataset.width;
                    }
                }
                
                observer.unobserve(entry.target);
            }
        });
    };
    
    const observer = new IntersectionObserver(observerCallback, observerOptions);
    
    // Observe all animated elements
    const animatedElements = document.querySelectorAll(
        '.fade-in, .skills-grid .card, .language-item'
    );
    
    animatedElements.forEach(el => observer.observe(el));
    
    console.log(`✓ Scroll observer watching ${animatedElements.length} elements`);
}
