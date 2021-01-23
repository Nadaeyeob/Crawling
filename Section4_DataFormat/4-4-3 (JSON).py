import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import simplejson as json
import urllib.request as req
import os.path

# https://api.github.com/repositories

#url
url = 'https://api.github.com/repositories'
# 경로와 & 파일명
savename = 'c:/crawling/section4/repo.json'

if not os.path.exists(savename):
    req.urlretrieve(url,savename)

# downlaod 이후 작업, download 하지 않고 바로 끌어오는 방법은?
items = json.load(open(savename,'r',encoding='utf-8'))
# items = json.loads(open(savename,'r',encoding='utf-8')).read()

for item in items:
    print(item['full_name']+' - '+item['owner']['url'])
