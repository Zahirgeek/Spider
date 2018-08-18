from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
from time import sleep

def getName(url = "http://www.pythonscraping.com/pages/warandpeace.html"):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print("Name couldn't found")
        sleep(2)
        for i in range(3):
            getName()
    else:
        bsObj = BeautifulSoup(html)
    # findAll(tag, attributes, recursive, text, limit, keywords)
    nameList = bsObj.findAll("span", {"class": "green"})
    for name in nameList:
        print(name.get_text())

getName()
