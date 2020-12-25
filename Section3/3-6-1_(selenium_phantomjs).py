import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

from selenium import webdriver

driver = webdriver.PhantomJS('C:\Crawling\Section3\webdriver\phantomjs\phantomjs')

driver.implicitly_wait(5)

driver.get('https://google.com')

driver.save_screenshot('c:\Crawling\Section3\website1.png')

driver.implicitly_wait(5) # 암묵적으로 5초간 대기

driver.get('https://www.daum.net')

driver.save_screenshot('c:\Crawling\Section3\website2.png')

driver.quit()

print('스크린샷 완료')
