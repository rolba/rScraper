from rScraper.rScraperGoogle import ScraperGoogle
from rScraper.rScraperYoutube import ScraperYoutube

class ScraperWraper():
    def __init__(self, itemsList = [], deleteOldDownloads = False, searchEngine = None):
        self.itemsListTodownload = itemsList
        self.deleteOldDownloads = deleteOldDownloads
        self._avilableSearchEngines = {"google": ScraperGoogle,
                                 "youtube": ScraperYoutube}
        try:
            self._avilableSearchEngines[searchEngine]
        except Exception as e:
                print("No searche engine found:", e)
        else:
            self.searchEngine = searchEngine

        # Add all logic in terms of iterating over list to here.
        # think about threading - spliting list between single threds to speed up
        # implement it as a choose - Google search or YT search [future]