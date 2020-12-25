import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')
# HTML -> 필요한 텍스트 파싱 -> DB,TXT,엑셀,JSON -> Server

import urllib.request as dw

imgUrl = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA3MDlfNDgg%2FMDAxNTk0MjYxOTAwODg5.JIZsWvEHASyqn-kLXMcXp6UNK7xWZhxZ52wqiqM9KcAg.J1Yi-dIM94OT0YIlkHzDC4jasCrvmPiNQQnUxu8vxP8g.JPEG.jjh4775%2Fbandicam_2020-07-09_11-25-56-490.jpg&type=sc960_832'
htmlUrl = 'http://google.com'
savePath1 = 'c:/Crawling/Section2/test1.jpg'
savePath2 = 'c:/crawling/Section2/index.html'

# urllib.request.urlretrieve(imgUrl,savePath1)
# urllib.request.urlretrieve(htmlUrl,savePath2)

f1 = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlUrl).read()
savefile1 = open(savePath1,'wb') # w : write, r : read, a : add (file 끝 부분부터 data 추가)
savefile1.write(f1)
# Resource 반납
savefile1.close()


# with를 쓰면 close가 알아서 적용됌
# with가 무엇인지 확인 필요
with open(savePath2,'wb') as savefile2:
    savefile2.write(f2)

# urlretrieve : (Direct 저장) 저장 -> Open('r') -> 파싱 -> 저장
# urlopen : 저장하기 전에 변수 할당 -> 파싱 -> 저장


print('다운로드 완료')
