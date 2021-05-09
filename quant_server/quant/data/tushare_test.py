#5d2773294dea485e06d949f132e3cf6a620a83fc3b46ee08a03b007d
import tushare as ts
ts.set_token('5d2773294dea485e06d949f132e3cf6a620a83fc3b46ee08a03b007d')
pro = ts.pro_api()


data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,market,exchange,industry,list_date,curr_type,list_status,list_date,delist_date,is_hs')
print(data)
