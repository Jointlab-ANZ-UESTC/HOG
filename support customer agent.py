import csv
import requests
from fake_useragent import UserAgent
ua=UserAgent()
resulthtml='result.html'
f=open(resulthtml,'w+')
with open('urls.csv', 'r') as csvfile:
    readcsv = csv.reader(csvfile)
    hd={}
    rows = [row for row in readcsv]
    f.write("""
     <!DOCTYPE html>
     <html>
     <head>
     <title>result</title>
     </head>
     <body>
     <h1>set customer user agent</h1>
     <table border="1">
     <caption>result</caption>
     <tr>
          <td>URL</td>
          <td>UserAgent</td>
     </tr>      
     """
    )
    for row in rows:
         row1=row[0]
         r = requests.get(row1.strip(), headers=hd)
         str=ua.random
         hd['User-Agent']=str
         if r.status_code == 200:
             info = """
             <tr>
             <td>%s</td>
             <td>%s</td>
             </tr>
             """%(row1,str)
             f.write(info)
             print(row1,r)
    f.write("""
     </table>
     </body>   
     </html>
     """
    )       
input("entrance")
f.close()

