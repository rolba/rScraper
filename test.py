from rScraper.rScraperGoogle import ScraperGoogle

def main():
    scrapingList = ["dog", "cat"]
    googleScraper = ScraperGoogle(scrapingList)
    googleScraper.openBrowser()
    googleScraper.searchPhrase(1)
    googleScraper.closeBrowser()


if __name__ == '__main__':
    main()
