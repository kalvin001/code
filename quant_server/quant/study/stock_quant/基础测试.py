from stockquant.market import Market
from stockquant.backtest import BackTest, backtest_save, plot_asset, plot_signal
from stockquant.utils.dingtalk import DingTalk
from stockquant.utils.sendmail import sendmail
from stockquant.utils.logger import logger
from stockquant.utils.storage import txt_read, txt_save, save_to_csv_file, read_csv_file
from stockquant.utils.tools import *
from stockquant.config import config
from stockquant.indicators import *
#import talib

config.loads('config.json')			# 载入配置文件®®®
tick = Market.tick("sh601003")
print(tick.symbol,tick.last,tick.timestamp)

print(len(Market.kline("sh601003","1d")))
print(Market.shanghai_component_index())
print(Market.shenzhen_component_index())
#print(Market.stocks_list())
print(Market.new_stock())

#print(sendmail("test kalvin"))

save_to_csv_file("ddd","./test.txt")