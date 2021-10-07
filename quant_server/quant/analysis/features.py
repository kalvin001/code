#def
from data.source.dbdata import *
import matplotlib.pyplot as plt


df  =DBData.k_line_daily(str("600519.SH"), start_date="2015-01-01", end_date="2022-01-01")


print(df["pct_chg"])
plt.plot(df["pct_chg"])
plt.show()
#600519.SH