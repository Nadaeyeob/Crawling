import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

from bs4 import BeautifulSoup

# 인터넷 상에서 retreive 받아왔다고 가정
fp = open('c:/Crawling/Section2/food_list.html', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')

print('1', soup.select_one('li:nth-of-type(4)').string) # 왜 이걸로 하면 8번째가 안나오지?
print('2', soup.select_one('#ac-list > li:nth-of-type(4)').string)
print('2.1', soup.select_one('#ac-list'))
print('3', soup.select('#ac-list > li[data-lo="cn"]')[0].string)
print('4', soup.select('#ac-list > li.alcohol.high')[0].string)

param = {'data-lo' : 'cn', 'class' : 'alcohol'}
print('5', soup.find('li',param).string)
print('6', soup.find(id='ac-list').find('li',param).string)

for ac in soup.find_all('li'):
    if ac['data-lo'] == 'us':
        print('data-lo == us', ac.string)
