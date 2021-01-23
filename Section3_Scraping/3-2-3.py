import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import requests, json

# Response
s = requests.Session()
r = s.get('http://httpbin.org/stream/20')
# r = s.get('http://httpbin.org/stream/20', stream=True)

# print(r.text)
# print(r.encoding) # -> None
# print(r.json()) -> error 발생

if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    # print(line)
    b = json.loads(line) # dict 형태
    for e in b.keys():
        print('key = ',e,'value = ',b[e])
