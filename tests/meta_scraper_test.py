import unittest
from gnosticdb.meta_scraper import scrape

class MetaScraperTest(unittest.TestCase):
    def test_basic(self):
        html_doc = """<html><head><title>The Dormouse's story</title></head>
        <body>
        <meta name="aaa" content="aaa">
        <meta name="author" content="authorname">
        <meta name="author" content="secondAuthor">
        <meta name="keywords" content="HTML, CSS, JavaScript">


        <p class="title"><b>The Dormouse's story</b></p>

        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>

        <p class="story">...</p>
        """
        mdata = scrape(html_doc)
        self.assertEqual(str(mdata.title),       "The Dormouse's story")
        self.assertEqual(str(mdata.author),      "['authorname', 'secondAuthor']")
        self.assertEqual(str(mdata.keywords),    "['HTML, CSS, JavaScript']")
