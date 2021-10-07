from market import Market
from backtest import BackTest, backtest_save, plot_asset, plot_signal
from utils.dingtalk import DingTalk
from utils.sendmail import sendmail
from utils.logger import logger
from utils.storage import txt_read, txt_save, save_to_csv_file, read_csv_file
from utils.tools import *
from config import config
from indicators import *


class Strategy:

    def __init__(self):
        #config.loads("config.json")
        self.asset = 10000
        self.backtest = BackTest()
        data = Market.kline("sh.600519",'1d',start_date="2010-01-01")
        data = data.drop('code', axis=1)
        data = data.values.tolist()
        #print(data)
        self.buy_signal,self.sell_signal,self.ma20,self.ma30= [],[],[],[]
        self.kline = []
        for k in data:
            self.kline.append(k)
            self.backtest.initialize(self.kline,data)
            self.begin()
        plot_asset()
        #plot_signal(data,self.buy_signal,self.sell_signal,self.ma20,self.ma30)

    def begin(self):
        if CurrentBar(self.kline)<30:
            return
        #print(self.backtest.timestamp)
        if self.backtest.timestamp< "2010-01-01" or self.backtest.timestamp>"2021-10-10":
            return
        ma20 = MA(20,self.kline)
        ma30 = MA(30,self.kline)
        self.ma20 = ma20
        self.ma30 = ma30

        cross_over = ma20[-1]>ma30[-1] and ma20[-2]<=ma30[-2]
        cross_down = ma20[-1]<ma30[-1] and ma20[-2]>=ma30[-2]
        if cross_over and self.backtest.long_quantity ==0:
            self.backtest.buy(
                price=self.backtest.close,
                amount=self.asset/self.backtest.close,
                long_quantity=self.asset/self.backtest.close,
                long_avg_price=self.backtest.close,
                profit=0,
                asset=self.asset
            )
            self.buy_signal.append(self.backtest.high)
        elif cross_down and self.backtest.long_quantity!=0:
            profit = (self.backtest.close - self.backtest.long_avg_price) * self.backtest.long_quantity
            self.asset +=profit
            self.backtest.sell(
                price=self.backtest.close,
                amount=self.backtest.long_quantity,
                long_quantity=0,
                long_avg_price=0,
                profit=profit,
                asset=self.asset

            )
            self.sell_signal.append(self.backtest.low)

        if self.backtest.long_quantity>0 and self.backtest.low <=self.backtest.long_avg_price*0.9:
            profit = (self.backtest.close - self.backtest.long_avg_price) * self.backtest.long_quantity
            self.asset += profit
            self.backtest.sell(
                price=self.backtest.close,
                amount=self.backtest.long_quantity,
                long_quantity=0,
                long_avg_price=0,
                profit=profit,
                asset=self.asset
            )
            self.sell_signal.append(self.backtest.low)


if __name__ == '__main__':
    strategy = Strategy()

