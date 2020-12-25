import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import urllib.parse as rep
import requests, json
from bs4 import BeautifulSoup

import urllib.request as req # image 받는 용도
import os

# Log in 할때 preserve Log 하여 무엇이 먼저 나오는지 확인, header에서 확인 가능

# 로그인 유저정보
LOGIN_INFO ={
    'log' : '',
    'pwd' : '',
    'user_submit : 'rep.quote_plust('로그인'),
    'user_cookie' : 1

}

# Session 생성, with 구문안에서 유지

with requests.Session() as s:
    Login_req = s.post('https://www.inflearn.com/',data=LOGIN_INFO)
    # post인지 다른 작업인지도 어떻게 하는지 확인 가능 (header)
    # html 소스 확인
    print('login_req',login_req.text)
    # header 확인
    print('header',login_req.headers)

    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('https://www.inflearn.com/')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, 'html.parser')
        # print(soup.prettyfy())
        badges = soup.select('선택자 입력').find_all('p')
        print(article)
        for i,z in badges:
            print(z)
            fullFileName = os.path.join('c:/',str(i)+'.jpg')
            req.urlretrieve(z['src'],fullFileName)
