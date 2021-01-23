import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import requests

# Response
s = requests.Session()
r = s.get('http://httpbin.org/get')
print(r.status_code) # Server 상태
print(r.ok)

# http://jsonplaceholder.typicode.com

r = s.get('http://jsonplaceholder.typicode.com/posts/1')
# print(r.text)
print(r.json()) # json 형태로 converter하므로 python 코드를 사용 가능하게됌
print(r.json().keys())
print(r.json().values())
print(r.encoding) # encoding type을 찾을 수 있음
print(r.content) # binary 형태
print(r.raw)

s.close()
