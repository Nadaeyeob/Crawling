import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import os # 파이썬을 쓰고있는 OS에 접근해서 명령어 실행

# Volume / Variety / Velocity

base = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
quote = rep.quote_plus('아이유')
url = base + quote

print(url)

res = req.urlopen(url)
savePath = 'C:\Crawling\Section2\Image\\' # \\로 넣어야함을 주의하자

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
# 이미 있을 시 발생되는 Error
except OSError as e:
    if e.errno != errno.EEXIST:
        print('폴더 만들기 실패!')
        raise

soup = BeautifulSoup(res, 'html.parser')
print('------')
# print(soup)
print('------')
img_list = soup.select('img')
print(img_list[49])
print(img_list[50]) # Data-Source가 없음

value = img_list[0].get('data-source')
print(value)
value = img_list[50].get('data-source')
print('50 = ',value)
value = img_list[51].get('data-source')
print('51 = ',value)

# -> 해당 원소가 없는 경우 어떻게 삭제 할 수 있는지 공부 필요
# 이번 case는 img_list 내 Element에 data-source 가 없는 경우

print('------')
print(len(img_list))
i = 0
for a in img_list:
    val = a.get('data-source')
    if val == None:
        i+=1
        continue

print(i)
# Error가 나는 이유 -> 자꾸 동기화 시켜서 index를 부족하게 만듬

print(len(img_list))
print('------')


for i, a in enumerate(img_list,1):
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    req.urlretrieve(a['data-source'],fullFileName)

print('DownLoad Complete')
