from futu import *

pwd_unlock = '681246'
trd_ctx = OpenHKTradeContext(host='127.0.0.1', port=11111)
print(trd_ctx.get_acc_list())
trd_ctx.unlock_trade(pwd_unlock)
print("----", trd_ctx.accinfo_query(acc_id=281756455982890410,refresh_cache=True,currency=Currency.USD)[1].to_json())
res = trd_ctx.accinfo_query()
#print("------" + res.values())
trd_ctx.close()