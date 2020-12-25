import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')
# HTML -> 필요한 텍스트 파싱 -> DB,TXT,엑셀,JSON -> Server

import urllib.request as req
from urllib.parse import urlparse

url = 'http://www.naver.com'
naver = req.urlopen(url)

print(naver)
# grturl(),info(),getopen()
print(type(naver))

# print(type({}))
# print(type([]))
# print(type(()))

print('geturl',naver.geturl())
print('status',naver.status) # 200, 404, 403, 500 / 200 -> 정상, 404 -> 없음, 403 -> reject 등 나뉨, 후에 status 에 따라서 if 구문등으로 예외처리 필요
print('headers',naver.getheaders())
print('info',naver.info()) #getheaders와 같음
print('code',naver.getcode()) # status와 같음
print('read',naver.read(50).decode('utf-8')) # read(int) 등으로 줄일 수 있음, 옛날 사이트의 경우 euc-kr 로 decode 해서 가져옴
print(urlparse(url))
print(urlparse('http://www.naver.com?test=test'))
