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

# 한글 코드 변환
# import urllib.parse as rep
# quote = rep.quote_plus('나대엽')
# print(quote)
# url = url1 + quote

url = 'https://www.inflearn.com/'
res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser')

recommand = soup.select("div.recent_courses_content > div > div > div.swiper-wrapper > div > div > a > div.card-content > div.course_title")
print(type(recommand))
print(len(recommand))
print('---')
print(recommand)
print('---')

i = 1
for e in recommand:
    print(i,e.string)
    i+= 1

# 배울 점, 무조건 자식 까지 다 내려가줘야 받을 수 있다. (최소단위까지 쪼개줘야함)
