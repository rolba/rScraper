from rScraper.rScraper import Scraper
import urllib3
import time
import json
import os
import shutil

class ScraperGoogle(Scraper):
    """
    ScraperGoogle inherits from Scraper and implements not implemented methoods.
    This class is responsible for implementing downloading mechanism from Google search images engine.
    It has proper html parser and selenium implementations. It also saves data to hdd in localisation.
    
    This cals can only donwload one single search item. For multiple items you have to call rScraperWraper class.
    Which in general concept should be a multithread class to speed up download process.
    """
    
    def __init__(self, scrapingItem, directory, delOldDwldDir = True):
        """
        ScraperGoogle constructor.
        
        @type scrapingItem: string
        @param scrapingItem: Item name that will be searched in google images. like "dog" or "cat"
        
        @type directory: os.path
        @param directory: Directory where downloaded images will be stored inside "Download" dir
        
        @type delOldDwldDir: bool
        @param delOldDwldDir: Default = True - Existing download directory will be deleted.
        """
        
        super(Scraper, self).__init__()

        if delOldDwldDir:
            shutil.rmtree(directory)
            os.makedirs(directory)
        if not os.path.exists(directory):
            os.makedirs(directory)

        self.downloadDir = directory
        self.searchedElementDirName = None
        self.allowedImagesExtensions = {"jpg", "jpeg", "png", "gif"}
        self.scrpaingPhrase = scrapingItem
        self.url = {"begin":"https://www.google.com/search?q=",
                    "end":"&source=lnms&tbm=isch"}

    def _openSearchEngine(self):
        self.searchedElementDirName = os.path.join(self.downloadDir, self.scrpaingPhrase)
        lUrl = self._getSearchItemUrl(self.scrpaingPhrase)
        self.webDriver.get(lUrl)
        for _ in range(20):
            for _ in range(30):
                self.webDriver.execute_script("window.scrollBy(0, 2000)")
                time.sleep(0.5)
            try:
                self.webDriver.find_element_by_xpath("//input[@value='Więcej wyników']").click()
            except Exception as e:
                print("No more images found:", e)
                break

    def _getSearchItemUrl(self, searchItem):
        print(self.scrpaingPhrase)
        lUrl = self.url["begin"] + \
               searchItem +\
               self.url["end"]
        return lUrl

    def _imgsGetter(self, urls):
        imgsCount = 0
        downloadedImgsCount = 0
        print(self.searchedElementDirName)
        if not os.path.exists(self.searchedElementDirName):
            os.makedirs(self.searchedElementDirName)

        for url in urls:
            imgsCount += 1
            img_url = json.loads(url.get_attribute('innerHTML'))["ou"]
            img_type = json.loads(url.get_attribute('innerHTML'))["ity"]
            try:
                # Thy to save image on HDD
                if img_type not in self.allowedImagesExtensions:
                    img_type = "jpg"
                http = urllib3.PoolManager()

                # Write image to hdd. Don't forget about timeout!
                response = http.request('GET', img_url, timeout=2)
                downoadedFilePath = self.searchedElementDirName + "/" + str(downloadedImgsCount) + "." + img_type
                print(downoadedFilePath)
                f = open(downoadedFilePath, "wb")
                f.write(response.data)
                f.close
                downloadedImgsCount += 1
            except Exception as e:
                print ("Download failed:", e)
        return downloadedImgsCount

    def _getImagesUrls(self):
        urls = self.webDriver.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')
        return urls

    def downloadImages(self):
        urls = self._getImagesUrls()
        self._imgsGetter(urls)

    def searchPhrase(self):
        self._openSearchEngine()




