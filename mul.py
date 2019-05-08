import threading
import requests
import csv


with open('urls.csv',encoding='UTF-8') as csvfile:
    m = csv.reader(csvfile)
    urls = [l for l in m]


class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):  # 定义每个线程要运行的函数

        target = input("Input the file's name: ")

        with open(target, encoding='UTF-8') as csvfile:
            m = csv.reader(csvfile)
            urls = [l for l in m]

        for url in urls:
            str1 = url[0]
            str2 = requests.get(str1.strip())

            print(str1, str2)

        input("Press Enter")



t1 = MyThread(1)
t2 = MyThread(2)
t1.start()
t2.start()
