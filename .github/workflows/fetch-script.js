const Parser = require('rss-parser');
const fs = require('fs');
const path = require('path');

const parser = new Parser();

// Direct Google News RSS Feed URLs
const italyFeedUrl = 'https://news.google.com/rss/search?q=italy+economy+business&hl=en-US&gl=US&ceid=US:en';
const indiaFeedUrl = 'https://news.google.com/rss/search?q=india+economy+business&hl=en-US&gl=US&ceid=US:en';

async function fetchNews() {
    try {
        console.log('Fetching feeds directly...');
        const [italyFeed, indiaFeed] = await Promise.all([
            parser.parseURL(italyFeedUrl),
            parser.parseURL(indiaFeedUrl)
        ]);
        console.log('Feeds fetched successfully.');

        const combinedItems = [...(italyFeed.items || []), ...(indiaFeed.items || [])];
        
        if (combinedItems.length === 0) {
            throw new Error('No news items found after combining feeds.');
        }

        // Sort by publication date, newest first
        combinedItems.sort((a, b) => new Date(b.isoDate) - new Date(a.isoDate));
        console.log(`Found ${combinedItems.length} total items. Saving the top items.`);

        // NEW: Save to data/ folder instead of root
        const dataDir = path.join(__dirname, '..', '..', 'data');
        
        // Create data/ folder if it doesn't exist
        if (!fs.existsSync(dataDir)) {
            fs.mkdirSync(dataDir, { recursive: true });
            console.log('Created data/ directory.');
        }

        const outputPath = path.join(dataDir, 'news.json');
        fs.writeFileSync(outputPath, JSON.stringify(combinedItems, null, 2));
        
        console.log(`Successfully saved news to ${outputPath}`);

    } catch (error) {
        console.error('An error occurred during the fetch process:', error);
        process.exit(1);
    }
}

fetchNews();
