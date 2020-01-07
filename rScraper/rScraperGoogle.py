from rScraper.rScraper import Scraper

class ScraperGoogle(Scraper):
    def __init__(self, scrapingList):
        super(Scraper, self).__init__()
        self.scrpaingPhrasesList = scrapingList
        self.url = {"begin":"https://www.google.com/search?q=",
                    "end":"&source=lnms&tbm=isch"}

    def _openSearchEngine(self, searchItemIndex):
        lUrl = self._getSearchItemUrl(self.scrpaingPhrasesList[searchItemIndex])
        self.webDriver.get(lUrl)

    def _getSearchItemUrl(self, searchItem):
        print(self.scrpaingPhrasesList)
        lUrl = self.url["begin"] + \
               searchItem +\
               self.url["end"]
        return lUrl

    def searchPhrase(self, searchItemIndex):
        self._openSearchEngine(searchItemIndex)


