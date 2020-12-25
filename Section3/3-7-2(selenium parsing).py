import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

class Ncafeparsing:
    # 초기화 실행(webdriver)
    def __init__(self):
        chrome_option = Options()
        chrome_option.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_option, executable_path='C:\Crawling\Section3\webdriver\chrome\chromedriver')
        self.driver.implicitly_wait(5)

    def getinformation(self):
        self.driver.get('https://cafe.naver.com/ArticleList.nhn?search.clubid=29332148&search.menuid=5&search.boardtype=L')
        self.driver.implicitly_wait(30)
        self.driver.switch_to.frame("cafe_main")
        # self.driver.find_element_by
        soup = BeautifulSoup(self.driver.page_source,'html.parser')
        return soup.select('div.board-list > div.inner_list > a.article')

    def printlist(self,list):
        for i in list:
            print(i.contents[2].strip())


    def __del__(self):
        self.driver.quit()
        print('removed driver object')

if __name__ == '__main__':
    # 객체 생성
    a = Ncafeparsing()
#     # 시작 시간
    start_time = time.time()
#     # 프로그램 실행
    a.printlist(a.getinformation())
#     # 종료 시간
    print('---Total %s seconds---' % (time.time() - start_time))

    del a
