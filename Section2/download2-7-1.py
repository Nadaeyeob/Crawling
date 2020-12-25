import sys
import io
import json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

from bs4 import BeautifulSoup
import urllib.request as req
import requests
from fake_useragent import UserAgent

ua = UserAgent()
# Daum 금융 시가 총액 상위 종목 가져오기
# Naver 금융 TOP 10 종목 가져오기
# 인프런 추천강좌 10개 가져오기
# 네이버 실시간 인기 검색어 + link 스크랩핑 하기

#URL -> res로 open -> soup로 만들어줌

url = 'https://finance.daum.net/api/search/ranks?limit=10'
headers = {'User-Agent': ua.chrome,
            'referer' : 'https://finance.daum.net/'}
res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')
print(res)
print(type(res))
# json Data로 바꿔줘야지 사용 가능
rank_json = json.loads(res)['data']
print(rank_json)
print(type(rank_json))

for elm in rank_json:
    print('{0}'.format(elm['name']))

# 실습 코드 , # 선택자가 중요함을 잘 이해하자

url = 'https://finance.daum.net'
res = req.urlopen(url).read()
soup = BeautifulSoup(res,'html.parser')
top = soup.select('u#topMyListNo1 > li')

for i,e in enumerate(top):
    print(i,",",e.find("a").string)

for i,e in enumerate(top,1):
    print(i,",",e.find('a').string,':',e.find('span').string)
