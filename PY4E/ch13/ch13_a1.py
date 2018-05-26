import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl 

# # Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter a URL: ')
# if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_70857.xml'
#  uh = urllib.request.urlopen(url)
#     data = uh.read()
#     print('Retrieved', len(data), 'characters')
    # print(data.decode())
xml = urlopen(url, context=ctx).read()
print(len(xml))

stuff = ET.fromstring(xml)
lst = stuff.findall('comments/comment')
print('Comment count:', len(lst))

tot = 0
# counts = stuff.findall('.//count')
# print(counts)
for item in lst:
    # print('Name', item.find('name').text)
    # print('Count', item.find('count').text)
    x = int(item.find('count').text)
    tot = tot + x
    
print(tot)




