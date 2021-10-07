from sqlalchemy import create_engine
import pandas as pd
import os
import django
from django.db.models import Avg, Count, Sum
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quant_server.settings")# project_name 项目名称
django.setup()
from quant.models import StockBasic
from quant.models import Kline_1d
import datetime

class DBData:

    _sql_engine = create_engine("postgresql+psycopg2://postgres:k135792684@localhost:5432/quant", echo=False)

    def __init__(self):
        pass
        #self.sql_engine = create_engine("postgresql+psycopg2://postgres:k135792684@localhost:5432/quant",echo=False)


    @staticmethod
    def k_line_daily(code=None, start_date="", end_date=""):
        sql = "select * from stock_trade_daily where ts_code='" + code + "'"

        if start_date != "":
            sql += " and trade_date>='" + start_date +"'"
        if end_date != "":
            sql += " and trade_date<='" + end_date +"'"
        #print(sql)
        df = pd.read_sql_query(sql, con=DBData._sql_engine)
        return

    @staticmethod
    def get_all_kline(start_date=None,end_date=None):

        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        #print(len(Kline_1d.objects.filter(date__range=(start_date,end_date))))
        return Kline_1d.objects.filter(date__range=(start_date,end_date))

    @staticmethod
    def get_kline(code,start_date=None,end_date=None):

        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        return Kline_1d.objects.filter(code=code,date__range=(start_date, end_date))


if __name__ == '__main__':
    print(DBData.get_kline("000001.SZ","2021-09-30","2021-09-30")[0].close)

#print(DB_Data().k_line_daily(code=str("000002.SZ"),start_date="2015-01-01",end_date="2022-01-01"))