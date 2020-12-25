import sys
import io
import pytube
import os
import subprocess # python 별도 process로 command 환경을 실행시켜줌

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')
# HTML -> 필요한 텍스트 파싱 -> DB,TXT,엑셀,JSON -> Server

import urllib.request as req
from urllib.parse import urlparse,urlencode

# url도 console 창에서 입력할 수 있게 끔 변경.
# MP3 변환할 것인지? y/n 등으로 표시 할 수 있게끔.

yt = pytube.YouTube('https://www.youtube.com/watch?v=uz6nWl0tyhA')
videos = yt.streams.all()

print('videos',videos)

for i in range(len(videos)):
    print(i,',',videos[i])

cNum = int(input('다운 받을 화질은?(0~21)'))

down_dir = 'C:\youtube'
videos[cNum].download(down_dir) # 화질이 가장 좋은..

newFileName = input('변환할 MP3 파일명은?')
originalName = videos[cNum].default_filename

subprocess.call(['ffmpeg','-i',
    os.path.join(down_dir,originalName),
    os.path.join(down_dir,newFileName)])

print('동영상 다운로드 및 mp3 변환 완료!')

# ffmpeg이 환경변수 지정이 안되어 있기 때문에 youtube 파일에 옮겨줘야함. (Console 창 사용)
