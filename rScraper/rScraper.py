from selenium import webdriver

class Scraper():
    def __init__(self):
        self.url = None
        self.webDriver = None

    def openBrowser(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("intl.accept_languages", 'en-us')
        profile.update_preferences()
        self.webDriver  = webdriver.Firefox(profile)


    def closeBrowser(self):
        self.webDriver.quit()



    def _openSearchEngine(self):
        raise NotImplementedError()

    def _getSearchItemUrl(self):
        raise NotImplementedError()

    def _getImagesUrls(self):
        raise NotImplementedError()

    def downloadImages(self):
        raise NotImplementedError()

    def searchPhrase(self):
        raise NotImplementedError()










