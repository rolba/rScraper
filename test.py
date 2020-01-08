from rScraper.rScraperGoogle import ScraperGoogle
import os
def main():
    scrapingList = ["dog", "cat"]
    googleScraper = ScraperGoogle(scrapingList, directory= os.getcwd() + "/Downloads", delOldDwldDir=True)
    googleScraper.openBrowser()
    googleScraper.searchPhrase(1)
    googleScraper.downloadImages()
    googleScraper.closeBrowser()


if __name__ == '__main__':
    main()
