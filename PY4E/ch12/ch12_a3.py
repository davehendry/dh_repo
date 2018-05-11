import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl 

# # Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter a URL: ')
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/known_by_Lucille.html'
count = input('Enter a count: ')
position = input('Enter a position: ')
print('Retrieving:', url)
repeat_count = 0
while repeat_count < int(count):
    repeat_count = repeat_count + 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    link_pos = 0
    tags = soup('a')
    for tag in tags:
        link_pos = link_pos + 1
        if link_pos == int(position):
            x = tag.get('href', None)
            url = x
            if repeat_count < int(count):
                print('Retrieving:', url)
            else:
                print('Final link:', url)                
        else:
            continue