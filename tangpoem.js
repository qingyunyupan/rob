const puppeteer = require('puppeteer');
const fs = require('fs');

async function searchTangPoem() {
    const query = '蒸菜系列';
    const url = `https://www.google.com/search?q=${encodeURIComponent(query)}`;
  
    try {
        const browser = await puppeteer.launch({ headless: true });
        const page = await browser.newPage();

        await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36');
        await page.setViewport({ width: 1280, height: 800 });

        await page.goto(url, { waitUntil: 'domcontentloaded' });

        const results = await page.evaluate(() => {
            const items = [];
            const resultElements = document.querySelectorAll('div.g'); // Update the selector
            resultElements.forEach(result => {
                const titleElement = result.querySelector('h3');
                const linkElement = result.querySelector('a');
                if (titleElement && linkElement) {
                    const title = titleElement.innerText;
                    const url = linkElement.href;
                    items.push({ title, url });
                }
            });
            return items;
        });

        if (results.length > 0) {
            console.log("Found Tang Poetry results:");
            results.forEach((result, index) => {
                console.log(`${index + 1}. ${result.title} - ${result.url}`);
            });

            const jsonResults = JSON.stringify(results, null, 2);
            fs.writeFileSync('tang_poetry_results.json', jsonResults, 'utf8');
            console.log('Results saved to tang_poetry_results.json');
        } else {
            console.log('No Tang poetry-related content found.');
        }

        await browser.close();
    } catch (error) {
        console.error('Error while searching for Tang poetry:', error);
    }
}

searchTangPoem();
