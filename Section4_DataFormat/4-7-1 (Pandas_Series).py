import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import pandas as pd
from pandas import Series
import numpy as np

# series1 선언
series1 = Series([92300,94800,88800,75400,92300])
print(series1)
# count
print(series1.count())
# 요약
print(series1.describe())
# Index 접근
print(series1[2])

# series2 선언
series2 = Series([92300,94800,88800,75400,92300], index = ['2010','2011','2012','2013','2014'])
print(series2)
 # Index 순회
for date in series2.index:
    print('year',date)
 # Value 순회
for value in series2.values:
    print('value',value)

# Series3 선언
series_g1 = Series([10,20,30],index=['n1','n2','n3'])
series_g2 = Series([50,40,25],index=['n3','n2','n1'])

# Series 병함
sum = series_g1 + series_g2
mul = series_g1 * series_g2
cul = (series_g1* series_g2) * (0.5+1)

print(sum) # 같은 Index 끼리 sum
print(mul)
print(cul)
