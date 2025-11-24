const fetch = require('node-fetch');
const fs = require('fs');

const RSS_BASE = 'https://api.rss2json.com/v1/api.json?rss_url=';
const italyFeed = `${RSS_BASE}https://news.google.com/rss/search?q=italy+economy+business&hl=en-US&gl=US&ceid=US:en`;
const indiaFeed = `${RSS_BASE}https://news.google.com/rss/search?q=india+economy+business&hl=en-US&gl=US&ceid=US:en`;

async function fetchNews() {
    try {
        const [italyResponse, indiaResponse] = await Promise.all([
            fetch(italyFeed),
            fetch(indiaFeed)
        ]);

        if (!italyResponse.ok || !indiaResponse.ok) {
            throw new Error('Network response was not ok.');
        }

        const italyData = await italyResponse.json();
        const indiaData = await indiaResponse.json();

        if (italyData.status !== 'ok' || indiaData.status !== 'ok') {
            throw new Error('API status was not ok.');
        }

        const combinedItems = [...(italyData.items || []), ...(indiaData.items || [])];
        if (combinedItems.length === 0) {
            console.log('No news items found. No update needed.');
            return;
        }

        combinedItems.sort((a, b) => new Date(b.pubDate) - new Date(a.pubDate));

        fs.writeFileSync('news.json', JSON.stringify(combinedItems, null, 2));
        console.log('Successfully fetched and saved news to news.json');

    } catch (error) {
        console.error('Failed to fetch news:', error);
        process.exit(1); // Exit with an error code to fail the action
    }
}

fetchNews();
