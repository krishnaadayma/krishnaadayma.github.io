/* ==================================================================================
   PARTICLES-INIT.JS - Particles.js Background Effect
   ================================================================================== */

function initializeParticles() {
    if (!CONFIG.FEATURES.particles) return;
    
    const container = document.getElementById('particles-js');
    if (!container || typeof particlesJS === 'undefined') {
        console.warn('Particles.js not available');
        return;
    }
    
    particlesJS('particles-js', {
        particles: {
            number: { 
                value: CONFIG.PARTICLES.count, 
                density: { enable: true, value_area: 800 } 
            },
            color: { value: CONFIG.PARTICLES.color },
            shape: { type: 'circle' },
            opacity: { 
                value: 0.5, 
                random: true,
                anim: { enable: true, speed: 1, opacity_min: 0.1, sync: false }
            },
            size: { 
                value: 3, 
                random: true 
            },
            line_linked: { 
                enable: true, 
                distance: 150, 
                color: CONFIG.PARTICLES.lineColor, 
                opacity: 0.4, 
                width: 1 
            },
            move: { 
                enable: true, 
                speed: CONFIG.PARTICLES.speed, 
                direction: 'none', 
                random: true, 
                straight: false,
                out_mode: 'out'
            }
        },
        interactivity: {
            detect_on: 'canvas',
            events: { 
                onhover: { enable: true, mode: 'grab' }, 
                onclick: { enable: true, mode: 'push' },
                resize: true 
            },
            modes: { 
                grab: { distance: 140, line_linked: { opacity: 0.8 } },
                push: { particles_nb: 4 }
            }
        },
        retina_detect: true
    });
    
    console.log('✓ Particles initialized');
}
