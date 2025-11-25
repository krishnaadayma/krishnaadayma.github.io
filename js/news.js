/* ==================================================================================
   NEWS.JS - Live News Feed Functionality
   ================================================================================== */

async function initializeNewsFeed() {
    if (!CONFIG.FEATURES.newsFeed) return;
    
    const container = document.getElementById('insights-container');
    const indicator = document.getElementById('live-indicator');
    const title = document.getElementById('insights-title');
    
    if (!container || !indicator || !title) {
        console.log('News feed elements not found');
        return;
    }

    const newsUrl = `${CONFIG.NEWS_FILE}?v=${Date.now()}`;
    
    try {
        const response = await fetch(newsUrl);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        
        const articles = await response.json();
        if (!Array.isArray(articles) || articles.length === 0) {
            throw new Error('No articles found');
        }
        
        // Update UI for success
        container.innerHTML = '';
        title.textContent = 'Bilateral Economic Intelligence';
        indicator.style.display = 'inline-block';
        
        // Create article observer for fade-in
        const articleObserver = new IntersectionObserver(entries => {
            entries.forEach(e => {
                if (e.isIntersecting) {
                    e.target.classList.add('visible');
                    articleObserver.unobserve(e.target);
                }
            });
        }, { threshold: 0.2 });
        
        // Render articles
        articles.slice(0, CONFIG.NEWS.maxArticles).forEach(article => {
            const card = createArticleCard(article);
            container.appendChild(card);
            articleObserver.observe(card);
        });
        
        console.log(`✓ News feed loaded: ${CONFIG.NEWS.maxArticles} articles`);
        
    } catch (error) {
        console.error('News feed error:', error);
        title.textContent = 'Intelligence Feed';
        indicator.style.display = 'none';
        container.innerHTML = `
            <p class="loading-text">Live feed is currently unavailable.</p>
        `;
    }
}

function createArticleCard(article) {
    const card = document.createElement('div');
    card.className = 'card fade-in';
    card.style.padding = 'var(--space-md)';
    
    const title = article.title || 'Untitled Article';
    const source = article.author || 'Google News';
    const link = article.link || '#';
    
    card.innerHTML = `
        <h4>
            <a href="${link}" target="_blank" rel="noopener noreferrer">
                ${title}
            </a>
        </h4>
        <p class="company">Source: ${source}</p>
    `;
    
    return card;
}
