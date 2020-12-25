import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

x = range(0,100)
y1 = [v*v for v in x]
y2 = [v*v*2 for v in x]

# Line chart
ax1.plot(x,y1,'r--')
ax1.plot(x,y2,'d--')
# Bar chart
ax1.bar(x,y2)
ax2.bar(x,y1)
plt.show()
