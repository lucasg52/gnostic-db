from bs4 import BeautifulSoup
import datetime

def scrape_metadata(htmlstream):
    return MetaData(htmlstream)

class MetaData:
    def __init__(self,htmlstream):
        soup = BeautifulSoup(htmlstream, 'html.parser')


        # testing
        # self.g_meta = soup.meta['name']    attribute stuff

        # title
        self.g_title = soup.title.string #this just works actually lol

        # author list
        self.g_author = []

        self.g_author_metas = soup.find_all("meta", attrs={"name": "author"})
        for meta in self.g_author_metas:
            self.g_author.append(meta.get("content"))
        if len(self.g_author) == 0:
            self.g_author.append("None") #default author


        # keywords
        self.g_keywords = []

        self.g_keywords_metas = soup.find_all("meta", attrs={"name": "keywords"})
        for meta in self.g_keywords_metas:
            self.g_keywords.append(meta.get("content"))
        if len(self.g_keywords) == 0:
            self.g_keywords.append("None") #default author


        # access date
        self.g_date_access = datetime.datetime.now()


        # testing
        # self.g_meta = soup.meta['name']    attribute stuff

        # title
        self.g_title = soup.title.string #this just works actually lol

        # author list
        self.g_author = []

        self.g_author_metas = soup.find_all("meta", attrs={"name": "author"})
        for meta in self.g_author_metas:
            self.g_author.append(meta.get("content"))
        if len(self.g_author) == 0:
            self.g_author.append("None") #default author


        # keywords
        self.g_keywords = []

        self.g_keywords_metas = soup.find_all("meta", attrs={"name": "keywords"})
        for meta in self.g_keywords_metas:
            self.g_keywords.append(meta.get("content"))
        if len(self.g_keywords) == 0:
            self.g_keywords.append("None") #default author


        # access date
        self.g_date_access = datetime.datetime.now()


