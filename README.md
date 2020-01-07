# rScraper
rScaper == Rolba Scraper! It is a helper module for scraping data using selenium. 

Work in Progress.

Example:
from rScraper.rScraperGoogle import ScraperGoogle

def main():
    scrapingList = ["dog", "cat"]
    googleScraper = ScraperGoogle(scrapingList)
    googleScraper.openBrowser()
    googleScraper.searchPhrase(1)

if __name__ == '__main__':
    main()
