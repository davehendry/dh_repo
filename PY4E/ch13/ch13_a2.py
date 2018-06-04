import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter a URL: ')
# if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_42.json'
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_70858.json'

uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
# print(data)

info = json.loads(data)
print('User count:', len(info["comments"]))

tot = 0
for item in info["comments"]:
    # print('Name', item['name'])
    # print('Count', item['count'])
    x = int(item['count'])
    tot = tot + x
    
print(tot)