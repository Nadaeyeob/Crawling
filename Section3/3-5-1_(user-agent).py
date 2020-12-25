import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# csrf Token, Fake User-agent, Header Payload 처리
# Tocken 값을 Cookie 등에서 확인 한다.
# 최초로 Homepage를 방문해야 Cookie(개발자 도구에서 Application - Cookie)가 생성됌

# 요청 URL
URL = ''

# fake user-agent 생성
ua = UserAgent()
# print(ua.ie)
# print(ua.chrome)
# print(ua.random)

with requests.Session() as s:

    # URL 연결
    s.get(URL) # get 방식으로 Homepage 접근하여 Cookie 받음
    # Login 정보 Payload
    LOGIN_INFO = {
        'identification' : 'id',
        'password' : 'password',
        'csrfmiddlewaretoken' : s.cookies['csrftoken'],
    }
    headers = {
        'User-Agent' : str(ua.chrome),
        'Referer' : 'url1' # referer : 이전 Page의 Log 기록
    }

    # print('headers',s.headers) # user-agent 확인용
    # 요청
    resoponse = s.post(URL,data=LOGIN_INFO, headers = headers)
    # html 결과 확인
    print('response',response.text)

    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text,'html.parser')
        projectList = soup.select('선택자 입력')
        for i in projectList:
            print(i.find('th'.string),i.find('td').text) # string 과 text 차이는?
