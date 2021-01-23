import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime

# 조회 시작 날짜
start = datetime.datetime(2020,9,1)
end = datetime.datetime(2020,12,16)

GS = web.DataReader('035720','naver',start,end)
print(GS)

import matplotlib.pyplot as plt
x = range(0,256)
print(x)

# List 범위 (y축)
y = [v*v for v in x]
# for v in x:
#     y.append(v*v)
# print(y)

plt.plot(x,y)
plt.show()
plt.plot(x,y,'r--')
