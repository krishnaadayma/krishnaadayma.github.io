(() => {
  "use strict";

  // --- EXPANDED DATASET FOR TOP 10 GLOBAL ECONOMIES ---
  const COUNTRIES = [
    { id: 'usa', name: 'USA' }, { id: 'china', name: 'China' }, { id: 'japan', name: 'Japan' },
    { id: 'germany', name: 'Germany' }, { id: 'uk', name: 'UK' }, { id: 'france', name: 'France' },
    { id: 'india', name: 'India' }, { id: 'italy', name: 'Italy' }, { id: 'brazil', name: 'Brazil' },
    { id: 'canada', name: 'Canada' }
  ];
  const CURRENCIES = { usa: 'USD', china: 'CNY', japan: 'JPY', germany: 'EUR', uk: 'GBP', france: 'EUR', india: 'INR', italy: 'EUR', brazil: 'BRL', canada: 'CAD' };
  const TAX_RATES = { usa: 0.10, china: 0.13, japan: 0.10, germany: 0.19, uk: 0.20, france: 0.20, india: 0.18, italy: 0.22, brazil: 0.25, canada: 0.05 };
  const BASE_DUTY_RATES = {
    electronics: 0.05, machinery: 0.07, automotive: 0.10, pharmaceuticals: 0.03, textiles: 0.12, food: 0.15
  };
  // Free Trade Agreements (FTAs) reduce duty rates. Value is the new multiplier. 0 = no duty.
  const TRADE_AGREEMENTS = {
    'canada-usa': 0, 'usa-canada': 0, // USMCA
    'germany-france': 0, 'germany-italy': 0, 'france-germany': 0, 'france-italy': 0, 'italy-france': 0, 'italy-germany': 0, // EU
    'uk-japan': 0.5, 'japan-uk': 0.5 // UK-Japan CEPA
  };

  // --- MODEL ---
  class GlobalTradeModel {
    constructor(origin, destination, category, value, insurance, shippingMode) {
      this.origin = origin;
      this.destination = destination;
      this.category = category;
      this.value = Number(value) || 0;
      this.insurance = Number(insurance) || 0;
      this.shippingMode = shippingMode;
    }

    getDutyRate() {
      const agreementKey = `${this.origin}-${this.destination}`;
      const baseRate = BASE_DUTY_RATES[this.category] ?? 0.08;
      
      if (TRADE_AGREEMENTS.hasOwnProperty(agreementKey)) {
        return baseRate * TRADE_AGREEMENTS[agreementKey];
      }
      return baseRate;
    }
    
    calculate() {
      const dutyRate = this.getDutyRate();
      const taxRate = TAX_RATES[this.destination] ?? 0.15;
      const currency = CURRENCIES[this.destination] ?? 'USD';

      // Shipping cost & time vary by mode
      const shippingBaseCost = this.value * (this.shippingMode === 'air' ? 0.12 : 0.06);
      const shippingCost = shippingBaseCost + (Math.random() * 100); // Add variability
      const clearanceHours = 24 + (this.shippingMode === 'air' ? 24 : 72) + (dutyRate * 100) + (this.value / 5000);

      const importDuty = this.value * dutyRate;
      const taxableValue = this.value + shippingCost + this.insurance;
      const tax = (taxableValue + importDuty) * taxRate;
      const totalLandedCost = this.value + shippingCost + this.insurance + importDuty + tax;

      return {
        origin: this.origin,
        destination: this.destination,
        currency: currency,
        shipmentValue: this.value,
        totalLandedCost: totalLandedCost,
        importDuty: importDuty,
        tax: tax,
        logisticsCost: shippingCost + this.insurance,
        dutyRate: dutyRate,
        taxRate: taxRate,
        clearanceHours: Math.round(clearanceHours),
        hasFta: TRADE_AGREEMENTS.hasOwnProperty(`${this.origin}-${this.destination}`)
      };
    }
  }

  // --- UI & APPLICATION LOGIC ---
  function el(id) { return document.getElementById(id); }

  function populateDropdowns() {
    const originSelect = el('origin');
    const destSelect = el('destination');
    COUNTRIES.forEach(country => {
      originSelect.add(new Option(country.name, country.id));
      destSelect.add(new Option(country.name, country.id));
    });
    // Set default values that are not the same
    originSelect.value = 'usa';
    destSelect.value = 'germany';
  }

  function runAnalysis() {
    const origin = el('origin').value;
    const destination = el('destination').value;
    if (origin === destination) {
        alert("Origin and Destination countries cannot be the same.");
        return;
    }

    const category = el('category').value;
    const value = el('value').value;
    const insurance = el('insurance').value;
    const shippingMode = el('shipping-mode').value;

    const model = new GlobalTradeModel(origin, destination, category, value, insurance, shippingMode);
    
    // --- ANIMATION & PROCESSING LOGIC ---
    const analyzeBtn = el('analyzeBtn');
    const processingOverlay = el('processing-overlay');
    const processingStatus = el('processing-status');
    const resultsDashboard = el('results-dashboard');
    
    analyzeBtn.disabled = true;
    resultsDashboard.style.display = 'none';
    processingOverlay.style.display = 'block';

    const statuses = ["Connecting to global trade network...", "Analyzing tariff codes...", "Verifying trade agreements...", "Calculating logistics matrix...", "Finalizing analysis..."];
    let statusIndex = 0;
    
    const statusInterval = setInterval(() => {
        if(statusIndex < statuses.length) {
            processingStatus.textContent = statuses[statusIndex++];
        } else {
            clearInterval(statusInterval);
        }
    }, 600);

    setTimeout(() => {
        clearInterval(statusInterval);
        processingOverlay.style.display = 'none';
        const results = model.calculate();
        renderDashboard(results);
        analyzeBtn.disabled = false;
    }, 3500); // Simulate 3.5 seconds of processing
  }

  function formatMoney(value, currency) {
    return new Intl.NumberFormat('en-US', { style: 'currency', currency: currency, minimumFractionDigits: 0, maximumFractionDigits: 0 }).format(value);
  }

  function renderDashboard(data) {
    const dashboard = el('results-dashboard');
    dashboard.innerHTML = `
      <div class="metric-card" style="grid-column: 1 / -1;">
        <div class="label">Total Landed Cost</div>
        <div class="value total-cost">${formatMoney(data.totalLandedCost, data.currency)}</div>
      </div>
      <div class="metric-card">
        <div class="label">Import Duty</div>
        <div class="value">${formatMoney(data.importDuty, data.currency)}</div>
      </div>
      <div class="metric-card">
        <div class="label">Taxes (VAT/GST)</div>
        <div class="value">${formatMoney(data.tax, data.currency)}</div>
      </div>
      <div class="metric-card">
        <div class="label">Logistics & Insurance</div>
        <div class="value">${formatMoney(data.logisticsCost, data.currency)}</div>
      </div>
      <div class="metric-card">
        <div class="label">Duty Rate</div>
        <div class="value">${(data.dutyRate * 100).toFixed(1)}% ${data.hasFta ? ' (FTA Applied)' : ''}</div>
      </div>
      <div class="metric-card">
        <div class="label">Est. Clearance</div>
        <div class="value">~${data.clearanceHours} hrs</div>
      </div>
       <div class="metric-card">
        <div class="label">Shipment Value</div>
        <div class="value">${formatMoney(data.shipmentValue, data.currency)}</div>
      </div>
    `;
    dashboard.style.display = 'grid';
  }

  function wire() {
    populateDropdowns();
    el('analyzeBtn').addEventListener('click', runAnalysis);
  }

  document.addEventListener("DOMContentLoaded", wire);
})();
