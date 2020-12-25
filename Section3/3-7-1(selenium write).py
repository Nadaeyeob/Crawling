import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


class NcafewriteAtt:
    # 초기화 실행(webdriver)
    def __init__(self):
        chrome_options = Options()
        # self.chrome_options 를 하면 매번 Self때마다 사용가능하나, 여기서만 쓰기 위해..
        chrome_opetions.add_argumnet('--headless') # CLI (User-agent에 headlessChrome으로 발송됌)
        self.driver = webdriver.Chrome(chrome_options=chrome_opetions, executable_path='C:\Crawling\Section3\webdriver\chrome\chromedriver')
        self.driver.implicitly_wait(5)

    # Naver Cafe Login 및 출석 체크
    def writeAttendCheck(self):
        self.driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
        self.driver.find_element_by_name('id').send_keys('sw993102')
        self.driver.find_element_by_xpath('//*[@id="log.login"]').click()
        self.driver.implicitly_wait(30) # Response가 오면 바로 넘어감
        self.driver.get('https://cafe.naver.com/ArticleList.nhn?search.clubid=29332148&search.menuid=23&search.boardtype=L')
        self.driver.implicitly_wait(30)
        # 여기서부터 수정 필요
        self.driver.switch_to_frame('cafe_main') # IFRAME 이기 떄문에 바꿔줘야함
        self.driver.find_element_by_id('cmtinput').send_keys('반갑습니다.')
        self.driver.find_element_by_xpath('').click()
        time.sleep(3)

    # 소멸자
    def __del__(self):
        # self.driver.close() # 현재 실행 Focus (지금은 IFRAME) 된 영역을 종료
        self.driver.quit() # selenium 전체 프로그램 종료
        print('removed driver object')

if __name__ == '__main__':
    # 객체 생성
    a = NcafewriteAtt()
    # 시작 시간
    start_time = time.time()
    # 프로그램 실행
    a.writeAttendCheck()
    # 종료 시간
    print('---Total %s seconds---' % (time.time() - start_time))

    del a
