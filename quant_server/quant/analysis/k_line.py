from data.data_manager import DataManager
import pandas as pd
from sqlalchemy import create_engine


# K线切分, 分为x,y; y= 1day reward 3day reward 5day reward;
# 特征抽取:
    #1、最简单对K线的Summery
# 计算不同特征的Reward, 存入数据库; feature, feature_type, stock_code,stock_name, trade_day, reward_1d,reward_3d,reward_5d,reward_10d
# 对所有特征进行统计分析得到解结论

dm = DataManager()
stock_basic = dm.get_stock_basic()

FE_TYPE_PCT_2 = "pct_2"
sql_engine = create_engine("mysql+mysqlconnector://root:k135792684@127.0.0.1:3306/quant?auth_plugin=mysql_native_password", echo=False)


def analysis():
    if_exists = "replace"
    for idx,itm in stock_basic.iterrows():
        if idx !=0:
            if_exists="append"
        print(idx,itm['ts_code'])
        res = analysis_stock(itm['ts_code'],start_date="20110201")
        res.to_sql(name="stock_analysis1", con=sql_engine, if_exists=if_exists)
        #df = dm.k_line_daily(code=itm['ts_code'])

#获取变化率
def change_rate(cur_price,pre_price,type="pct"):

    res = (cur_price/pre_price-1)*100
    if type == FE_TYPE_PCT_2:
        if res >=9.5:res = 9
        elif res>=5:res =5
        elif res>=3:res=3
        elif res>=1:res =1
        elif res>=0:res=0
        elif res>-1:res=-0
        elif res>-3:res=-1
        elif res>-5:res=-3
        elif res>-9.5:res=-5
        else: res=-9
    return round(res,2)

def fe_kline_base(open,close,high,low,pre_close):
    res = ''
    res += str(change_rate(open,pre_close,type=FE_TYPE_PCT_2))
    res += str(change_rate(close,pre_close,type=FE_TYPE_PCT_2))
    res += str(change_rate(high,pre_close,type=FE_TYPE_PCT_2))
    res += str(change_rate(low,pre_close,type=FE_TYPE_PCT_2))
    return res


def get_reward(df,close,cur_idx,reward_day):
    #row_size = df.shape[0]
    idx = cur_idx - reward_day #0是最近一天
    if idx<0:   #row_size-1:
        return 0
    else:
        #print(df.loc[idx])
        end_close = df.loc[idx]["close"]
        return change_rate(end_close,close)



def analysis_stock(code,start_date):
    df = dm.k_line_daily(code,start_date)
    #df = df.sort_values(by=["trade_date"],ascending=[True])
    res = pd.DataFrame()
    for idx, itm in df.iterrows():
        fe_kine_pct2 = fe_kline_base(itm["open"],itm["close"],itm["high"],itm["low"],itm["pre_close"])
        close =itm["close"]
        stock_code =itm["ts_code"]
        trade_date =itm["trade_date"]
        #print(idx)
        reward_1d = get_reward(df,close,idx,1)
        reward_3d = get_reward(df,close,idx,3)
        reward_5d = get_reward(df,close,idx,5)
        reward_10d = get_reward(df,close,idx,10)
        data={"stock_code":stock_code,"trade_date":trade_date,
                "feature":fe_kine_pct2,"feature_type":'pct_2',
                "reward_1d":reward_1d,"reward_3d":reward_3d,
                "reward_5d":reward_5d,"reward_10d":reward_10d}

        #feature, feature_type, stock_code,stock_name, trade_day, reward_1d,reward_3d,reward_5d,reward_10d
        #df1 = pd.DataFrame(data=[[itm["ts_code"],itm["trade_date"],fe_kine_pct2,'pct_2',reward_1d,reward_3d,reward_5d,reward_10d]],
        #                   columns=["stock_code","trade_date","feature","feature_type","reward_1d","reward_3d","reward_5d","reward_10d"],
        #                   index=[idx])
        res =res.append(data,ignore_index=True)
        #print(res)
        #print(idx,itm["trade_date"],fe_kine_pct2,reward_1d,reward_3d,reward_5d,reward_10d)
        #print(idx,itm["open"],itm["close"],itm["high"],itm["low"],itm["pre_close"])
        #print(changeprate(itm["open"],itm["pre_close"]),change_rate(itm["close"],itm["pre_close"]))

    return res


#analysis_stock("000565.SZ")

analysis()