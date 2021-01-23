import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import requests

s = requests.Session()
r = s.get('https://www.naver.com')# put(fetch), delete, get, post
# print('1',r.text) # naver에 있는 page 가져옴 , bs4로 불러올 필요가 없다

# httpbin.org -> html 관해 공부 가능
r = s.get('http://httpbin.org/cookies',cookies={'from' : 'myName'})
print(r.text)
url = 'http://httpbin.org/get'
headers = {'user-agent' : 'mypython_1.0.0'}
r = s.get(url,headers=headers)
# print(r.text)


s.close() # resource 방지 목적

with requests.Session() as s: # close 자동으로 작동
    r = s.get('https://www.naver.com')
    print(r.text)
