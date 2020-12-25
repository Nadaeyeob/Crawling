import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

from bs4 import BeautifulSoup

# CSS scraping 하는 방법으로 가장 많이 쓰임
# https://www.w3schools.com/cssref/trysel.asp -> CSS Selector 공부

html = """
<html><body>
<div id = 'main'>
    <h1>강의목록</h1>
    <ul class = 'lecs'>
        <li> Java 초고수 되기</li>
        <li> 파이썬 기초 프로그래밍</li>
        <li> 파이썬 머신러닝 프로그래밍</li>
        <li> 안드로이드 블루투스 프로그래밍</li>
    </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html,'html.parser')
h1 = soup.select('div#main > h1')
print('h1',h1)
# h1.string의 경우 Error가 나옴. Type 확인시 List class임
for z in h1:
    print(z.string)
# or soup.select_one() method 를 사용한다
list_li = soup.select('div#main > ul.lecs > li')
for li in list_li:
    print(li.string)
