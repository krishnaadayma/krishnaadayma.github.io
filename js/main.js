/* ==================================================================================
   MAIN.JS - Application Orchestrator
   Imports and initializes all modules
   ================================================================================== */

function initializeApp() {
    console.log('🚀 Initializing Portfolio...');
    
    // Core UI
    initializeUI();
    
    // Scroll animations
    initializeScrollObserver();
    
    // Live news feed
    initializeNewsFeed();
    
    // Visual effects
    initializeParticles();
    initializeGlobe();
    
    console.log('✅ Portfolio ready!');
}

// Start application when DOM is ready
window.addEventListener('load', () => {
    setTimeout(initializeApp, CONFIG.ANIMATION.fadeDelay);
});
