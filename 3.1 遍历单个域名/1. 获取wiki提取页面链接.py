# 链接地址https://en.wikipedia.org/wiki/Kevin_Bacon
from urllib.request import urlopen
from urllib.request import URLError, HTTPError
from bs4 import BeautifulSoup


def scrap_links():
    url = "https://en.wikipedia.org/wiki/Kevin_Bacon"
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        flag = 0
        # 遇到网络问题重试3次
        for i in range(3):
            scrap_links()
            flag += 1
            if html is not "":
                break
        print("flag = {0}".format(flag))
    bsObj = BeautifulSoup(html.read())
    for link in bsObj.findAll("a"):
        if "href" in link.attrs:
            print(link.attrs["href"])


scrap_links()
