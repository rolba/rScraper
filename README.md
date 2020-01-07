# rScraper
rScaper == Rolba Scraper! It is a helper module for scraping data using selenium. 

Work in Progress.

Example:<br>
from rScraper.rScraperGoogle import ScraperGoogle<br>
<br>
def main():<br>
    scrapingList = ["dog", "cat"]<br>
    googleScraper = ScraperGoogle(scrapingList)<br>
    googleScraper.openBrowser()<br>
    googleScraper.searchPhrase(1)<br>
<br>
if __name__ == '__main__':<br>
    main()<br>
