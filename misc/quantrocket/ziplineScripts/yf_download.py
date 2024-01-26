# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 16:16:14 2023

@author: MAYANK DANGWAL
"""

from pandas_datareader import data as pdr
import pandas as pd
import yfinance as yf
yf.pdr_override() # <== that's all it takes :-)

symbol = "SPY"
base_folder = r"C:\Users\MAYANK DANGWAL\.zipline\csv\yahoo\daily"
# download dataframe using pandas_datareader
df = pdr.get_data_yahoo(symbol, start="2023-01-01", end="2023-12-10")
df = df.reset_index()
df = df.drop(columns="Close").rename(columns={"Adj Close": "Close"})
df.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
df['dividend'] = 0.0
df['split'] = 1.0
df['date'] = pd.to_datetime(df.date)
print(df.head(2))
file_path = "{}\{}.csv".format(base_folder,symbol)
df.to_csv(file_path, index=False)