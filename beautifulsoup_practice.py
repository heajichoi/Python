

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
href = soup('a')

count = int(input('Enter count'))+1
position = int(input('enter position'))
tags = href[position:position+count]
lst = list()
for i in tags:
    a = i.get('href',None)
    lst.append(a)
print(lst)
for i in range(0,count):
    print ('retrieving: ',lst[position])
    position = position + 1
