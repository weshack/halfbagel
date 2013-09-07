from BeautifulSoup import BeautifulSoup
import re
import urllib
import requests
import json
link="http://www.wesleyan.edu/reslife/ugrad_housing/res_halls.html"
link2="http://www.wesleyan.edu/reslife/housing/residence/156_High.htm"
f = requests.get(link2)
soup = BeautifulSoup(''.join(f))
soup = soup.prettify()

s = re.findall('<p>', soup)
lines = soup.splitlines()
n=0

    
    
print lines

