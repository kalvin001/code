from market import Market
from backtest import BackTest, backtest_save, plot_asset, plot_signal
from utils.dingtalk import DingTalk
from utils.sendmail import sendmail
from utils.logger import logger
from utils.storage import txt_read, txt_save, save_to_csv_file, read_csv_file
from utils.tools import *
from config import config
from indicators import *
from data.source.baostockdata import BaoStockData
from data.source.dbdata import DBData
from data.stock_data import *




class Strategy:

    def __init__(self):
        #config.loads("config.json")
        self.asset = 10000
        self.pre_code=None
        self.backtest = BackTest()
        df = BaoStockData.query_trade_dates(start_date="2018-06-30")
        df1 = df.loc[df["is_trading_day"] == '1']
        dates = df1.values.tolist()
        #print(data)
        self.buy_signal,self.sell_signal = [],[]
        self.dates = []
        for k in dates:
            self.dates.append(k)
            self.backtest.initialize(self.dates,dates)
            self.begin()
        plot_asset()
        #plot_signal(data,self.buy_signal,self.sell_signal,self.ma20,self.ma30)

    def begin(self):


        cur_date  = self.dates[-1][0]
        print(cur_date)
        klines = DBData.get_all_kline(cur_date,cur_date)
        code = get_min_pe_ttm_stock(klines).code
        close = float(get_min_pe_ttm_stock(klines).close)
        if self.pre_code!=code:
            if self.pre_code is not None:
                pre_close = float(DBData.get_kline(self.pre_code,cur_date,cur_date)[0].close)
                profit = (pre_close - self.backtest.long_avg_price) * self.backtest.long_quantity
                self.asset += profit
                self.backtest.sell(
                    price=pre_close,
                    amount=self.backtest.long_quantity,
                    long_quantity=0,
                    long_avg_price=0,
                    profit=profit,
                    asset=self.asset

                )
                self.sell_signal.append(pre_close)
                print("sell",self.pre_code,pre_close,cur_date)
            self.pre_code=code
            self.backtest.buy(
                price=close,
                amount=self.asset/close,
                long_quantity=self.asset/close,
                long_avg_price=close,
                profit=0,
                asset=self.asset
            )
            self.buy_signal.append(close)
            print("buy", code, close,cur_date)




if __name__ == '__main__':
    strategy = Strategy()

