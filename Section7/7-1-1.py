import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 현재 스크롤바 길이 토대로 진행
# youtube URL : https://www.youtube.com/watch?v=UGBgNSoZojs

import time

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

# Chrome Option
chrome_options = Options()

# headless 모드 (Brower 미실행)
# chrome_options.add_argument('--headless')
# Sound Mute
chrome_options.add_argument('--mute-audio')

# webdriver 설정(chrome) - headless
browser = webdriver.Chrome("C:/Users/sw991/Crawling/Section7/webdriver/chrome/chromedriver.exe",options=chrome_options)

# 일반 모드
# browser = webdriver.Chrome("C:/Users/sw991/Crawling/Section7/webdriver/chrome/chromedriver.exe")

# Chrome browser 내부 대기
browser.implicitly_wait(5)
# expected_conditions 을 사용하면 data가 나올때까지 기다릴 수 있음
# Rough 하게 해놓은 상태

# Browser 크기
# minimize_window()
# maximize_window()
browser.set_window_size(800,600)

# Brower 이동
browser.get('https://www.youtube.com/watch?v=UGBgNSoZojs')

# 5초간 대기
time.sleep(5)

# html Focus 주기 위한 코드
# Explicitly wait(명시적 대기)
WebDriverWait(browser,5).until(EC.presence_of_element_located((By.TAG_NAME,'html'))).send_keys(Keys.PAGE_DOWN)

# 2초간 대기
time.sleep(2)

# Page 내용 (시간 오래걸림)
# print('Before Page Contents : {0}'.format(browser.page_source))

# 페이지 이동 시 새로운 데이터 수신 완료위한 대기 시간
scroll_pause_time = 4

# Java Scrpit 사용 - document.documentElement.scrollHeight (Page에서 Console 창에서 해당 명령어 실행)
# python 에서 JS Code를 사용하게끔 해줌
last_height = browser.execute_script('return document.documentElement.scrollHeight')
# IE는 하기와 같은 함수 사용
# last_height = browser.execute_script('return document.body.scrollHeight')

print()
print()

# 모든 댓글 Data가 수신(렌더링) 완료 될 때까지 진행
while True:
    # Scroll 바 이동
    browser.execute_script('window.scrollTo(0,document.documentElement.scrollHeight)') # JS Code 사용

    # 대기
    time.sleep(scroll_pause_time)

    # Scroll 바 이동 -> 새로운 데이터 렌더링 -> 현재 높이를 구한다
    new_height = browser.execute_script('return document.documentElement.scrollHeight')

    # 이전 높이와 신규 높이 비교
    print('Last height : {0}, Current height{1}'.format(last_height,new_height))


    if new_height == last_height:
        break

    # 높이 변경
    last_height = new_height

soup = BeautifulSoup(browser.page_source, 'html.parser')

# 통계 리스트
top_level = soup.select('div#menu-container yt-formatted-string#text')
# 댓글 리스트
comment = soup.select('ytd-comment-renderer#comment')

# HTML 소스 확인
# print(soup.prettify())

print()
print()

# 전체 추천 카운트
print('Total Like Count : {}'.format(top_level[0].text.strip()))
print('Total DisLike Count : {}'.format(top_level[1].text.strip()))

# DOM 반복
for dom in comment:
    print()
    # Image URL 정보
    img_src = dom.select_one('#img').get('src')
    print('thumbnail image urls : {}'.format(img_src if img_src else 'None'))
    # 작성자
    print('author : {}'.format(dom.select_one('#author-text > span').text.strip()))
    # 댓글 본문
    print('content Text : {}'.format(dom.select_one('#content-text').text.strip()))
    # 좋아요
    print('Vote : {}'.format(dom.select_one('#vote-count-middle').text.strip()))
    print()

# Browser 종료
browser.quit()
