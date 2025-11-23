import os
import datetime
import time
import json
import sqlite3
from bs4 import BeautifulSoup
from keyword_extractor.extract_keywords_to_json import extract_keywords_to_json

def handle(fp):
    ph = PostHandler(fp)
    return ph

class PostHandler:
    def __init__(self, htmlstream, url = "unknown", header = None):
        self.htmlstream = htmlstream
        self.url = url
        self.bool_use_ml = False
        self.url_from_front = "placeholder"

        self.metascraper = self.scrape(htmlstream)
        self.sqlite_insert()

    def scrape(self, htmlstream):
        return MetaScraper(htmlstream)
    
    def sqlite_insert(self, dbpath = "data.db", metascraper = None):
        #sqlite insert
        if metascraper is None:
            metascraper = self.metascraper
        con = sqlite3.connect(dbpath)
        cur = con.cursor()

        #init table
        cur.execute("""
        CREATE TABLE IF NOT EXISTS sites(
            date TEXT,
            url TEXT,
            keywords TEXT,
            metadata TEXT,
            body TEXT
        )
        """)

        assert("data.db" in os.listdir())


        # make these proper data types
        cur.execute("""
            INSERT INTO sites (date, url, keywords, metadata, body)
            VALUES (?, ?, ?, ?, ?)
        """, (
            metascraper.date_access,
            self.url,
            metascraper.mlkw_json() if self.bool_use_ml else "{}",
            metascraper.metadata_json(),
            metascraper.body_json()
        ))

        con.commit()


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


        # access date


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
        self.date_access = str(int(time.time()*1000))

        # paragraphs & headers
        self.paragraphs = [p.get_text(strip=True) for p in soup.find_all(['p','h1','h2','h3','h4','h5','h6'])]


    def metadata_json(self):
        # jsonify data
            # title, authors, keywords
            # para, headers
        combined = {
            "title": self.title,
            "author": self.author,
            "htmlkeywords": self.keywords
        }
        return json.dumps(combined)


    def body_json(self):
        combined = {
            "paragraphs": self.paragraphs
        }
        return json.dumps(combined)
        


        # ADD SEPARATELY
            # llm keywords
            # url  

    def mklw_json(self):
        send_paras = " ".join(self.paragraphs)

        ml_keywords = "None"
        ml_keywords = extract_keywords_to_json(self.title, send_paras,output_file = 'ml_key.json')
        
        combined = {
            "ml_keywords": ml_keywords
        }
        return json.dumps(combined)

        # debugging
        # res = cur.execute("SELECT name FROM sqlite_master")
        # res = cur.execute("SELECT date FROM sites")
        # print(res.fetchall())

