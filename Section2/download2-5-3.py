import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

from bs4 import BeautifulSoup

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.google.com">google</a></li>
        <li><a href="http://www.tistory.com">tistory</a></li>
        </ul>
</body></html>
"""
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())

links = soup.find_all('a') # 'a' Tag를 한번에 담음
print('links',type(links))
print(links)

a = soup.find_all('a',string="daum")
print('a >>>',a)
# a >>> [<a href="http://www.daum.net">daum</a>]
b = soup.find_all('a',limit=3)
print('b >>>',b)
# b >>> [<a href="http://www.naver.com">naver</a>, <a href="http://www.daum.net">daum</a>, <a href="http://www.google.com">google</a>]
c = soup.find_all(string=['naver','google'])
print('c >>>',c)
# c >>> ['naver', 'google']

for i in links:
    # print('a',type(a),a)
    href = i.attrs['href']
    txt = i.string
    print('href',href)
    print('txt', txt)
# href http://www.naver.com
# txt naver
# href http://www.daum.net
# txt daum
# href http://www.google.com
# txt google
# href http://www.tistory.com
# txt tistory
