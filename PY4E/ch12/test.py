from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


html = urlopen('http://py4e-data.dr-chuck.net/comments_70855.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tot = 0
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    x = tag.contents[0]
    tot = tot + int(x) 
print(tot)
   