import requests
from urlparse import urlsplit
import sqlite3

url = "GET /SQL_Injection/1/{hostname_and_port}/{original_path_and_query_string}"
input = url.split('/')

con = sqlite3.connect('mydb.db')

cur = con.cursor()
cur.execute("select text from blacklist where text=?", (input[1],))
data = cur.fetchall()

if not data:
        print ('No malware', data)
else:
        print ('Malware found')
																																																																																																																																																													
