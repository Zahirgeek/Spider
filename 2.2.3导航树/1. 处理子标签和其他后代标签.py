# 找出网页中giftList子标签
from urllib.request import urlopen
from urllib.request import URLError, HTTPError
from bs4 import BeautifulSoup


def get_children():
    try:
        html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    except (HTTPError, URLError) as e:
        # 失败重连3次
        for i in range(3):
            get_children()
            if html not in "":
                break
            else:
                print(e)
    else:
        bsObj = BeautifulSoup(html)

    # 获取网页中id为giftList中的子标签
    for child in bsObj.find("table", {"id": "giftList"}).children:
        print(child)
    # 获取网页中id为giftList中的后代标签
    # for child in bsObj.find("table", {"id": "giftList"}).descendants:
    #     # 一行显示
    #     print(child, end=" ")


get_children()
