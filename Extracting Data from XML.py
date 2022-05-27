# Extracting Data from XML

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_687797.xml'

uh = urllib.request.urlopen(url)
data = uh.read()

tree = ET.fromstring(data)

lst = tree.findall('comments/comment/count')

counts = tree.findall('.//count')
count = 0
sum = 0

for each in counts:
    print(each.text)
    x = int(each.text)
    count = count +1
    sum = sum + x

print("Count:", count)
print("Sum:",sum)














#import urllib.request
#import xml.etree.ElementTree as ET

#url = input("Enter - ")
#uh = urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
#data = url.read()

#tree = ET.fromstring(data)
#results = tree.findall('comments/comment')
#count = 0
#sum = 0

#for item in results:
    #x = int (item.find('count').text)
    #count = count+1
    #sum = sum+x
#print("Count:", count)
#print("Sum:", sum)
