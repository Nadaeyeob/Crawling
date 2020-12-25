import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import requests, json

# API 란? -> 확인 필요
# RestFul, Rest API -> URI 로 Resouce 위치 명시, Method : 명시 -> 주소만 봐도 어떤 Action을 하는지 알 수 있게끔..
# get, post, put(fetch), delete

# https://www.apistore.co.kr/api/apiList.do -> xml,json,rss.. 등등 기타 모듈로 가져와서 실습 가능

# r = requests.get('https://api.github.com/events')
# r.raise_for_status() # error가 발생했을 때 예외처리를 하여 Error 파악을 해줌
# print(r.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('name','kim',domain='httpbin.org',path='/cookies')

# r = requests.get('http://httpbin.org/cookies',cookies=jar) # cookie로 request 하여 response 받음
# r.raise_for_status()
# print(r.text)

# r = requests.get('https://github.com',timeout=5) # -> 너무 많은 접근을 방지, 5s 기다린다는 의미
# print(r.text)

# Post = Data를 Server에 저장하는 방법

# r = requests.post('http://httpbin.org/post',data={'name':'kim'}, cookies = jar)
# print(r.text)

payload1 = {'key1' : 'value1', 'key2' : 'value2'}
payload2 = (('key1','value1'),('key2','value2'))

# r = requests.post('http://httpbin.org/post', data=payload1) # form data 로 보냄
# print(r.text)

payload3 = {'some' : 'nice'}
r = requests.post('http://httpbin.org/post', data=json.dumps(payload3)) # json 으로 data를 보냄
print(r.text)
