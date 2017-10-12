# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 13:57:10 2017

@author: hp
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
sns.set_style("darkgrid",{"font.sans-serif":['simhei', 'Arial']})
##设置中文显示
from WindPy import *
w.start()
##打开wind
#import time
#tradingDay=time.strftime('%Y-%m-%d',time.localtime(time.time()))#获得当天时间
import last_tradingday
tradingDay=last_tradingday.tradingDay
SW_second=w.wset("sectorconstituent","date="+tradingDay+";sectorid=a39901011h000000")
Sw_second_df=pd.DataFrame(data=SW_second.Data[1],index=SW_second.Data[2])

def find_constituent(industry_name):
    for each in list(Sw_second_df.index):
        if each.find(industry_name)!=-1:
            temp=w.wset("sectorconstituent","date="+tradingDay+";windcode="+Sw_second_df[0][each])
            stock_list=temp.Data[1]
            break
    stock_list.extend(['000905.SH','000016.SH','000300.SH'])
    stock_list.append(Sw_second_df[0][each])
    return stock_list

import industryRotation as ir
def getconstituent_data(industry_name):
    return ir.getData(find_constituent(industry_name))

