#因子统计分析
from market import Market
from backtest import BackTest, backtest_save, plot_asset, plot_signal
from utils.dingtalk import DingTalk
from utils.sendmail import sendmail
from utils.logger import logger
from utils.storage import txt_read, txt_save, save_to_csv_file, read_csv_file
from utils.tools import *
from config import config
from indicators import *
from data.source.dbdata import *
#import talib


def get_k_lines():
    for i,item in enumerate(Market.stocks_list().iterrows()):
        print(item[1]["market"])
        if str(item[1]["market"]) not in ["中小板","主板"]:
            continue
        ts_code = item[1]["ts_code"]
        if str(ts_code).endswith(".SH"):
            name = "sh" + str(ts_code).replace(".SH", "")
        else:
            name = "sz" + str(ts_code).replace(".SZ", "")
        print(get_localtime(),i, ts_code)
        #Market.kline(name,"1d","2",start_date="2015-01-01",end_date="2022-01-01")

        DBData.k_line_daily(str(ts_code),start_date="2015-01-01",end_date="2022-01-01")


get_k_lines()

if "sd" not in ["sd","aa"]:
    print("11")
else:
    print("222")