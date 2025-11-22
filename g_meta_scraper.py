from bs4 import BeautifulSoup
import datetime

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

soup = BeautifulSoup(html_doc, 'html.parser')


# testing
# g_meta = soup.meta['name']    attribute stuff

# title
g_title = soup.title.string #this just works actually lol

# author list
g_author = []

g_author_metas = soup.find_all("meta", attrs={"name": "author"})
for meta in g_author_metas:
    g_author.append(meta.get("content"))
if len(g_author) == 0: g_author.append("None") #default author


# keywords
g_keywords = []

g_keywords_metas = soup.find_all("meta", attrs={"name": "keywords"})
for meta in g_keywords_metas:
    g_keywords.append(meta.get("content"))
if len(g_keywords) == 0: g_keywords.append("None") #default author


# access date
g_date_access = datetime.datetime.now()



# debugging
print(g_title)
print(g_author)
print(g_keywords)
print(g_date_access)