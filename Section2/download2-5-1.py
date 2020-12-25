import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')
# HTML -> 필요한 텍스트 파싱 -> DB,TXT,엑셀,JSON -> Server

# HTML : 태그, 요소, 속성 등

from urllib.parse import urljoin

baseurl = 'http://test.com/html/a.html'
print('<<',urljoin(baseurl,'b.html'))
# << http://test.com/html/b.html a.html 이 b.html 로 치환됌
print('<<',urljoin(baseurl,'sub/b.html'))
# << http://test.com/html/sub/b/html 절대경로까지 놔두고 나머지는 치환됌
print('<<',urljoin(baseurl,'../index.html'))
# << http://test.com/index.html
print('<<',urljoin(baseurl,'../img/img.jpg'))
# << http://test.com/img/img.jpg
print('<<',urljoin(baseurl,'../css/img.css'))
# << http://test.com/css/img.css
