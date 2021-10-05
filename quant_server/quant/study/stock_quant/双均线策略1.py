from stockquant.market import Market
from stockquant.backtest import BackTest, backtest_save, plot_asset, plot_signal
from stockquant.utils.dingtalk import DingTalk
from stockquant.utils.sendmail import sendmail
from stockquant.utils.logger import logger
from stockquant.utils.storage import txt_read, txt_save, save_to_csv_file, read_csv_file
from stockquant.utils.tools import *
from stockquant.config import config
from stockquant.indicators import *


class Strategy:

    def __init__(self):
        config.loads("config.json")
        self.amount, self.price=0,0

    def begin(self):
        if(get_localtime()[11:16]=="16:00" and Market.today_is_open()):
            kline = Market.kline("sh600519",'1d')
            ma20 = MA(20,kline)
            ma30 = MA(20,kline)
            cross_over = ma20[-1]>ma30[-1] and ma20[-2]<=ma30[-2]
            cross_down = ma20[-1]<ma30[-1] and ma20[-2]>=ma30[-2]
            if cross_over:
                sendmail("金叉 请买入")
                self.amount,self.price=100,float(kline[-1][4])
            else:
                sendmail("死叉 请卖出")
                self.amount, self.price = 0, 0
        if self.amount>0 and not not_open_time():
            tick = Market.tick("sh600519")
            last = tick.last
            if last <= self.price *0.9:
                sendmail.text("当前价格已经到止损位置")


if __name__ == '__main__':
    strategy = Strategy()
    while True:
        try:
            strategy.begin()
            sleep(3)
        except Exception as e:
            logger.error(e)

