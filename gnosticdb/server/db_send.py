import json
import sqlite3

def format_to_json():
    con = sqlite3.connect("data.db") # find right spot to grab this from
    cur = con.cursor()

    # init table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS sites(
        date TEXT,
        url TEXT,
        keywords TEXT,
        metadata TEXT,
        body TEXT
    )
    """)

    # Fetch all cols
    cols = cur.execute("SELECT date, url, keywords, metadata, body FROM sites").fetchall()

    
    result = {}
    for date, url, keywords, metadata, body in cols:
        result[date] = {
            "url": url,
            "keywords": keywords,
            "metadata": metadata,
            "body": body
        }

    # json string
    json_str = json.dumps(result, indent=4)

    return json_str

