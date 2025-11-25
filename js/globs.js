/* ==================================================================================
   GLOBE.JS - Three.js 3D Rotating Globe
   ================================================================================== */

function initializeGlobe() {
    if (!CONFIG.FEATURES.globe) return;
    
    const canvas = document.getElementById('globe-canvas');
    if (!canvas || typeof THREE === 'undefined') {
        console.warn('Three.js or globe canvas not available');
        return;
    }
    
    // Scene setup
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ 
        canvas: canvas, 
        alpha: true, 
        antialias: true 
    });
    
    renderer.setSize(350, 350);
    renderer.setPixelRatio(window.devicePixelRatio);
    
    // Main globe
    const globeGeometry = new THREE.SphereGeometry(1.8, 32, 32);
    const globeMaterial = new THREE.MeshBasicMaterial({ 
        color: CONFIG.GLOBE.color, 
        wireframe: true, 
        transparent: true, 
        opacity: CONFIG.GLOBE.opacity 
    });
    const globe = new THREE.Mesh(globeGeometry, globeMaterial);
    scene.add(globe);
    
    // Inner glow effect
    const glowGeometry = new THREE.SphereGeometry(1.5, 32, 32);
    const glowMaterial = new THREE.MeshBasicMaterial({ 
        color: 0x4a5568, 
        wireframe: true, 
        transparent: true, 
        opacity: 0.1 
    });
    const innerGlow = new THREE.Mesh(glowGeometry, glowMaterial);
    scene.add(innerGlow);
    
    camera.position.z = 4;
    
    // Animation loop
    function animate() {
        requestAnimationFrame(animate);
        globe.rotation.y += CONFIG.GLOBE.rotationSpeed;
        globe.rotation.x += CONFIG.GLOBE.rotationSpeed / 4;
        innerGlow.rotation.y -= CONFIG.GLOBE.rotationSpeed / 2;
        renderer.render(scene, camera);
    }
    animate();
    
    // Handle resize
    window.addEventListener('resize', () => {
        const size = Math.min(350, window.innerWidth * 0.8);
        renderer.setSize(size, size);
    });
    
    console.log('✓ 3D Globe initialized');
}
