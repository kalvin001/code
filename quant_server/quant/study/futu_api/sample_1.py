import time
from futu import *
from sqlalchemy import create_engine

sql_engine = create_engine("mysql+mysqlconnector://root:k135792684@127.0.0.1:3306/quant?auth_plugin=mysql_native_password", echo=False)


class StockQuoteTest(StockQuoteHandlerBase):
    def on_recv_rsp(self, rsp_pb):
        ret_code, data = super(StockQuoteTest, self).on_recv_rsp(rsp_pb)
        if ret_code != RET_OK:
            print("StockQuoteTest: error, msg: %s" % data)
            return RET_ERROR, data
        print("StockQuoteTest ", data)  # StockQuoteTest 自己的处理逻辑
        data.to_sql(name="stock_test_futu", con=sql_engine, if_exists="replace")

        return RET_OK, data


quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
handler = StockQuoteTest()
quote_ctx.set_handler(handler)  # 设置实时报价回调
quote_ctx.subscribe(['HK.00700'], [SubType.QUOTE])  # 订阅实时报价类型，FutuOpenD 开始持续收到服务器的推送
time.sleep(15)  # 设置脚本接收 FutuOpenD 的推送持续时间为15秒
quote_ctx.close()  # 关闭当条连接，FutuOpenD 会在1分钟后自动取消相应股票相应类型的订阅
