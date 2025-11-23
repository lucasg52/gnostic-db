from ..meta_scraper import scrape

def handle(fp):
    return PostHandler(fp)

class PostHandler:
    def __init__(self, fp):
        self.metadata = scrape(fp)
        #self.body = 


