import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')
# HTML -> 필요한 텍스트 파싱 -> DB,TXT,엑셀,JSON -> Server

import urllib.request as req
from urllib.parse import urlparse,urlencode


API = 'http://api.ipify.org'
values = {'format' : 'json'}

print('before',values)
params = urlencode(values)
print('after',params)

url = API + '?' + params
print('요청 URL',url)

reqData = req.urlopen(url).read().decode('utf-8')
print('출력',reqData)

# url + ? + format 으로 주소 생성 이후 urlopen으로 사용
