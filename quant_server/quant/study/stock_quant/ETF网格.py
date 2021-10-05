from stockquant.market import Market
from stockquant.backtest import BackTest, backtest_save, plot_asset, plot_signal
from stockquant.utils.dingtalk import DingTalk
from stockquant.utils.sendmail import sendmail
from stockquant.utils.logger import logger
from stockquant.utils.storage import txt_read, txt_save, save_to_csv_file, read_csv_file
from stockquant.utils.tools import *
from stockquant.config import config
from stockquant.indicators import *


class EtfGridStrategy:

    def __init__(self):
        config.loads("config.json")
        self._symbol = 'sh512980'
        self._asset = 10000
        self._amount = 0
        self.first_buy_day = None

        logger.info("start to run .... Currnet price is {}".format(Market.tick(self._symbol).last))

        while True:
            try:
                self.do_action()
                sleep(5)
            except:
                logger.error()

    def do_action(self):
        if not not_open_time() and Market.today_is_open():
            price = Market.tick(self._symbol).last
            logger.info("Current price is {}".format(price))

            if self._symbol ==0 and 3450 <= price <=3550:
                first_buy_amount = round(self._asset/2/price/100)
                self._amount=first_buy_amount
                self._asset-=first_buy_amount*price
                self.first_buy_day = get_date()

            if self._amount> 0:
                if price<=3250:
                    buy_amount = round(self._asset/2/price/100)
                    self._amount +=buy_amount
                    self._asset -= buy_amount + price
                elif price<=3000:
                    buy_amount = round(self._asset/price/100)
                    self._amount +=buy_amount
                    self._asset -= buy_amount + price

                if get_date()!=self.first_buy_day:
                    if price>=3750:
                        sell_amount  = self._amount/2
                        self._amount -= sell_amount
                        self._asset += sell_amount * price
                    elif price>4000:
                        sell_amount = self._amount
                        self._amount -= sell_amount
                        self._asset += sell_amount * price

if __name__ == '__main__':
    strategy = EtfGridStrategy()

