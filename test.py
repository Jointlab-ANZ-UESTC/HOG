import requests
import csv


URLS_HTML = 'urls.html'
f = open(URLS_HTML, 'w+')
with open('urls.csv',encoding='UTF-8') as csvfile:
    m = csv.reader(csvfile)
    urls = [l for l in m]

    for url in urls:

        str1 = url[0]
        str2 = requests.get(str1.strip())
        message = """
        <html>
        <head></head>
        <body>
        <p>%s</p>
        <p>%s</p>
        </body>
        </html>""" %(str1, str2)
        f.write(message)
        print(str1, str2)
input("Press Enter")
f.close()