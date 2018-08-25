# 采集wiki页面所有链接(/wiki/)并去重
from urllib.request import urlopen
from urllib.request import URLError, HTTPError
from bs4 import BeautifulSoup
import re

pages = set()


def get_links(new_url):
    global pages
    try:
        html = urlopen("https://en.wikipedia.org" + new_url)
    except (HTTPError, URLError) as e:
        get_links(new_url)
        # 失败重连3次
        for i in range(3):
            if html != "":
                break
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                new_page = link.attrs["href"]
                print(new_page)
                pages.add(new_page)
                get_links(new_page)


get_links("")
