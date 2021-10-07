import tushare as ts
from config import config


class TuShareData:

    @staticmethod
    def new_stock():
        """获取新股上市列表数据"""
        pro = ts.pro_api(config.tushare_api)
        result = pro.new_share()
        return result

    @staticmethod
    def stocks_list(fields='ts_code,symbol,name,area,market,exchange,industry,curr_type,list_status,list_date,delist_date,is_hs'):
        """股票列表,获取基础信息数据，包括股票代码、名称、上市日期、退市日期等"""
        pro = ts.pro_api(config.tushare_api)
        response = pro.query('stock_basic', exchange='', list_status='L',
                             fields=fields)
        return response