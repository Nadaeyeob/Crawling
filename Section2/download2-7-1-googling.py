import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import json
import urllib.request as req
from fake_useragent import UserAgent

ua = UserAgent()

headers = {'User-Agent': ua.chrome,
            'referer' : 'https://finance.daum.net/'}

url = 'https://finance.daum.net/api/search/ranks?limit=10'
res = req.urlopen(req.Request(url, headers = headers)).read().decode('UTF-8')
print(res)
