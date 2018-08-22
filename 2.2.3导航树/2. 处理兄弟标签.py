from urllib.request import urlopen
from urllib.request import URLError, HTTPError
from bs4 import BeautifulSoup


def get_siblings():
    try:
        html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    except (HTTPError, URLError) as e:
        # 失败重连3次
        for i in range(3):
            get_siblings()
            if html not in "":
                break
            else:
                print(e)
    else:
        bsObj = BeautifulSoup(html)

    # 获取网页中id为giftList中的兄弟标签
    for child in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
        print(child)

get_siblings()