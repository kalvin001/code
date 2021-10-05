from futu import *

pwd_unlock = '681246'
trd_ctx = OpenHKTradeContext(host='127.0.0.1', port=11111,security_firm=SecurityFirm.FUTUSECURITIES)
print(trd_ctx.unlock_trade(pwd_unlock))
trd_ctx.close()


import futu
print(futu.__file__)
print("Python version: ", sys.version)
