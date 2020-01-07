from selenium import webdriver

class Scraper():
    def __init__(self):
        self.url = None
        self.webDriver = None

    def openBrowser(self):
        self.webDriver = webdriver.Firefox()

    def closeBrowser(self):
        self.webDriver.quit()

    def searchPhrase(self):
        raise NotImplementedError()

    def _openSearchEngine(self):
        raise NotImplementedError()

    def _getSearchItemUrl(self):
        raise NotImplementedError()









