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
data2 = pd.read_csv(file_name, skiprows=1,header=None, names=['ds','Open','High','Low','Close','y','Volume'])
print(type(data2['Close']))
print(data2)
data = data.append(data2)

#指標追加
def nfl_sunday(ds,y):
    date = pd.to_datetime(ds)
    end = pd.to_datetime(y)

data['nfl_sunday'] = data['ds'].apply(nfl_sunday)

#モデル作成
model = Prophet()

#指標の追加
model.add_regressor('nfl_sunday')

model.fit(data)

#描画の設定,何日分出力する、など
future_data = model.make_future_dataframe(periods=250, freq = 'd')
future_data = future_data[future_data['ds'].dt.weekday < 5]

future_data['nfl_sunday'] = future_data['ds'].apply(nfl_sunday)

# 予測
forecast_data = model.predict(future_data)

# 描画
fig = model.plot(forecast_data)

model.plot_components(forecast_data)

plt.legend()

plt.show()
