import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = "http://py4e-data.dr-chuck.net/comments_1498152.xml"
fhandle = urllib.request.urlopen(url).read()

tree = ET.fromstring(fhandle)
#print(tree)
lst = tree.findall('comments/comment')

sum = 0
count = 0
for i in lst:
    number = i.find('count').text
    sum = sum + int(number)
    count = count + 1
print(sum, count)
