import urllib
import json
import re
from bs4 import BeautifulSoup

file_name = "links.txt"

with open(file_name, 'r') as f:
    for line in f:
        _html = urllib.request.urlopen(line).read()
        _soup = BeautifulSoup(_html, features='lxml')
        _script = _soup.findAll('script')[10].string
        _data = re.search(r"packages:\s(.*)", _script).group(1)
        _json = json.loads(_data[:-1])
        for i in _json:
            print("{} - {} - Available: {}".format(i['download_artist'], i['title'], i['origins'][0]['quantity_available']))
