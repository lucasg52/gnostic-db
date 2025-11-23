from bs4 import BeautifulSoup
import datetime

def scrape(htmlstream):
    return MetaScraper(htmlstream)

class MetaScraper:
    def __init__(self,htmlstream):
        soup = BeautifulSoup(htmlstream, 'html.parser')

        # enforce UTF-8 encoding some time before this

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

        # paragraphs & headers
        headers = [h.get_text(strip=True) for h in soup.find_all(['h1','h2','h3','h4','h5','h6'])]
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]

        # debugging
        # print("HEADERS:", headers)
        # print("PARAGRAPHS:", paragraphs)


