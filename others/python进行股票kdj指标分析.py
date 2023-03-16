import tushare as ts
import pandas as pd
import pylab as plt
from matplotlib.pyplot import MultipleLocator
data=ts.get_k_data('000001')
data.to_excel('股票000001历史行情.xls')
df=pd.DataFrame()
df['close']=data['close']
DATE=[]
RSV=[]
K_value=[]
K_value.append(50)
D_value=[]
D_value.append(50)
J_value=[]

for i in range(8,len(data)):
    DATE.append(data['date'][i])
    high_price=data['high'][i-8:i+1].max()
    low_price=data['low'][i-8:i+1].min()
    close_price=data['close'][i]
    RSV.append(100*(close_price-low_price)/(high_price-low_price))

for i in range(1,len(RSV)):
    K_value.append(2/3*K_value[i-1]+1/3*RSV[i])

for i in range(1,len(RSV)):
    D_value.append(2/3*D_value[i-1]+1/3*K_value[i])

for i in range(len(K_value)):
    J_value.append(3*K_value[i]-2*D_value[i])

plt.subplot(3,1,1)
plt.plot(data['date'],df['close'],label=u'收盘价')
plt.title('股票行情')
plt.ylabel(u"价格线")
x_major_locator=MultipleLocator(120)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.subplot(3,1,2)
plt.plot(DATE,RSV,label=u'RSV线')
x_major_locator=MultipleLocator(120)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.title('RSV线分析')
plt.ylabel(u"RSV线")
plt.subplot(3,1,3)
plt.plot(DATE,K_value,'r',label=u'K值线')
plt.plot(DATE,D_value,'g',label=u'D值线')
plt.plot(DATE,J_value,'b',label=u'J值线')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.title('KDJ线分析')
plt.ylabel(u"KDJ指标")
x_major_locator=MultipleLocator(120)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.legend()
plt.show()