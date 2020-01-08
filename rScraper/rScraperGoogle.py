from rScraper.rScraper import Scraper
import urllib3
import time
import json
import os
import shutil

class ScraperGoogle(Scraper):
    def __init__(self, scrapingList, directory, delOldDwldDir = False):
        super(Scraper, self).__init__()

        if delOldDwldDir:
            shutil.rmtree(directory)
            os.makedirs(directory)
        if not os.path.exists(directory):
            os.makedirs(directory)

        self.downloadDir = directory
        self.searchedElementDirName = None
        self.allowedImagesExtensions = {"jpg", "jpeg", "png", "gif"}
        self.scrpaingPhrasesList = scrapingList
        self.url = {"begin":"https://www.google.com/search?q=",
                    "end":"&source=lnms&tbm=isch"}

    def _openSearchEngine(self, searchItemIndex):
        self.searchedElementDirName = os.path.join(self.downloadDir, self.scrpaingPhrasesList[searchItemIndex])
        lUrl = self._getSearchItemUrl(self.scrpaingPhrasesList[searchItemIndex])
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
        print(self.scrpaingPhrasesList)
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

    def searchPhrase(self, searchItemIndex):
        self._openSearchEngine(searchItemIndex)




