# 链接地址https://en.wikipedia.org/wiki/Kevin_Bacon
from urllib.request import urlopen
from urllib.request import URLError, HTTPError
from bs4 import BeautifulSoup

# 爬取所有的链接
# def scrap_links_v1():
#     url = "https://en.wikipedia.org/wiki/Kevin_Bacon"
#     try:
#         html = urlopen(url)
#     except (HTTPError, URLError) as e:
#         flag = 0
#         # 遇到网络问题重试3次
#         for i in range(3):
#             scrap_links_v1()
#             flag += 1
#             if html is not "":
#                 break
#         print("flag = {0}".format(flag))
#     bsObj = BeautifulSoup(html.read())
#     for link in bsObj.findAll("a"):
#         if "href" in link.attrs:
#             print(link.attrs["href"])
#
#
# scrap_links_v1()

# 一个函数getLinks,可以用维基百科词条 /wiki/<词条名称>形式的URL链接作为参数,然后以同样的形式返回一个列表,里面包含所有的词条URL链接.
# 一个主函数,以某个起始词条为参数调用getLinks,再从返回的URL列表里随机选择一个词条链接,再调用getLinks,知道我们主动停止,或者在新的页面上没有词条链接了,程序才停止运行.
import datetime
import random
import re

random.seed(datetime.datetime.now())

def get_links(articleUrl):
    html = urlopen("https://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


links = get_links("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = get_links(newArticle)
