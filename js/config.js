/* ==================================================================================
   CONFIG.JS - Global Configuration & Constants
   ================================================================================== */

const CONFIG = {
    // API Endpoints
    NEWS_FILE: 'data/news.json',
    
    // Feature Flags
    FEATURES: {
        particles: true,
        globe: true,
        newsFeed: true,
        animations: true
    },
    
    // Animation Settings
    ANIMATION: {
        scrollThreshold: 0.2,
        fadeDelay: 300
    },
    
    // Particles Settings
    PARTICLES: {
        count: 80,
        color: '#A0A0A0',
        lineColor: '#4a5568',
        speed: 2
    },
    
    // Globe Settings
    GLOBE: {
        color: 0xA0A0A0,
        opacity: 0.25,
        rotationSpeed: 0.002
    },
    
    // News Feed Settings
    NEWS: {
        maxArticles: 4,
        refreshInterval: 300000 // 5 minutes
    }
};

// Freeze config to prevent modifications
Object.freeze(CONFIG);
Object.freeze(CONFIG.FEATURES);
Object.freeze(CONFIG.ANIMATION);
Object.freeze(CONFIG.PARTICLES);
Object.freeze(CONFIG.GLOBE);
Object.freeze(CONFIG.NEWS);
