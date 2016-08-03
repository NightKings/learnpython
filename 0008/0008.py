#conding:utf-8
import urllib.request,re
from bs4 import BeautifulSoup
url = 'http://www.luxiaochen.com/?p=292'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html,"html.parser")
print(soup.body.text)