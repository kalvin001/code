from stockquant.market import Market
from stockquant.backtest import BackTest, backtest_save, plot_asset, plot_signal
from stockquant.utils.dingtalk import DingTalk
from stockquant.utils.sendmail import sendmail
from stockquant.utils.logger import logger
from stockquant.utils.storage import txt_read, txt_save, save_to_csv_file, read_csv_file
from stockquant.utils.tools import *
from stockquant.indicators import *
from stockquant.config import config

config.loads("config.json")

#kline = Market.kline("sh600519","1d")
#print(MA(20,kline))

stocks_list = Market.stocks_list()
print(stocks_list)
stocks_pool = []

while True:
    if(get_localtime()[11:16] =="16:00" and Market.today_is_open()):
        start_time = get_localtime()
        print("开始时间:" + start_time)
        for i,item in enumerate(stocks_list["ts_code"]):
            if str(item).endswith(".SH"):
                name = "sh" + str(item).replace(".SH","")
            else:
                name = "sz" + str(item).replace(".SZ", "")
            print(i,name)
            kline = Market.kline(name,"1d")
            if len(kline)<30:
                continue

            ma20 = MA(20,kline)
            ma30 = MA(30,kline)

            if ma20[-1]>ma30[-1] and ma20[-2]<ma30[-2]:
                stocks_pool.append(name)
        print("结束时间:" + get_localtime())

        print(stocks_pool)
        sleep(1440*60)
    else:
        sleep(60*60)