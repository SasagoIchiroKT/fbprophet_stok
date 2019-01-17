import matplotlib
#matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import os
import pandas as pd
import numpy as np
from sklearn import svm
import talib as ta
ta.get_function_groups


filename = 'TOYOTA.csv' # 日経平均株価データ
df = pd.read_csv(filename,index_col='date', parse_dates=True)
df.index = pd.to_datetime(df.index)

print(df)
print(df.index)
closed = df.asfreq('B')['Adj Close'].dropna() # 調整後終値を抽出
#stday = df.asfreq('B')['date'].dropna()


prices = np.array(closed, dtype='f8') # 浮動小数点数による NumPy 配列にしておく
#date = np.array(stday, dtype='f8') #浮動小数点数による NumPy 配列にしておく

# 5 日単純移動平均を求める
sma5 = ta.SMA(prices, timeperiod=5)

# RSI (14 日) を求める
rsi14 = ta.RSI(prices, timeperiod=14)

# MACD (先行 12 日移動平均、遅行 26 日移動平均、 9 日シグナル線) を求める
macd, macdsignal, macdhist = ta.MACD(prices,fastperiod=12, slowperiod=26, signalperiod=9)
fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d\n%H:%M'))

plt.plot(df.index, sma5)
plt.plot(df.index, rsi14)
plt.plot(df.index, macd)
plt.plot(df.index, macdsignal)
plt.plot(df.index, macdhist)


    # プロット表示(設定の反映)
plt.show()