from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        url = urlopen(url)
    # 如果HTTPError和URLError分开捕获,将HTTPError放在URLError的前面，因为HTTPError是URLError的一个子类
    except (HTTPError, URLError) as e:
        return None
    try:
        html = BeautifulSoup(url.read())
        title = html.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://blog.csdn.net/c406495762/article/details/59488464")
if title == None:
    print("Title couldn't be found")
else:
    print(title)
