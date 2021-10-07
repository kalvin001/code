#from django.utils import timezone as datetime # 处理django的时区问题
import datetime
from data.source.tusharedata import TuShareData
from data.source.baostockdata import BaoStockData
from data.source.dbdata import DBData
import baostock as bs
from utils.tools import *
import os
import django
from django.db.models import Avg, Count, Sum
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quant_server.settings")# project_name 项目名称
django.setup()
from quant.models import StockBasic
from quant.models import Kline_1d


def update_stock_basic():
    res_list = []
    data = TuShareData.stocks_list()
    for row in data.itertuples():
        if row.market is None: continue
        list_date = datetime.datetime.strptime(row.list_date, "%Y%m%d")
        if (row.delist_date != None):
            delist_date = datetime.datetime.strptime(row.delist_date, "%Y%m%d")
        else:
            delist_date = datetime.datetime.strptime("29990101", "%Y%m%d")

        area = row.area if row.area != None else ""
        industry = row.industry if row.industry != None else ""

        if row.is_hs == 'H':
            is_hs = '沪股通'
        elif row.is_hs == 'S':
            is_hs = '深股通'
        else:
            is_hs = ''

        res_list.append(StockBasic(code=row.ts_code, name=row.name, area=area,
                                   market=row.market, exchange=row.exchange, industry=industry, curr_type=row.curr_type,
                                   list_date=list_date, delist_date=delist_date, is_hs=is_hs))
    res = StockBasic.objects.all().delete()
    print("StockBasic Delete=",res)
    res = StockBasic.objects.bulk_create(res_list)
    print("StockBasic Update Size=",len(res))
    return res_list



def update_kline_1d():
    '''

    # "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST"
    # ['2015-01-05', '8.8186086400', '9.0240800000', '8.6409036800', '8.9241209600', '8.7130963200', '513568704',
    # '8182820864.0000', '2', '3.441509', '1', '2.421900', '6.530320', '1.295783', '2.555270', '-9.848905', '0']
    '''
    #Kline_1d.objects.all().delete() #清空数据库
    start = get_cur_timestamp_ms()
    num = 0

    t_cnt = Kline_1d.objects.filter(code="000001.SZ").count()
    latest_trade_date = datetime.datetime.strptime(BaoStockData.query_latest_trade_date(), "%Y-%m-%d")
    bs.login()
    for i,sb in enumerate(StockBasic.objects.all()):
        code = sb.code
        print(i, "code=", code, get_cur_timestamp_ms() - start)
        if not _is_update_kline(code,t_cnt,latest_trade_date): continue

        name = 'sh.' + str(code).split('.SH')[0] if str(code).endswith("SH") else 'sz.' + str(code).split('.SZ')[0]
        kline = BaoStockData.query_history_k_data_plus(name,"1d",start_date="2015-01-01",bs=bs)
        res_list=[]
        for itm in kline.iterrows():
            num+=1
            d = itm[1]
            if d['amount'] =="" or d['psTTM']=="" or d['pbMRQ']=="": continue #脏数据-最后一天ST数据有问题
            res_list.append(Kline_1d(date=datetime.datetime.strptime(d['date'], "%Y-%m-%d"), code=code,
                                     open=d['open'], high=d['high'], low=d['low'], close=d['close'],
                                     preclose=d['preclose'], volume=d['volume'], amount=d['amount'],
                                     adjustflag=d['adjustflag'],
                                     turn=0 if d["turn"] == "" else d["turn"],
                                     tradestatus=d['tradestatus'], pct_chg=d['pctChg'],
                                     pe_ttm=d['peTTM'], pb_mrq=d['pbMRQ'], ps_ttm=d['psTTM'],
                                     pcf_ncf_ttm=d['pcfNcfTTM'], is_st=d['isST']))
            if num%10000==0:
                res=Kline_1d.objects.bulk_create(res_list)
                res_list=[]
                print(num,"Kline_1d bulk_create=", len(res),(get_cur_timestamp_ms()-start))
        res = Kline_1d.objects.bulk_create(res_list)
        print(num, "Kline_1d bulk_create=", len(res), (get_cur_timestamp_ms() - start))




def _is_update_kline(code,kline_t_cnt,latest_trade_date):
    day_cnt = Kline_1d.objects.filter(code=code).count()
    if day_cnt>0 and day_cnt !=kline_t_cnt and Kline_1d.objects.filter(code=code,date=latest_trade_date).count()!=1:
        #大部分是停牌的数据 & 极少数是数据不全的问题
        res = Kline_1d.objects.filter(code=code).delete()
        return True
    elif day_cnt==0:
        return True
    else:
        return False




def test_kline():
    bs.login()
    kline = BaoStockData.query_history_k_data_plus("sh.601360", "1d", start_date="2015-01-01",end_date="2022-01-01",bs=bs)
    #print(kline)
    #Kline_1d.
    res_list = []
    for itm in kline.iterrows():
        d=itm[1]
        print(d)
        if d['amount'] =="": continue
        res_list.append(Kline_1d(date=datetime.datetime.strptime(d['date'], "%Y-%m-%d"),code=d['code'],
                                 open=d['open'],high=d['high'],low=d['low'],close=d['close'],
                                 preclose=d['preclose'],volume=d['volume'],amount=d['amount'],
                                 adjustflag=d['adjustflag'],
                                 turn=0 if d["turn"] == "" else d["turn"],
                                 tradestatus=d['tradestatus'],pct_chg=d['pctChg'],
                                 pe_ttm=d['peTTM'],pb_mrq=d['pbMRQ'],ps_ttm=d['psTTM'],pcf_ncf_ttm=d['pcfNcfTTM'],is_st=d['isST']))

        Kline_1d.objects.bulk_create(res_list)
        res_list=[]
    print(res_list)
#

#update_stock_basic()
#update_kline_1d()
#test_kline()



#print(BaoStockData.query_latest_trade_date())
