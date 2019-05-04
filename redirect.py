import requests
import csv

URLS_HTML = 'urls.html'
f = open(URLS_HTML, 'w+')
message = """
       <html>
       <head></head>
       <body>
       """
f.write(message)
with open('urls.csv', encoding='UTF-8') as csvfile:
 m = csv.reader(csvfile)
 urls = [l for l in m]

 for url in urls:
   url = url[0]
   x = 1
   rs = requests.get(url.strip())
   for response in rs.history:
     message = """<p>%s -> </p>""" % (response.url)
     f.write(message)
   message = """
          <p>%s</p>
          <p>%s</p>
          """ % (rs.url, rs.status_code)
   f.write(message)
 message = """
        </body>
        </html>
        """
f.write(message)
f.close

