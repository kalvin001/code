from django.db import models
 


class StockBasic(models.Model):
    code = models.CharField(primary_key=True,verbose_name="股票/标的代码",max_length=32)
    name = models.CharField(verbose_name="名称",max_length=64,default="")
    area = models.CharField(verbose_name="地域",max_length=32,default="")
    market = models.CharField(verbose_name="市场类型",max_length=16,default="")
    exchange = models.CharField(verbose_name="交易所代码",max_length=16)
    industry = models.CharField(verbose_name="所属行业",max_length=16,default="")
    curr_type = models.CharField(verbose_name="交易货币",max_length=16)
    list_status = models.CharField(verbose_name="上市状态",max_length=16)
    list_date = models.DateTimeField(verbose_name="上市时期",max_length=16)
    delist_date = models.DateTimeField(verbose_name="退市日期",max_length=16)
    is_hs = models.CharField(verbose_name="沪深港通",max_length=16,default="")


    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

"""

参考: http://baostock.com/baostock/index.php/A%E8%82%A1K%E7%BA%BF%E6%95%B0%E6%8D%AE
是个
"""
class Kline_1d(models.Model):
    date = models.DateTimeField(verbose_name="交易时间",max_length=16,db_index=True)
    code = models.CharField(verbose_name="名称",max_length=64,default="",db_index=True)
    open = models.DecimalField(verbose_name="开盘价格",max_digits="10", decimal_places="4",default=0.0)
    close = models.DecimalField(verbose_name="收盘价格",max_digits="10", decimal_places="4",default=0.0)
    high = models.DecimalField(verbose_name="最高价格",max_digits="10", decimal_places="4",default=0.0)
    low = models.DecimalField(verbose_name="最低价格",max_digits="10", decimal_places="4",default=0.0)
    preclose = models.DecimalField(verbose_name="前一天收盘价格",max_digits="10", decimal_places="4" ,default=0.0)
    volume = models.BigIntegerField(verbose_name="成交量(股)",default=0)
    amount = models.DecimalField(verbose_name="成交金额",max_digits="16", decimal_places="2",default=0)
    # 复权状态(1：后复权， 2：前复权，3：不复权）主要考虑使用前复权数据; 不过前复权需要复权后需要回刷历史数据
    adjustflag = models.IntegerField(verbose_name="复权类型",default=0)
    # [指定交易日的成交量(股)/指定交易日的股票的流通股总股数(股)]*100%
    turn = models.DecimalField(verbose_name="换手率",max_digits="8", decimal_places="4")
    # 交易状态(1：正常交易，0：停牌）
    tradestatus = models.IntegerField(verbose_name="交易状态",default=0)
    pct_chg = models.DecimalField(verbose_name="涨跌幅(百分比)",max_digits="12", decimal_places="4",default=0.0)
    # (指定交易日的股票收盘价/指定交易日的每股盈余TTM)=(指定交易日的股票收盘价*截至当日公司总股本)/归属母公司股东净利润TTM
    pe_ttm = models.DecimalField(verbose_name="滚动市盈率",max_digits="12", decimal_places="4",default=0.0)
    # (指定交易日的股票收盘价/指定交易日的每股净资产)=总市值/(最近披露的归属母公司股东的权益-其他权益工具)
    pb_mrq = models.DecimalField(verbose_name="市净率",max_digits="12", decimal_places="4",default=0.0)
    # (指定交易日的股票收盘价/指定交易日的每股销售额)=(指定交易日的股票收盘价*截至当日公司总股本)/营业总收入TTM
    ps_ttm = models.DecimalField(verbose_name="滚动市销率",max_digits="12", decimal_places="4",default=0.0)
    # (指定交易日的股票收盘价/指定交易日的每股现金流TTM)=(指定交易日的股票收盘价*截至当日公司总股本)/现金以及现金等价物净增加额TTM
    pcf_ncf_ttm = models.DecimalField(verbose_name="滚动市现率",max_digits="12", decimal_places="4",default=0.0)
    is_st = models.IntegerField(verbose_name="是否ST(1是 0否)",default=0)

    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))