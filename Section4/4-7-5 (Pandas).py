import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2020,11,1)
end = datetime.datetime(2020,12,1)

gs_k = web.DataReader('035720','naver',start,end)
gs_n = web.DataReader('035420','naver',start,end)

x = gs_k.index
y1 = gs_k['Open']
y2 = gs_n['Open']

fig = plt.figure('Close_Stock : Kakao vs Naver')
fig.set_size_inches(10,6,forward=True)

plt.plot(gs_k.index,y1,'b',label='kakao')
plt.plot(gs_n.index,y2,'r',label='naver')

plt.legend(loc='upper left')
plt.xlabel('Date')
plt.ylabel('Close')
plt.show()
