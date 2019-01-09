# ライブラリインポート
import pandas as pd # データ格納
import matplotlib.pyplot as plt #描画
from fbprophet import Prophet #時系列予測ライブラリ
from fbprophet import diagnostics
#Prophetのインストール
#'pip install fbprophet' を実行 

#使用するcsvデータはYahoo Finance より取得.
# https://finance.yahoo.com/quote/2181.T/history?p=2181.T&.tsrc=fin-srch

def nfl_sunday(ds):
    date = pd.to_datetime(ds)
    if date.weekday() == 6 and (date.month > 8 or date.month < 2):
        return 1
    else:
        return 0

data = pd.DataFrame()
file_name = 'AMZN.csv'
data2 = pd.read_csv(file_name, skiprows=1,header=None,names=['ds','Open','High','Low','Close','y','Volume'])
print(type(data2['Close']))
print(data2)
data = data.append(data2)

#モデル作成
cap = 3000  #データの最大値
flr = 1.5   #データの最小値

data2['cap'] = cap
data2['flr'] = flr

model = Prophet(growth='logistic',n_changepoints=5)
cv = diagnostics.cross_validation(model,horizon='365 days')
cv.tail()

some_mape = cal_some_mape(model)

some_mape.plot(x='horizon')

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