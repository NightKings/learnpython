#conding:utf-8
import urllib.request,re
from bs4 import BeautifulSoup
url = 'http://www.baidu.com'
html = urllib.request.urlopen(url,timeout=60)
soup = BeautifulSoup(html,"html.parser")
find_hred = soup('a')
for x in find_hred:
    print(x['href'])