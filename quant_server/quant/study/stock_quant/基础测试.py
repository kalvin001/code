from market import Market
from backtest import BackTest, backtest_save, plot_asset, plot_signal
from utils.dingtalk import DingTalk
from utils.sendmail import sendmail
from utils.logger import logger
from utils.storage import txt_read, txt_save, save_to_csv_file, read_csv_file
from utils.tools import *
from config import config
from indicators import *
#import talib

config.loads('config.json')			# 载入配置文件®®®


for i,item in enumerate(Market.stocks_list()["ts_code"]):
    if str(item).endswith(".SH"):
        name = "sh" + str(item).replace(".SH", "")
    else:
        name = "sz" + str(item).replace(".SZ", "")
        print(i, name)
    Market.kline(name,"1d","2",start_date="2015-01-01",end_date="2022-01-01")


#print(Market.stocks_list())
#tick = Market.tick("sh601003")
#print(tick.symbol,tick.last,tick.timestamp)

#print(len(Market.kline("sh601003","1d")))
#print(Market.shanghai_component_index())
#print(Market.shenzhen_component_index())
#print(Market.stocks_list())
#print(Market.new_stock())

#print(sendmail("test kalvin"))

save_to_csv_file("ddd","./test.txt")