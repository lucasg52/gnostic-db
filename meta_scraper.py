from bs4 import BeautifulSoup
import datetime

def scrape(htmlstream):
    return MetaScraper(htmlstream)

class MetaScraper:
    def __init__(self,htmlstream):
        soup = BeautifulSoup(htmlstream, 'html.parser')


        # testing
        # self.meta = soup.meta['name']    attribute stuff

        # title
        self.title = soup.title.string #this just works actually lol

        # author list
        self.author = []

        self.author_metas = soup.find_all("meta", attrs={"name": "author"})
        for meta in self.author_metas:
            self.author.append(meta.get("content"))
        if len(self.author) == 0:
            self.author.append("None") #default author


        # keywords
        self.keywords = []

        self.keywords_metas = soup.find_all("meta", attrs={"name": "keywords"})
        for meta in self.keywords_metas:
            self.keywords.append(meta.get("content"))
        if len(self.keywords) == 0:
            self.keywords.append("None") #default author


        # access date
        self.date_access = datetime.datetime.now()


        # testing
        # self.meta = soup.meta['name']    attribute stuff

        # title
        self.title = soup.title.string #this just works actually lol

        # author list
        self.author = []

        self.author_metas = soup.find_all("meta", attrs={"name": "author"})
        for meta in self.author_metas:
            self.author.append(meta.get("content"))
        if len(self.author) == 0:
            self.author.append("None") #default author


        # keywords
        self.keywords = []

        self.keywords_metas = soup.find_all("meta", attrs={"name": "keywords"})
        for meta in self.keywords_metas:
            self.keywords.append(meta.get("content"))
        if len(self.keywords) == 0:
            self.keywords.append("None") #default author


        # access date
        self.date_access = datetime.datetime.now()


