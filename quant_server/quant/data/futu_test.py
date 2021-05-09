from futu import *

pwd_unlock = '681246'
trd_ctx = OpenHKTradeContext(host='127.0.0.1', port=11111)
trd_ctx.unlock_trade(pwd_unlock)
print( trd_ctx.accinfo_query())
res = trd_ctx.accinfo_query()
#print("------" + res.values())
trd_ctx.close()