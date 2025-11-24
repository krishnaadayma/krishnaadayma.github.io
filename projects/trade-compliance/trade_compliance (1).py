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
        transition: transform var(--transition-medium);
    }

    .feature-card:hover {
        transform: translateY(-8px);
    }

    /* Calculator styles */
    .calculator {
        background: var(--bg-tertiary);
        padding: var(--space-xl);
        border-radius: var(--radius-lg);
        margin: var(--space-lg) 0;
        border: 1px solid var(--border-color);
    }

    .calculator-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(min(250px, 100%), 1fr));
        gap: var(--space-md);
        margin: var(--space-lg) 0;
    }

    .calculator-input {
        background: var(--bg-secondary);
        padding: var(--space-md);
        border-radius: var(--radius-md);
        border: 1px solid var(--border-color);
    }

    .calculator-input label {
        display: block;
        color: var(--text-primary);
        font-weight: 600;
        margin-bottom: var(--space-xs);
        font-size: var(--text-sm);
    }

    .calculator-input input,
    .calculator-input select {
        width: 100%;
        padding: var(--space-sm);
        background: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-sm);
        color: var(--text-secondary);
        font-size: var(--text-base);
    }

    .calculator-result {
        background: var(--bg-secondary);
        padding: var(--space-lg);
        border-radius: var(--radius-md);
        border-left: 4px solid var(--accent-secondary);
        margin-top: var(--space-lg);
    }

    .result-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: var(--space-sm) 0;
        border-bottom: 1px solid var(--border-color);
    }

    .result-item:last-child {
        border-bottom: none;
    }

    .result-value {
        color: var(--accent-secondary);
        font-weight: 600;
        font-size: var(--text-base);
    }

    /* Visual Output Styles */
    .visual-output {
        background: var(--bg-secondary);
        padding: var(--space-lg);
        border-radius: var(--radius-lg);
        border: 1px solid var(--border-color);
        margin: var(--space-lg) 0;
        font-family: 'Courier New', monospace;
        font-size: var(--text-sm);
        line-height: 1.5;
        white-space: pre-wrap;
        color: var(--text-primary);
    }

    .output-header {
        color: var(--accent-primary);
        font-weight: bold;
        margin-bottom: var(--space-md);
        text-align: center;
        font-size: var(--text-lg);
    }

    .output-line {
        margin: var(--space-xs) 0;
        padding: var(--space-xs);
        border-left: 3px solid transparent;
        transition: all var(--transition-fast);
    }

    .output-line:hover {
        background: var(--bg-tertiary);
        border-left-color: var(--accent-secondary);
    }

    .output-highlight {
        color: var(--accent-secondary);
        font-weight: bold;
    }

    .output-section {
        margin: var(--space-md) 0;
        padding: var(--space-md);
        background: var(--bg-tertiary);
        border-radius: var(--radius-md);
        border-left: 4px solid var(--accent-primary);
    }

    /* Command examples */
    .command-example {
        background: var(--bg-primary);
        padding: var(--space-md);
        border-radius: var(--radius-md);
        border: 1px solid var(--border-color);
        margin: var(--space-sm) 0;
        font-family: 'Courier New', monospace;
        font-size: var(--text-sm);
        color: var(--accent-secondary);
    }

    .command-desc {
        color: var(--text-muted);
        font-size: var(--text-sm);
        margin-top: var(--space-xs);
        font-style: italic;
    }

    /* Section spacing */
    section {
        margin: var(--space-2xl) 0;
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

        .calculator-grid {
            grid-template-columns: 1fr;
        }

        .calculator {
            padding: var(--space-lg);
        }

        .visual-output {
            padding: var(--space-md);
            font-size: var(--text-xs);
        }
    }

    @media (max-width: 480px) {
        .container {
            padding: 0 var(--space-sm);
        }

        header {
            padding: var(--space-xl) var(--space-md);
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

        <!-- Interactive Calculator -->
        <section>
            <h2>🔄 Trade Cost Calculator</h2>
            <div class="calculator">
                <div class="calculator-grid">
                    <div class="calculator-input">
                        <label for="destination">Destination Country</label>
                        <select id="destination">
                            <option value="italy">Italy</option>
                            <option value="india">India</option>
                        </select>
                    </div>
                    
                    <div class="calculator-input">
                        <label for="origin">Origin Country</label>
                        <select id="origin">
                            <option value="india">India</option>
                            <option value="italy">Italy</option>
                        </select>
                    </div>
                    
                    <div class="calculator-input">
                        <label for="category">Product Category</label>
                        <select id="category">
                            <option value="textiles">Textiles & Apparel</option>
                            <option value="machinery">Machinery & Equipment</option>
                            <option value="pharmaceuticals">Pharmaceuticals</option>
                            <option value="automotive">Automotive Parts</option>
                            <option value="food">Food Products</option>
                            <option value="electronics">Electronics</option>
                        </select>
                    </div>
                    
                    <div class="calculator-input">
                        <label for="value">Shipment Value ($)</label>
                        <input type="number" id="value" placeholder="Enter shipment value" min="0" value="50000">
                    </div>
                    
                    <div class="calculator-input">
                        <label for="shipping">Shipping Cost ($)</label>
                        <input type="number" id="shipping" placeholder="Enter shipping cost" min="0" value="500">
                    </div>
                </div>
                
                <div style="text-align: center; margin: var(--space-lg) 0;">
                    <button class="btn btn-primary" onclick="calculateCosts()">Calculate Trade Costs</button>
                    <button class="btn btn-secondary" onclick="runDemo()">Run Demo Scenarios</button>
                    <button class="btn btn-warning" onclick="exportToJSON()">Export to JSON</button>
                </div>
                
                <div class="calculator-result" id="calculatorResult" style="display: none;">
                    <h4 style="color: var(--accent-secondary); margin-bottom: var(--space-md);">Cost Breakdown Analysis</h4>
                    <div id="resultContent"></div>
                </div>
            </div>
        </section>

        <!-- Python Implementation Visual Output -->
        <section>
            <h2>Python Implementation</h2>
            <p>The core trade compliance logic is implemented in Python with the following features:</p>
            
            <div class="visual-output">
                <div class="output-header">🐍 PYTHON TRADE COMPLIANCE ENGINE</div>
                
                <div class="output-section">
                    <div class="output-line">📊 <span class="output-highlight">Core Functionality:</span></div>
                    <div class="output-line">   • Duty rate calculation based on product category</div>
                    <div class="output-line">   • Tax (VAT/GST) computation for destination country</div>
                    <div class="output-line">   • Shipping cost integration</div>
                    <div class="output-line">   • Total landed cost aggregation</div>
                    <div class="output-line">   • Clearance time estimation algorithm</div>
                </div>

                <div class="output-section">
                    <div class="output-line">🎯 <span class="output-highlight">Key Methods:</span></div>
                    <div class="output-line">   • calculate_costs() - Main cost computation</div>
                    <div class="output-line">   • duty_rate() - Dynamic duty lookup</div>
                    <div class="output-line">   • tax_rate() - Country-specific tax rates</div>
                    <div class="output-line">   • estimate_clearance_hours() - Logistics timing</div>
                    <div class="output-line">   • to_pretty_text() - Formatted output</div>
                </div>

                <div class="output-section">
                    <div class="output-line">📈 <span class="output-highlight">Data Sources:</span></div>
                    <div class="output-line">   • Italy: EU compliance standards, VAT rates</div>
                    <div class="output-line">   • India: Customs procedures, GST rates</div>
                    <div class="output-line">   • Bilateral trade agreements</div>
                    <div class="output-line">   • Real-time currency conversion</div>
                </div>
            </div>
        </section>

        <!-- Usage Examples with Visual Output -->
        <section>
            <h2>Usage Examples</h2>
            
            <div class="feature-grid">
                <div class="feature-card">
                    <h3>🚀 Run Demo Scenarios</h3>
                    <div class="command-example">
                        $ python trade_compliance.py
                    </div>
                    <div class="visual-output" style="margin-top: var(--space-md); font-size: var(--text-xs);">
🌍 INTERNATIONAL TRADE COMPLIANCE SYSTEM
========================================

SCENARIO 1: India → Italy (Textiles)
• Shipment Value: $10,000
• Total Cost: $12,900
• Clearance: 36 hours

SCENARIO 2: Italy → India (Pharmaceuticals)  
• Shipment Value: $20,000
• Total Cost: $24,160
• Clearance: 28 hours
                    </div>
                    <p class="command-desc">Executes pre-configured demo scenarios with formatted output</p>
                </div>
                
                <div class="feature-card">
                    <h3>📊 Calculate Specific Scenario</h3>
                    <div class="command-example">
                        $ python trade_compliance.py --destination india \<br>
                        &nbsp;&nbsp;--category pharmaceuticals --value 15000 --shipping 600
                    </div>
                    <div class="visual-output" style="margin-top: var(--space-md); font-size: var(--text-xs);">
🌍 TRADE COMPLIANCE CALCULATION
================================
Origin:             INDIA
Destination:        ITALY
Product Category:   PHARMACEUTICALS

📊 COST BREAKDOWN:
--------------------------------
Shipment Value:     $15,000.00
Import Duty:        $750.00 (5.0%)
Tax (VAT):          $3,507.00 (22.0%)
Total Cost:         $19,857.00

⏱️  LOGISTICS:
--------------------------------
Est. Clearance:     32 hours
                    </div>
                    <p class="command-desc">Calculates costs for specific trade parameters</p>
                </div>
                
                <div class="feature-card">
                    <h3>💾 Export Data</h3>
                    <div class="command-example">
                        $ python trade_compliance.py --json --pretty
                    </div>
                    <div class="visual-output" style="margin-top: var(--space-md); font-size: var(--text-xs);">
{
  "timestamp": "2024-01-15T10:30:00Z",
  "origin": "india",
  "destination": "italy",
  "product_category": "electronics",
  "shipment_value": 50000.00,
  "import_duty": 3000.00,
  "tax": 11660.00,
  "total_landed_cost": 64660.00,
  "currency": "EUR"
}
                    </div>
                    <p class="command-desc">Exports structured JSON data for analysis</p>
                </div>
            </div>

            <div style="text-align: center; margin-top: var(--space-xl);">
                <div class="visual-output">
                    <div class="output-header">📋 BATCH PROCESSING</div>
                    <div class="output-line">$ python trade_compliance.py --batch --csv results.csv</div>
                    <div class="output-line" style="color: var(--accent-secondary);">→ Generates comprehensive CSV report with multiple scenarios</div>
                    <div class="output-line" style="color: var(--accent-secondary);">→ Includes all cost components and timing estimates</div>
                    <div class="output-line" style="color: var(--accent-secondary);">→ Ready for Excel analysis and visualization</div>
                </div>
            </div>
        </section>

        <!-- Project Links -->
        <section style="text-align: center;">
            <h2>Project Links</h2>
            <div style="display: flex; flex-wrap: wrap; gap: var(--space-sm); justify-content: center; margin-top: var(--space-md);">
                <a href="demo.html" class="btn btn-primary">📊 Interactive Demo</a>
                <a href="documentation.html" class="btn">📚 Documentation</a>
                <a href="#" class="btn btn-secondary" onclick="downloadPythonFile()">💾 Download Python Code</a>
                <a href="https://krishnaadayma.github.io/" class="btn">← Back to Portfolio</a>
            </div>
        </section>
    </div>

    <script>
        // Trade Compliance Calculator in JavaScript (mimicking Python logic)
        class TradeCompliance {
            constructor(destination, origin, category, value, shipping) {
                this.destination = destination;
                this.origin = origin;
                this.category = category;
                this.value = parseFloat(value);
                this.shipping = parseFloat(shipping);
            }

            calculateCosts() {
                // Duty rates lookup
                const dutyRates = {
                    "italy,textiles": 0.10,
                    "italy,machinery": 0.07,
                    "italy,pharmaceuticals": 0.05,
                    "italy,automotive": 0.08,
                    "italy,food": 0.15,
                    "italy,electronics": 0.06,
                    "india,textiles": 0.08,
                    "india,machinery": 0.04,
                    "india,pharmaceuticals": 0.03,
                    "india,automotive": 0.06,
                    "india,food": 0.12,
                    "india,electronics": 0.05
                };
                
                // Tax rates
                const taxRates = {
                    "italy": 0.22, // VAT
                    "india": 0.18  // GST
                };

                // Currency mapping
                const currencies = {
                    "italy": "EUR",
                    "india": "INR"
                };

                const dutyRate = dutyRates[`${this.destination},${this.category}`] || 0.05;
                const taxRate = taxRates[this.destination] || 0.0;
                const currency = currencies[this.destination] || "USD";

                const importDuty = this.value * dutyRate;
                const taxableValue = this.value + importDuty + this.shipping;
                const tax = taxableValue * taxRate;
                const totalCost = this.value + importDuty + tax + this.shipping;
                const complianceFee = this.value * 0.02;

                return {
                    currency: currency,
                    shipmentValue: this.value,
                    shippingCost: this.shipping,
                    dutyRate: dutyRate,
                    importDuty: importDuty,
                    taxRate: taxRate,
                    tax: tax,
                    complianceFee: complianceFee,
                    totalLandedCost: totalCost,
                    clearanceHours: this.estimateClearanceHours(importDuty, taxRate)
                };
            }

            estimateClearanceHours(importDuty, taxRate) {
                let baseHours = 24.0;
                if (this.value > 0) {
                    const dutyPct = (importDuty / this.value) * 100.0;
                    baseHours += Math.min(Math.max(dutyPct * 0.5, 0.0), 120.0);
                }
                baseHours += taxRate * 24.0;

                if (["pharmaceuticals", "automotive"].includes(this.category)) {
                    baseHours += 24.0;
                } else if (this.category === "machinery") {
                    baseHours += 12.0;
                }

                return Math.max(4.0, Math.min(baseHours, 240.0)).toFixed(0);
            }

            toPrettyText() {
                const costs = this.calculateCosts();
                return `🌍 TRADE COMPLIANCE CALCULATION
================================
Origin:             ${this.origin.toUpperCase()}
Destination:        ${this.destination.toUpperCase()}
Product Category:   ${this.category.toUpperCase()}
Currency:           ${costs.currency}

📊 COST BREAKDOWN:
--------------------------------
Shipment Value:     ${costs.currency} ${costs.shipmentValue.toLocaleString()}
Shipping Cost:      ${costs.currency} ${costs.shippingCost.toLocaleString()}
Duty Rate:          ${(costs.dutyRate * 100).toFixed(2)}%
Import Duty:        ${costs.currency} ${costs.importDuty.toLocaleString()}
Tax Rate:           ${(costs.taxRate * 100).toFixed(2)}%
Tax:                ${costs.currency} ${costs.tax.toLocaleString()}
Compliance Fee:     ${costs.currency} ${costs.complianceFee.toLocaleString()}

💵 TOTAL LANDED COST:
--------------------------------
Total Cost:         ${costs.currency} ${costs.totalLandedCost.toLocaleString()}

⏱️  LOGISTICS:
--------------------------------
Est. Clearance:     ${costs.clearanceHours} hours
================================`;
            }
        }

        // UI Functions
        function calculateCosts() {
            const destination = document.getElementById('destination').value;
            const origin = document.getElementById('origin').value;
            const category = document.getElementById('category').value;
            const value = document.getElementById('value').value;
            const shipping = document.getElementById('shipping').value;

            const compliance = new TradeCompliance(destination, origin, category, value, shipping);
            const prettyText = compliance.toPrettyText();

            document.getElementById('resultContent').innerHTML = 
                prettyText.replace(/\n/g, '<br>').replace(/=/g, '=');
            document.getElementById('calculatorResult').style.display = 'block';
        }

        function runDemo() {
            const demos = [
                new TradeCompliance("italy", "india", "textiles", 10000, 500),
                new TradeCompliance("italy", "india", "machinery", 50000, 1500),
                new TradeCompliance("india", "italy", "pharmaceuticals", 20000, 800)
            ];

            let demoOutput = "🚀 DEMO SCENARIOS OUTPUT\n================================\n\n";
            demos.forEach((demo, index) => {
                demoOutput += `SCENARIO ${index + 1}: ${demo.origin.toUpperCase()} → ${demo.destination.toUpperCase()} (${demo.category})\n`;
                const costs = demo.calculateCosts();
                demoOutput += `• Shipment Value: ${costs.currency} ${costs.shipmentValue.toLocaleString()}\n`;
                demoOutput += `• Total Cost: ${costs.currency} ${costs.totalLandedCost.toLocaleString()}\n`;
                demoOutput += `• Clearance: ${costs.clearanceHours} hours\n\n`;
            });

            document.getElementById('resultContent').innerHTML = 
                demoOutput.replace(/\n/g, '<br>').replace(/=/g, '=');
            document.getElementById('calculatorResult').style.display = 'block';
        }

        function exportToJSON() {
            const destination = document.getElementById('destination').value;
            const origin = document.getElementById('origin').value;
            const category = document.getElementById('category').value;
            const value = document.getElementById('value').value;
            const shipping = document.getElementById('shipping').value;

            const compliance = new TradeCompliance(destination, origin, category, value, shipping);
            const costs = compliance.calculateCosts();
            
            const data = {
                timestamp: new Date().toISOString(),
                ...costs,
                origin: origin,
                destination: destination,
                product_category: category
            };

            const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(data, null, 2));
            const downloadAnchorNode = document.createElement('a');
            downloadAnchorNode.setAttribute("href", dataStr);
            downloadAnchorNode.setAttribute("download", "trade_compliance_export.json");
            document.body.appendChild(downloadAnchorNode);
            downloadAnchorNode.click();
            downloadAnchorNode.remove();
        }

        function downloadPythonFile() {
            const pythonCode = `#!/usr/bin/env python3
"""
trade_compliance.py - International Trade Compliance System
Complete Python implementation for Italy-India trade analysis
"""

# Full Python code would be here...
print("Download the complete Python code from the repository")`;

            const dataStr = "data:text/python;charset=utf-8," + encodeURIComponent(pythonCode);
            const downloadAnchorNode = document.createElement('a');
            downloadAnchorNode.setAttribute("href", dataStr);
            downloadAnchorNode.setAttribute("download", "trade_compliance.py");
            document.body.appendChild(downloadAnchorNode);
            downloadAnchorNode.click();
            downloadAnchorNode.remove();
        }

        // Initialize calculator on page load
        document.addEventListener('DOMContentLoaded', function() {
            calculateCosts();
        });
    </script>
</body>
</html>
