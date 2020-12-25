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
# Daum 금융 시가 총액 상위 종목 가져오기 -> ajax
# Naver 금융 TOP 10 종목 가져오기 -> ajax
# 인프런 추천강좌 10개 가져오기
# 네이버 실시간 인기 검색어 + link 스크랩핑 하기

url = 'https://finance.naver.com/'
res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser')

# print(soup)

top5 = soup.select('#content > tr')

for e in top5:
    print(e)

for e in top10:
    print(e.find('a')) # -> a구문이 없으면 None 반환

for e in top10:
    if e.find('a') is not None:
        print(e.find('a'))
