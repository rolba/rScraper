# rScraper
rScaper == Rolba Scraper! It is a helper module for scraping data using selenium. 

Work in Progress due to the fact of rising competition. More on: https://ai-experiments.com/the-next-project-will-be/

Planned to be released on March 2020

Example:<br>
from rScraper.rScraperGoogle import ScraperGoogle<br>
<br>
def main():<br>
    scrapingList = ["dog", "cat"]<br>
    googleScraper = ScraperGoogle(scrapingList)<br>
    googleScraper.openBrowser()<br>
    googleScraper.searchPhrase(1)<br>
    googleScraper.closeBrowser()<br>
<br>
if __name__ == '__main__':<br>
    main()<br>
