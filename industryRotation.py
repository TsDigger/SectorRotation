# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 16:04:26 2017

@author: hp
"""
import datetime

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
import seaborn as sns
sns.set_style("darkgrid",{"font.sans-serif":['simhei', 'Arial']})
from WindPy import *
w.start()
#import time
#tradingDay=time.strftime('%Y-%m-%d',time.localtime(time.time()))
import last_tradingday
tradingDay=last_tradingday.tradingDay

industry_list="000905.SH,000016.SH,000300.SH,801010.SI,801020.SI,801030.SI,801040.SI,801050.SI,801080.SI,801110.SI,801120.SI,801130.SI,801140.SI,801150.SI,801160.SI,801170.SI,801180.SI,801200.SI,801210.SI,801230.SI,801710.SI,801720.SI,801730.SI,801740.SI,801750.SI,801760.SI,801770.SI,801780.SI,801790.SI,801880.SI,801890.SI"
concept_list="000905.SH,000016.SH,000300.SH,884001.WI,884028.WI,884030.WI,884031.WI,884032.WI,884034.WI,884035.WI,884036.WI,884037.WI,884039.WI,884040.WI,884041.WI,884045.WI,884046.WI,884050.WI,884057.WI,884062.WI,884069.WI,884074.WI,884075.WI,884076.WI,884077.WI,884079.WI,884080.WI,884081.WI,884086.WI,884087.WI,884088.WI,884089.WI,884090.WI,884091.WI,884092.WI,884093.WI,884096.WI,884098.WI,884099.WI,884100.WI,884101.WI,884103.WI,884104.WI,884106.WI,884107.WI,884109.WI,884110.WI,884111.WI,884112.WI,884113.WI,884114.WI,884115.WI,884116.WI,884119.WI,884121.WI,884123.WI,884124.WI,884125.WI,884126.WI,884127.WI,884128.WI,884129.WI,884130.WI,884131.WI,884132.WI,884133.WI,884134.WI,884135.WI,884136.WI,884137.WI,884138.WI,884139.WI,884140.WI,884141.WI,884142.WI,884144.WI,884145.WI,884146.WI,884148.WI,884149.WI,884151.WI,884152.WI,884153.WI,884154.WI,884155.WI,884156.WI,884157.WI,884158.WI,884159.WI,884160.WI,884161.WI,884162.WI,884163.WI,884164.WI,884165.WI,884166.WI,884167.WI,884168.WI,884169.WI,884170.WI,884171.WI,884172.WI,884173.WI,884174.WI,884175.WI,884176.WI,884177.WI,884178.WI,884179.WI,884180.WI,884181.WI,884182.WI,884183.WI,884184.WI,884185.WI,884186.WI,884187.WI,884188.WI,884189.WI,884190.WI,884191.WI,884192.WI,884193.WI,884194.WI,884195.WI,884196.WI,884197.WI,884198.WI,884199.WI,884200.WI,884201.WI,884202.WI,884203.WI,884204.WI,884205.WI,884206.WI,884207.WI,884208.WI,884209.WI,884210.WI,884211.WI,884212.WI,884213.WI,884214.WI,884215.WI,884216.WI,884217.WI,884218.WI,884219.WI,884220.WI,884221.WI,884222.WI,884223.WI,884224.WI,884225.WI,884226.WI,884227.WI,884228.WI,884229.WI,884230.WI,884231.WI,884232.WI,884233.WI,884234.WI,884235.WI,884236.WI,884237.WI,884238.WI,884239.WI,884240.WI,884241.WI,884242.WI,884243.WI,884244.WI,884245.WI,884246.WI,884247.WI,884248.WI,884249.WI,884250.WI,884251.WI,884252.WI,884253.WI,884254.WI,884255.WI"
industry_second_list="000905.SH,000016.SH,000300.SH,801011.SI,801012.SI,801013.SI,801014.SI,801015.SI,801016.SI,801017.SI,801018.SI,801021.SI,801022.SI,801023.SI,801024.SI,801032.SI,801033.SI,801034.SI,801035.SI,801036.SI,801037.SI,801041.SI,801051.SI,801053.SI,801054.SI,801055.SI,801072.SI,801073.SI,801074.SI,801075.SI,801076.SI,801081.SI,801082.SI,801083.SI,801084.SI,801085.SI,801092.SI,801093.SI,801094.SI,801101.SI,801102.SI,801111.SI,801112.SI,801123.SI,801124.SI,801131.SI,801132.SI,801141.SI,801142.SI,801143.SI,801144.SI,801151.SI,801152.SI,801153.SI,801154.SI,801155.SI,801156.SI,801161.SI,801162.SI,801163.SI,801164.SI,801171.SI,801172.SI,801173.SI,801174.SI,801175.SI,801176.SI,801177.SI,801178.SI,801181.SI,801182.SI,801191.SI,801192.SI,801193.SI,801194.SI,801202.SI,801203.SI,801204.SI,801205.SI,801211.SI,801212.SI,801213.SI,801214.SI,801215.SI,801222.SI,801223.SI,801231.SI,801711.SI,801712.SI,801713.SI,801721.SI,801722.SI,801723.SI,801724.SI,801725.SI,801731.SI,801732.SI,801733.SI,801734.SI,801741.SI,801742.SI,801743.SI,801744.SI,801751.SI,801752.SI,801761.SI,801881.SI"
def date2string(date_list):#把datetime型的日期转化为字符型，才能用loc函数
    time_string=[]
    for each in date_list:
        time_string.append(each.strftime("%Y-%m-%d"))
    return time_string


fig=plt.figure()
axe=fig.add_subplot(111)
def getData(code_list):
    Wind_data=w.wsd(code_list, "close", "2017-01-01", tradingDay, "PriceAdj=F")
    Wind_name=w.wsd(code_list, "sec_name", tradingDay, tradingDay, "")
    
    new_data=pd.DataFrame(data=Wind_data.Data,columns=date2string(Wind_data.Times),index=Wind_name.Data[0])
    new_data=new_data.T
    return new_data


def industry_plot(select_list,start_time='2017-01-03',total_list=industry_list,normalise=True):
    new_data=getData(total_list)
    a=[]
    axe.clear()
    n=list(new_data.index).index(start_time)
    plot_data=new_data[n:]

#    if symbol=='industry':
#        for each in industry: 
#            a.append(each+'(申万)')
#    else:
#        for each in industry:
#            a.append(each+'指数')
    for each1 in select_list:
        for each2 in list(plot_data.columns):
            if each2.find(each1)!=-1:
                a.append(each2)
                break
            
        
    a.extend(['沪深300','中证500','上证50'])
    if normalise==True:
        b=[]
        for each in a:
            plot_data[each+'标准化']=plot_data[each]/plot_data[each][0]
            b.append(each+'标准化')
        
        plot_data[b].plot(ax=axe)
    else:
        
        plot_data[a].plot(ax=axe)
        
    fig.show()

