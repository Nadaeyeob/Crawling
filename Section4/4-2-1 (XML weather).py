import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

# HTML : 지정된 태그 (DIV,P,BR)
# 기상청 http://www.weather.go.kr/weather/lifenindustry/sevice_rss.jsp

# Text + Console 로 최저온도 확인

import urllib.request as req
from bs4 import BeautifulSoup
import os.path

# 다운로드 URL
url = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
savename = 'c:/crawling/Section4/forecast.xml'

if not os.path.exists(savename):
    req.urlretrieve(url, savename)
    print('Download forecast')

# BeautifulSoup parsing
xml = open(savename, 'r', encoding = 'utf-8').read()
soup = BeautifulSoup(xml, 'html.parser') # XML = SGML + HTML로 만든 것이기 때문에 HTML로 가능

# 지역확인
info = {}
for location in soup.find_all('location'): # css 선택자가 아니기 떄문에 Find_all 가능
    loc = location.find('city').string
    tmns = location.find_all('tmn')
    tmxs = location.find_all('tmx')

    if not (loc in info):
        info[loc] = []
    for tmn in tmns:
        info[loc].append(tmn.string)

# print(info.keys())
# print(list(info.keys()))
# print(info.values())


# 각 지역별 날씨 텍스트 쓰기
with open('c:/crawling/Section4/forcast.txt','wt') as f:
    for loc in sorted(info.keys()):
        print('+',loc)
        f.write(str(loc)+'\n')
        for n in info[loc]:
            print('-',n)
            f.write('\t'+str(n)+'\n')
