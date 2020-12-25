import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

from selenium import webdriver
import time # time.sleep() 용

# 결국 selenium 을 할 경우 Browser를 통해서 가는 것과 동일
# CLI = command line interface -> phantomjs가 쓰여진 이유, Firefox와 Chrome도 사용 가능함

from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument('--headless') # CLI 환경으로 만듬
#
# driver = webdriver.Chrome(chrome_options = chrome_options, executable_path=r'C:\Crawling\Section3\webdriver\chrome\chromedriver')
driver = webdriver.Chrome('C:\Crawling\Section3\webdriver\chrome\chromedriver')

# drvier.set_window_size(900,600)
# driver.implicitly_wait(5)

driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
time.sleep(5)
driver.implicitly_wait(5)

driver.find_element_by_name('id').send_keys('sw993102')
driver.implicitly_wait(5)
time.sleep(3)
driver.find_element_by_name('pw').send_keys('dnfl4fkd@@!')
driver.implicitly_wait(5)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="log.login"]').click()
driver.implicitly_wait(5)
time.sleep(3)
driver.quit()
