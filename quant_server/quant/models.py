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