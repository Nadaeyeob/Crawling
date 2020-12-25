import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

from bs4 import BeautifulSoup

html = """
<html>
<body>
<h1>파이썬 BeautifulSoup 공부</h1>
<p>태그 선택자</p>
<p>CSS 선택자</p>
<body>
</html>
"""

print('html',html)
soup = BeautifulSoup(html,'html.parser')
print('soup',type(soup)) # BeautifulSoup Class 형태로 출력
print('prettify',soup.prettify())

h1 = soup.html.body.h1
print('h1',h1)
# h1 <h1>파이썬 BeautifulSoup 공부</h1>
print('h1',type(h1)) # -> Class 형태로 문자형태로 가져온게 아니다.
# h1 <class 'bs4.element.Tag'>
print(h1.string)
# 파이썬 BeautifulSoup 공부

# next_sibling, previous_sibling 으로 상대 접근 가능, 순서 등 바뀌는 경우 문제 발생

p1 = soup.html.body.p
print('p1',p1)
# p1 <p>태그 선택자</p> -> 첫번째 P를 가져왔음
p2 = p1.next_sibling
print('p2',p2)
# 결과값이 안나옴. -> 현재 줄바꿈이 되어 있기 때문에 공백을 가져옴 (/n을 가져온것)
p2 = p1.next_sibling.next_sibling
print('p2',p2)
# p2 <p>CSS 선택자</p>
p3 = p1.previous_sibling.previous_sibling
print('p3',p3)
# p3 <h1>파이썬 BeautifulSoup 공부</h1>

print('h1>>',h1.string)
print('p1>>',p1.string)
print('p2>>',p2.string)
