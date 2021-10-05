from easytrader import  remoteclient
import time
while True:
    user = remoteclient.use('universal_client', host='139.196.21.228', port='1430')
    print(user)
    print(user.prepare(user='63407352', password='681246'))
    print(user.balance)
    time.sleep(60)

# print(user)
#user.connect(r'C:\\同花顺软件\\同花顺\\xiadan.exe')  #
print(user.buy('162411', price=0.55, amount=100))
print(user.buy('162411', price=0.55, amount=100))