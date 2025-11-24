<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>International Trade Compliance System | Krishna Dayma</title>
    <meta name="description" content="Python application analyzing trade regulations between Italy and India with comprehensive compliance data and interactive analytics.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
    /* ===== OPTIMIZED CSS FOR TRADE COMPLIANCE ===== */
    :root {
        /* Color system */
        --bg-primary: #0a0a0a;
        --bg-secondary: #1a1a1a;
        --bg-tertiary: #2d2d2d;
        --text-primary: #ffffff;
        --text-secondary: #e0e0e0;
        --text-muted: #b0b0b0;
        --accent-primary: #007acc;
        --accent-secondary: #28a745;
        --accent-warning: #ff6b35;
        --accent-portfolio: #6c757d;
        --border-color: #333;
        --gradient-primary: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        --gradient-accent: linear-gradient(135deg, #007acc 0%, #005a9e 100%);
        
        /* Typography scale */
        --text-xs: clamp(0.75rem, 2vw, 0.875rem);
        --text-sm: clamp(0.875rem, 2.5vw, 1rem);
        --text-base: clamp(1rem, 3vw, 1.125rem);
        --text-lg: clamp(1.125rem, 3.5vw, 1.25rem);
        --text-xl: clamp(1.25rem, 4vw, 1.5rem);
        --text-2xl: clamp(1.5rem, 5vw, 1.875rem);
        --text-3xl: clamp(1.875rem, 6vw, 2.25rem);
        
        /* Spacing scale */
        --space-xs: clamp(0.5rem, 1vw, 0.75rem);
        --space-sm: clamp(0.75rem, 2vw, 1rem);
        --space-md: clamp(1rem, 3vw, 1.5rem);
        --space-lg: clamp(1.5rem, 4vw, 2rem);
        --space-xl: clamp(2rem, 6vw, 3rem);
        --space-2xl: clamp(3rem, 8vw, 4rem);
        
        /* Border radius */
        --radius-sm: 0.375rem;
        --radius-md: 0.5rem;
        --radius-lg: 0.75rem;
        --radius-xl: 1rem;
        
        /* Animation */
        --transition-fast: 0.2s ease;
        --transition-medium: 0.3s ease;
        --transition-slow: 0.5s ease;
        --shadow-glow: 0 0 20px rgba(0, 122, 204, 0.3);
    }

    /* Reset and base styles */
    *, *::before, *::after {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    html {
        scroll-behavior: smooth;
    }

    body {
        font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        line-height: 1.6;
        color: var(--text-secondary);
        background-color: var(--bg-primary);
        overflow-x: hidden;
    }

    /* Container system */
    .container {
        width: 100%;
        max-width: min(1200px, 95vw);
        margin: 0 auto;
        padding: 0 var(--space-md);
    }

    /* Typography */
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-primary);
        line-height: 1.2;
        font-weight: 700;
        margin-bottom: var(--space-sm);
    }

    h1 { 
        font-size: var(--text-3xl);
        text-align: center;
    }

    h2 { 
        font-size: var(--text-2xl);
        margin-bottom: var(--space-md);
    }

    h3 { 
        font-size: var(--text-xl);
    }

    p {
        color: var(--text-muted);
        margin-bottom: var(--space-sm);
        line-height: 1.6;
        font-size: var(--text-base);
        max-width: 65ch;
    }

    .subtitle {
        font-size: var(--text-lg);
        color: var(--text-muted);
        margin-bottom: var(--space-md);
    }

    /* Header */
    header {
        background: var(--gradient-primary);
        color: var(--text-primary);
        padding: var(--space-2xl) var(--space-md);
        text-align: center;
        border-radius: var(--radius-xl);
        margin-bottom: var(--space-xl);
        position: relative;
        overflow: hidden;
        border: 1px solid var(--border-color);
    }

    .header-content h1 {
        animation: fadeInUp 0.8s ease-out;
    }

    .header-content .subtitle {
        animation: fadeInUp 0.8s ease-out 0.2s both;
    }

    .header-content .tech-tags {
        animation: fadeInUp 0.8s ease-out 0.4s both;
    }

    /* Button system */
    .btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: var(--space-xs);
        background: var(--bg-tertiary);
        color: var(--text-primary);
        padding: var(--space-sm) var(--space-lg);
        text-decoration: none;
        border-radius: var(--radius-md);
        font-weight: 600;
        font-size: var(--text-base);
        border: 1px solid var(--border-color);
        transition: all var(--transition-fast);
        cursor: pointer;
        margin: var(--space-xs);
        text-align: center;
        position: relative;
        overflow: hidden;
    }

    .btn::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        transition: left var(--transition-medium);
    }

    .btn:hover::before {
        left: 100%;
    }

    .btn:hover,
    .btn:focus {
        background: #404040;
        transform: translateY(-2px);
    }

    .btn-primary {
        background: var(--gradient-accent);
        border-color: var(--accent-primary);
    }

    .btn-primary:hover,
    .btn-primary:focus {
        background: #005a9e;
        border-color: #005a9e;
        box-shadow: var(--shadow-glow);
    }

    .btn-secondary {
        background: var(--accent-secondary);
        border-color: var(--accent-secondary);
    }

    .btn-secondary:hover,
    .btn-secondary:focus {
        background: #1e7e34;
        border-color: #1e7e34;
    }

    .btn-warning {
        background: linear-gradient(135deg, var(--accent-warning), #e53e3e);
        border-color: var(--accent-warning);
        color: white;
    }

    .btn-warning:hover,
    .btn-warning:focus {
        background: linear-gradient(135deg, #e55a25, #c53030);
        border-color: #e55a25;
        box-shadow: 0 0 20px rgba(255, 107, 53, 0.4);
    }

    .btn-portfolio {
        background: var(--accent-portfolio);
        border-color: var(--accent-portfolio);
        color: white;
    }

    .btn-portfolio:hover,
    .btn-portfolio:focus {
        background: #545b62;
        border-color: #545b62;
    }

    /* Tech tags */
    .tech-tags {
        margin: var(--space-lg) 0;
    }

    .tech-tag {
        background: var(--accent-primary);
        padding: var(--space-xs) var(--space-sm);
        border-radius: 12px;
        font-size: var(--text-xs);
        margin-right: var(--space-sm);
        color: white;
        display: inline-block;
        transition: transform var(--transition-fast);
    }

    .tech-tag:hover {
        transform: scale(1.05);
    }

    /* Feature grid */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(min(280px, 100%), 1fr));
        gap: var(--space-lg);
        margin: var(--space-xl) 0;
    }

    .feature-card {
        background: var(--bg-secondary);
        padding: var(--space-lg);
        border-radius: var(--radius-lg);
        text-align: center;
        border: 1px solid var(--border-color);
        transition: transform var(--transition-medium), box-shadow var(--transition-medium);
        position: relative;
        overflow: hidden;
    }

    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: var(--gradient-accent);
        transform: scaleX(0);
        transform-origin: left;
        transition: transform var(--transition-medium);
    }

    .feature-card:hover::before {
        transform: scaleX(1);
    }

    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: var(--shadow-glow);
    }

    /* Output samples */
    .output-sample {
        background: var(--bg-secondary);
        padding: var(--space-lg);
        border-radius: var(--radius-lg);
        border-left: 4px solid var(--accent-primary);
        margin: var(--space-lg) 0;
        font-family: 'Courier New', monospace;
        font-size: var(--text-sm);
        line-height: 1.5;
        overflow-x: auto;
        transition: transform var(--transition-medium);
    }

    .output-sample:hover {
        transform: translateY(-4px);
    }

    /* Project links section */
    .project-links-section {
        text-align: center;
        margin: var(--space-xl) 0;
    }

    .links-grid {
        display: flex;
        flex-wrap: wrap;
        gap: var(--space-sm);
        justify-content: center;
        margin-top: var(--space-md);
    }

    /* Dashboard CTA */
    .dashboard-cta {
        text-align: center;
        background: var(--bg-secondary);
        padding: var(--space-xl);
        border-radius: var(--radius-lg);
        margin: var(--space-xl) 0;
        border: 1px solid var(--border-color);
        transition: transform var(--transition-medium);
        position: relative;
        overflow: hidden;
    }

    .dashboard-cta::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(0,122,204,0.05) 0%, rgba(0,90,158,0.05) 100%);
        opacity: 0;
        transition: opacity var(--transition-medium);
    }

    .dashboard-cta:hover::before {
        opacity: 1;
    }

    .dashboard-cta:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-glow);
    }

    /* Systematic output layout */
    .system-partition {
        display: grid;
        grid-template-columns: 1fr;
        gap: 0;
        background: var(--bg-secondary);
        border-radius: var(--radius-lg);
        border: 1px solid var(--border-color);
        overflow: hidden;
        margin: var(--space-lg) 0;
        transition: transform var(--transition-medium);
    }

    .system-partition:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-glow);
    }

    .partition-header {
        background: var(--bg-tertiary);
        color: var(--accent-primary);
        font-weight: bold;
        padding: var(--space-md);
        border-bottom: 2px solid var(--accent-primary);
        font-family: 'Courier New', monospace;
    }

    .partition-section {
        padding: var(--space-md);
        border-bottom: 1px solid var(--border-color);
    }

    .partition-section:last-child {
        border-bottom: none;
    }

    .compact-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .compact-list li {
        padding: var(--space-xs) 0;
        border-bottom: 1px solid var(--bg-tertiary);
        display: flex;
        align-items: flex-start;
        transition: color var(--transition-fast);
    }

    .compact-list li:hover {
        color: var(--text-primary);
    }

    .compact-list li:last-child {
        border-bottom: none;
    }

    .list-bullet {
        color: var(--accent-secondary);
        margin-right: var(--space-sm);
        font-weight: bold;
    }

    /* Section spacing */
    section {
        margin: var(--space-2xl) 0;
    }

    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }

    /* Scroll animations */
    .fade-in {
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.6s ease, transform 0.6s ease;
    }

    .fade-in.visible {
        opacity: 1;
        transform: translateY(0);
    }

    /* Mobile optimizations */
    @media (max-width: 768px) {
        body {
            padding: var(--space-sm);
        }

        .feature-grid {
            grid-template-columns: 1fr;
            gap: var(--space-md);
        }

        .links-grid {
            flex-direction: column;
            align-items: center;
        }

        .links-grid .btn {
            width: min(100%, 300px);
            margin: var(--space-xs) 0;
        }

        .dashboard-cta {
            padding: var(--space-lg);
        }

        .output-sample {
            padding: var(--space-md);
            font-size: var(--text-xs);
        }

        /* Reduce motion for better performance */
        @media (prefers-reduced-motion: reduce) {
            .btn,
            .feature-card,
            .output-sample,
            .dashboard-cta,
            .system-partition {
                transition: none;
            }
            
            .btn:hover,
            .feature-card:hover,
            .output-sample:hover,
            .dashboard-cta:hover,
            .system-partition:hover {
                transform: none;
            }
            
            .btn::before,
            .feature-card::before,
            .dashboard-cta::before {
                display: none;
            }
            
            html {
                scroll-behavior: auto;
            }
        }
    }

    @media (max-width: 480px) {
        .container {
            padding: 0 var(--space-sm);
        }

        header {
            padding: var(--space-xl) var(--space-md);
        }

        .feature-card {
            padding: var(--space-md);
        }
    }
    </style>
</head>

<body>
    <div class="container">
        <header>
            <div class="header-content">
                <h1>🌍 International Trade Compliance System</h1>
                <p class="subtitle">Python application for analyzing trade regulations between Italy and India</p>
                <div class="tech-tags">
                    <span class="tech-tag">Python</span>
                    <span class="tech-tag">Data Analysis</span>
                    <span class="tech-tag">International Business</span>
                    <span class="tech-tag">Trade Compliance</span>
                </div>
            </div>
        </header>

        <section class="fade-in">
            <h2>About This Project</h2>
            <p>This Python application provides comprehensive trade compliance data for international business operations between Italy and India, including documentation requirements, logistics information, and regulatory frameworks.</p>
            
            <div class="feature-grid">
                <div class="feature-card">
                    <h3>🇮🇹 Italy Data</h3>
                    <p>EU compliance standards, ports, VAT information, and documentation requirements</p>
                </div>
                <div class="feature-card">
                    <h3>🇮🇳 India Data</h3>
                    <p>Customs procedures, import licenses, GST rates, and trade logistics</p>
                </div>
                <div class="feature-card">
                    <h3>📊 Comparison</h3>
                    <p>Side-by-side analysis of trade regulations and bilateral context</p>
                </div>
            </div>
        </section>

        <section class="project-links-section fade-in">
            <h2>Project Links</h2>
            <div class="links-grid">
                <a href="demo.html" class="btn btn-primary">📊 Interactive Demo</a>
                <a href="documentation.html" class="btn">📚 Documentation</a>
                <a href="trade_compliance.py" download class="btn btn-secondary">💾 Download Code</a>
                <a href="https://krishnaadayma.github.io/" class="btn btn-portfolio">← Back to Portfolio</a>
            </div>
        </section>

        <section class="dashboard-cta fade-in">
            <h2>Interactive Analytics Dashboard</h2>
            <p>Explore our advanced data visualization platform with interactive charts and comprehensive trade analytics:</p>
            <a href="demo.html" class="btn btn-warning" style="padding: var(--space-md) var(--space-xl);">
                🚀 Launch Analytics Dashboard
            </a>
        </section>

        <section class="fade-in">
            <h2>Example Output</h2>
            <div class="system-partition">
                <div class="partition-header">
                    🌍 INTERNATIONAL TRADE COMPLIANCE SYSTEM
                </div>
                <div class="partition-section">
                    <div class="partition-header" style="background: transparent; border-bottom: 1px solid var(--border-color); padding: var(--space-sm) var(--space-md);">
                        TRADE COMPLIANCE DATA: ITALY
                    </div>
                    <div style="margin-top: var(--space-md);">
                        <div style="color: var(--accent-secondary); font-weight: bold; margin-bottom: var(--space-sm);">📋 GENERAL INFORMATION:</div>
                        <ul class="compact-list">
                            <li><span class="list-bullet">•</span> Official Name: Italian Republic</li>
                            <li><span class="list-bullet">•</span> Currency: Euro (EUR)</li>
                            <li><span class="list-bullet">•</span> EU Member: Yes</li>
                        </ul>
                    </div>
                    <div style="margin-top: var(--space-md);">
                        <div style="color: var(--accent-secondary); font-weight: bold; margin-bottom: var(--space-sm);">🚢 TRADE LOGISTICS:</div>
                        <ul class="compact-list">
                            <li><span class="list-bullet">•</span> Primary Ports: Genoa, Trieste, Gioia Tauro...</li>
                            <li><span class="list-bullet">•</span> VAT on Imports: 22.0%</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <section class="fade-in">
            <h2>How to Run</h2>
            <p>Download the Python file and run it using:</p>
            <div class="output-sample">
                python trade_compliance.py
            </div>
            <div style="text-align: center; margin-top: var(--space-md);">
                <a href="trade_compliance.py" download class="btn btn-secondary">
                    💾 Download Python File
                </a>
            </div>
        </section>
    </div>

    <script>
        // Scroll animation functionality
        function handleScrollAnimations() {
            const elements = document.querySelectorAll('.fade-in');
            
            elements.forEach(element => {
                const elementTop = element.getBoundingClientRect().top;
                const elementVisible = 150;
                
                if (elementTop < window.innerHeight - elementVisible) {
                    element.classList.add('visible');
                }
            });
        }

        // Initialize on page load
        document.addEventListener('DOMContentLoaded', function() {
            // Smooth scrolling for anchor links
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    const target = document.querySelector(this.getAttribute('href'));
                    if (target) {
                        target.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                });
            });
            // Mock TradeCompliance class for frontend demonstration
class TradeCompliance {
    constructor(config) {
        this.country = config.country;
        this.productCategory = config.productCategory;
        this.updateFrequency = config.updateFrequency;
    }

    calculateCosts(params) {
        // Mock calculation based on input parameters
        const baseCost = params.shipmentValue * 0.02; // 2% base compliance cost
        let additionalCosts = 0;
        
        if (this.country === 'italy') {
            additionalCosts += params.shipmentValue * 0.005; // Italy specific costs
        }
        
        if (this.productCategory === 'electronics') {
            additionalCosts += params.shipmentValue * 0.003; // Electronics specific costs
        }
        
        return {
            totalCost: baseCost + additionalCosts,
            baseComplianceFee: baseCost,
            countrySpecificFees: additionalCosts,
            currency: 'EUR',
            breakdown: {
                documentation: baseCost * 0.4,
                regulatoryFees: baseCost * 0.3,
                inspection: baseCost * 0.2,
                miscellaneous: baseCost * 0.1
            }
        };
    }
}

// Demo functions
function runDemo() {
    try {
        // Initialize analyzer
        const analyzer = new TradeCompliance({
            country: 'italy',
            productCategory: 'electronics',
            updateFrequency: 'realtime'
        });

        // Calculate costs
        const costs = analyzer.calculateCosts({
            shipmentValue: 50000,
            productType: 'consumer_goods'
        });

        // Display results
        const outputDiv = document.getElementById('demoOutput');
        const outputContent = document.getElementById('outputContent');
        
        outputContent.textContent = JSON.stringify(costs, null, 2);
        outputDiv.style.display = 'block';
        
        // Scroll to results
        outputDiv.scrollIntoView({ behavior: 'smooth' });
        
    } catch (error) {
        alert('Error running demo: ' + error.message);
    }
}

function resetDemo() {
    document.getElementById('demoOutput').style.display = 'none';
    document.getElementById('outputContent').textContent = '';
}
            // Initial check for scroll animations
            handleScrollAnimations();
            
            // Add scroll event listener for animations
            window.addEventListener('scroll', handleScrollAnimations);
        });
    </script>
    <section class="fade-in">
    <h2>Quick Start Example</h2>
    <p>Here's how to initialize and use the trade compliance analyzer:</p>
    
    <div class="output-sample">
// Initialize trade compliance analyzer
const analyzer = new TradeCompliance({
    country: 'italy',
    productCategory: 'electronics',
    updateFrequency: 'realtime'
});

// Calculate compliance costs
const costs = analyzer.calculateCosts({
    shipmentValue: 50000,
    productType: 'consumer_goods'
});

console.log('Compliance Costs:', costs);
    </div>

    <div class="demo-output" id="demoOutput" style="margin-top: var(--space-md); padding: var(--space-md); background: var(--bg-secondary); border-radius: var(--radius-md); display: none;">
        <h4>Demo Output:</h4>
        <pre id="outputContent"></pre>
    </div>

    <div style="text-align: center; margin-top: var(--space-md);">
        <button onclick="runDemo()" class="btn btn-primary">▶ Run Demo</button>
        <button onclick="resetDemo()" class="btn">🔄 Reset</button>
    </div>
</section>
</body>
</html>
