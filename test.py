from rScraper.rScraperGoogle import ScraperGoogle
import os
def main():
    scrapingItem = "dog"
    googleScraper = ScraperGoogle(scrapingItem, directory= os.getcwd() + "/Downloads", delOldDwldDir=True)
    googleScraper.openBrowser()
    googleScraper.searchPhrase()
    googleScraper.downloadImages()
    googleScraper.closeBrowser()


if __name__ == '__main__':
    main()
