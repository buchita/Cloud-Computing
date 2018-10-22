# The given code

from urllib.request import Request, urlopen
from json import loads
import json
url = 'https://swapi.co/api/people'
req = Request(url, None, {
    'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
})

data = loads(urlopen(req).read().decode("utf-8"))

print(data)
