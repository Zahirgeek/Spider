from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import URLError, HTTPError
import re


def scrap_img_url():
    url = "http://www.pythonscraping.com/pages/page3.html"
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        # 失败重连3次
        for i in range(3):
            scrap_img_url()
            if html is not "":
                break
    bsObj = BeautifulSoup(html.read())
    images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
    for image in images:
        print(image["src"])


scrap_img_url()
