from selenium import webdriver

class Scraper():
    """ 
    Scraper abstrac class used for defining interface for different scraping implementations. 
    You can have yor scraper implemented as inheritance for Google Image search, Bing Image search or even YouTube.
    
    Usage:
    This is the base class. Please see other implementations.
    
    """
    
    def __init__(self):
        """
        Scraper constructor
        """
        
        self.url = None
        self.webDriver = None

    def openBrowser(self):
        """
        Due to the fact that I am only using Firefox Browser this methood creates only Firefox webbrowser object.
        @TODO Add support for different webbrowsers
        """
        profile = webdriver.FirefoxProfile()
        profile.set_preference("intl.accept_languages", 'en-us')
        profile.update_preferences()
        self.webDriver  = webdriver.Firefox(profile)


    def closeBrowser(self):
        """
        This method cloases Firefox web browser.
        @TODO
        """
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










