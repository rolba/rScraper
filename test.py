from rScraper.rScraperGoogle import ScraperGoogle
import os
def main():
    scrapingItem = "dog"
    scrapingDir = os.getcwd() + "/Downloads"
    googleScraper = ScraperGoogle(scrapingItem, directory=scrapingDir, delOldDwldDir=True)
    googleScraper.openBrowser()
    googleScraper.searchPhrase()
    googleScraper.downloadImages()
    googleScraper.closeBrowser()


if __name__ == '__main__':
    main()
