from bs4 import BeautifulSoup
import datetime
import json
import sqlite3
from keyword_extractor.extract_keywords_to_json import extract_keywords_to_json


def scrape(htmlstream):
    return MetaScraper(htmlstream)

class MetaScraper:
    def __init__(self,htmlstream):
        soup = BeautifulSoup(htmlstream, 'html.parser')

        # enforce UTF-8 encoding some time before this

        bool_use_ml = False
        url_from_front = "placeholder"

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
        self.paragraphs = [p.get_text(strip=True) for p in soup.find_all(['p','h1','h2','h3','h4','h5','h6'])]



        # jsonify data
            # title, authors, keywords
            # para, headers
        combined = {
            "title": self.title,
            "author": self.author,
            "htmlkeywords": self.keywords
        }
        metadata_json = json.dumps(combined)

        combined = {
            "paragraphs": self.paragraphs
        }
        body_json = json.dumps(combined)
        


        # ADD SEPARATELY
            # llm keywords
            # url  

        send_paras = " ".join(self.paragraphs)

        ml_keywords = "None"
        if (bool_use_ml):
            open('ml_key.json', 'w')
            ml_keywords = extract_keywords_to_json(self.title, send_paras,output_file = 'ml_key.json')
        
        combined = {
            "ml_keywords": ml_keywords
        }
        mlkw_json = json.dumps(combined)

        #sqlite insert
        con = sqlite3.connect("data.db")
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


        # make these proper data types
        cur.execute("""
            INSERT INTO sites (date, url, keywords, metadata, body)
            VALUES (?, ?, ?, ?, ?)
        """, (
            self.date_access,
            "PLACEHOLDER URL",
            mlkw_json,
            metadata_json,
            body_json
        ))

        con.commit()

        # debugging
        # res = cur.execute("SELECT name FROM sqlite_master")
        # res = cur.execute("SELECT date FROM sites")
        # print(res.fetchall())

