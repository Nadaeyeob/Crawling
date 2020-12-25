import sys
import io

import os
import subprocess # python 별도 process로 command 환경을 실행시켜줌

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')
# HTML -> 필요한 텍스트 파싱 -> DB,TXT,엑셀,JSON -> Server



import pytube
# url = input('URL을 입력하세요.')

url = pytube.YouTube('https://www.youtube.com/watch?v=xuhg74nabss')
url.streams
