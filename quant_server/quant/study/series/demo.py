import numpy as np
import talib as ta
import matplotlib.pyplot as plt


import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

rs = bs.query_history_k_data_plus("sh.600000",
    "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
    start_date='2000-07-01', end_date='2020-12-31',
    frequency="d", adjustflag="3")
print(rs)

#plt.plot(rs["close"])
bs.logout()
