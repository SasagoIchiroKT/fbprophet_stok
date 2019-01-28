# ライブラリインポート
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import os

import sys
import pandas as pd # データ格納

import numpy as np
from sklearn import svm
import talib as ta

from fbprophet import Prophet #時系列予測ライブラリ
#Prophetのインストール
#'pip install fbprophet' を実行 

#使用するcsvデータはYahoo Finance より取得.
# https://finance.yahoo.com/quote/2181.T/history?p=2181.T&.tsrc=fin-srch

data = pd.DataFrame()
file_name = sys.argv[1] #GUI.pyから得たカレントパスを取得する
data2 = pd.read_csv(file_name, skiprows=1,header=None,names=['ds','Open','High','Low','Close','y','Volume',''])
print(type(data2['Close']))
print(data2)
data = data.append(data2)


#モデル作成
cap = 3000  #データの最大値
flr = 1.5   #データの最小値

data2['cap'] = cap
data2['flr'] = flr

model = Prophet(growth='logistic')
model.fit(data2)

#描画の設定,何日分出力する、など
future_data = model.make_future_dataframe(periods=250, freq = 'd')
future_data = future_data[future_data['ds'].dt.weekday < 5]

future_data['cap'] = cap
future_data['floor'] = flr

# 予測
forecast_data = model.predict(future_data)

forecast_data['cap'] = cap
forecast_data['floor'] = flr

# 描画
fig = model.plot(forecast_data)
model.plot_components(forecast_data)
plt.legend()

plt.show()