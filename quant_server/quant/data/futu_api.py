from futu import *
pwd_unlock = '681246'
#trd_ctx = OpenHKTradeContext(host='127.0.0.1', port=11111)
#print(trd_ctx.unlock_trade(pwd_unlock))
#print(trd_ctx.accinfo_query())


def accinfo_query():
    trd_ctx = OpenHKTradeContext(host='127.0.0.1', port=11111)
    trd_ctx.unlock_trade(pwd_unlock)
    res = trd_ctx.accinfo_query()
    trd_ctx.close()
    return res

print(accinfo_query()) 