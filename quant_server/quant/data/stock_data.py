#from django.utils import timezone as datetime # 处理django的时区问题
import datetime
from data.source.tusharedata import TuShareData
from data.source.baostockdata import BaoStockData
from data.source.dbdata import DBData
import baostock as bs
from utils.tools import *
import pandas as pd
import os
import django
from django.db.models import Avg, Count, Sum
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quant_server.settings")# project_name 项目名称
#django.setup()
from quant.models import StockBasic
from quant.models import Kline_1d

def get_min_pe_ttm_stock(stocks):
    min_pe_ttm = 10000
    min_pe_stock = None
    for itm in stocks:
        if itm.pe_ttm > 0 and min_pe_ttm > itm.pe_ttm and itm.is_st == 0:
            min_pe_ttm = itm.pe_ttm
            min_pe_stock = itm
    return min_pe_stock

if __name__ == '__main__':
    df = BaoStockData.query_trade_dates(start_date="2021-09-30")
    df1 = df.loc[df["is_trading_day"]=='1']
    dates = df1.values.tolist()
    for i,d in enumerate(dates):
        print(d[0])
        #print(df["calendar_date"][i])
        klines = DBData.get_all_kline(d[0],d[0])
        print(get_min_pe_ttm_stock(klines).code)






        #print(i,d[0],DBData.get_all_kline(d[0],d[0]))



#print(BaoStockData.query_history_k_data_plus("sz.000961",'1d'))
