from ..meta_scarper import meta_scraper

def handle(fp):
    return PostHandler(fp)

class PostHandler:
    def __init__(self, fp):
        self.metadata = meta_scraper(fp)
        #self.body = 


