# 编写爬虫随意跟随外链跳转
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())


# 获取页面所有内链的列表
def get_internal_links(bsObj, includeUrl):
    # urlparse(scheme = 'https', netloc = 'i.cnblogs.com', path = '/EditPosts.aspx', params = '', query = 'opt=1', fragment = '' ) 协议、位置、路径、参数、查询、片段
    includeUrl = urlparse(includeUrl).scheme + "://" + urlparse(includeUrl).netloc
    internallinks = []
    # 找出所有以"/"开头的链接
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in internallinks:
                if link.attrs["href"].startswith("/"):
                    internallinks.append(includeUrl+link.attrs["href"])
                else:
                    internallinks.append(link.attrs["href"])
    return internallinks


# 获取页面所有外链的列表
def get_external_links(bsObj, excludeUrl):
    externallinks = []
    # 找出所有以"https""http"或"www"开头且不包含当前url的链接
    for link in bsObj.findAll("a", href=re.compile("^(https|http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in externallinks:
                externallinks.append(link.attrs["href"])
    return externallinks


# url以"/"分段写入列表
def split_address(address):
    addressparts = address.replace("https://", "").split("/")
    return addressparts


# 随机跳转,遍历所有的链接
def get_random_external_link(startingpage):
    html = urlopen(startingpage)
    bsObj = BeautifulSoup(html)
    externallinks = get_external_links(bsObj, urlparse(startingpage).netloc)
    if len(externallinks) == 0:
        print("没有获取到外链,准备在内链中找一个")
        domian = urlparse(startingpage).scheme + "://" + urlparse(startingpage).netloc
        internallinks = get_internal_links(bsObj, domian)
        # 返回一个随机内链
        return get_random_external_link(internallinks[random.randint(0, len(internallinks)-1)])
    else:
        # 返回一个随机外链
        return externallinks[random.randint(0, len(externallinks)-1)]


# 输出获取的外链链接
def follow_external_only(startingSite):
    externallink = get_random_external_link(startingSite)
    print("随机获取的外链链接: ", externallink)
    follow_external_only(externallink)


follow_external_only("https://www.oreilly.com")
