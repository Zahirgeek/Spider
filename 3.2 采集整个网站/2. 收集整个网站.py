from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

pages = set()


def get_links(pageurl):
    global pages
    html = urlopen("https://en.wikipedia.org" + pageurl)
    bsObj = BeautifulSoup(html)
    try:
        print("title: ", bsObj.h1.get_text())
        print("paragraph: ", bsObj.find(id="mw-content-text").findAll("p")[0])
        print("links: ", bsObj.find(id="ca-edit").find("span").find("a").attrs["href"])
    except AttributeError as e:
        print("Something wrong with attribute")
    for link in bsObj.findAll("a", href=re.compile("^/wiki/")):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                newpage = link.attrs["href"]
                print(newpage, "\n", "-"*20)
                pages.add(newpage)
                get_links(newpage)


get_links("")
