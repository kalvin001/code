import tushare as ts
import sys
import os
from quant.models import StockBasic
from django.utils import timezone
import datetime
import json
from sqlalchemy import create_engine




ts.set_token('5d2773294dea485e06d949f132e3cf6a620a83fc3b46ee08a03b007d')
pro = ts.pro_api()

sql_engine = create_engine("postgresql+psycopg2://postgres:k135792684@localhost:5432/quant",echo=False)



#stock baisc 
def stock_basic():
    res_list = []
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,market,exchange,industry,curr_type,list_status,list_date,delist_date,is_hs')
    
    for row in data.itertuples():
        list_date = datetime.datetime.strptime(row.list_date,"%Y%m%d")
        if(row.delist_date !=None):
            delist_date = datetime.datetime.strptime(row.delist_date,"%Y%m%d")
        else:
            delist_date = datetime.datetime.strptime("29990101","%Y%m%d")

        area=row.area if row.area != None else  ""
        industry=row.industry if row.industry != None else  ""

        if row.is_hs == 'H':
            is_hs = '沪股通'
        elif row.is_hs == 'S':
            is_hs = '深股通'
        else:
            is_hs = ''

        res_list.append(StockBasic(code=row.ts_code,name=row.name,area=area,
                market=row.market,exchange=row.exchange,industry=industry,curr_type=row.curr_type,
                list_date=list_date,delist_date=delist_date,is_hs=is_hs))

    return res_list

def daily_trade():
    data = pro.stock_basic(exchange='', list_status='L')
    if_exists ='replace'
    for index,itm in data.iterrows():
        try:
            if index!=0:
                if_exists = 'append'
            print(index,itm["ts_code"])
            df = ts.pro_bar(ts_code=itm["ts_code"], adj='qfq',start_date='20140101', end_date='20220501') #前复权
            df.to_sql(name="stock_trade_daily", con=sql_engine, if_exists=if_exists)
        except Exception:
            print("error--",itm)


