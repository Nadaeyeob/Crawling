import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')
# HTML -> 필요한 텍스트 파싱 -> DB,TXT,엑셀,JSON -> Server

import urllib.request

imgUrl = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA3MDlfNDgg%2FMDAxNTk0MjYxOTAwODg5.JIZsWvEHASyqn-kLXMcXp6UNK7xWZhxZ52wqiqM9KcAg.J1Yi-dIM94OT0YIlkHzDC4jasCrvmPiNQQnUxu8vxP8g.JPEG.jjh4775%2Fbandicam_2020-07-09_11-25-56-490.jpg&type=sc960_832'
htmlUrl = 'http://google.com'
savePath1 = 'c:/Crawling/Section2/test1.jpg'
savePath2 = 'c:/crawling/Section2/index.html'

urllib.request.urlretrieve(imgUrl,savePath1)
urllib.request.urlretrieve(htmlUrl,savePath2)

print('다운로드 완료')
