import csv
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua=UserAgent()
resu=list()
resulthtml='result.html'
f=open(resulthtml,'w+')
with open('urls.csv', 'r') as csvfile:
    readcsv = csv.reader(csvfile)
    hd={}
    hd['User-Agent']=ua.random
    rows = [row for row in readcsv]
    f.write("""
     <!DOCTYPE html>
     <html>
     <head>
     <title>result</title>
     </head>
     <body>"""
    )
    for row in rows:
        row1=row[0]
        r = requests.get(row1.strip(), headers=hd)
        if r.status_code == 200:
             info = """
             <p>%s</p>
             <p>%s</p>
             """%(row1,r)
             f.write(info)
             print(row1,r)
    f.write("""
     </body>   
     </html>
     """
    )       
input("entrance")
f.close()

