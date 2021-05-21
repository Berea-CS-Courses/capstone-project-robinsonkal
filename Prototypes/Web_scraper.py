from bs4 import BeautifulSoup
import re
from urllib.request import Request, urlopen
import requests

url = 'https://boards.4channel.org/v/'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)

output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head',
    'input',
    'script',
    # there may be more elements you don't want, such as "style", etc.
]

for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)

print(output)
v=0
file1 = open("textfile.txt","a")
for i in output:
    file1.write(output)
    #v+=1
    #if v == 713:
    #   print (i)

#file1 = open("textfile.txt","w")
#file1.write(output)

#file1.close()
