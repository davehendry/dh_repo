from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
html = urlopen('http://www.investorguide.com/stock-by-letter.php?letter=A', context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags

tags = soup.find('div')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)


# for i, row in enumerate(soup.find('div', id = 'alpha-ticker').find_all('tr')):
#     row_data = []
#     cells = row.find_all('td')
#     # print('TAG:', row)
#     # print('URL:', row.get('class', None))
#     # print('Contents:', row.contents[0])
#     if i > 5:
#         break
   