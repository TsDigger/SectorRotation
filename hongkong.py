# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 11:26:31 2017

@author: thinkpad
"""
def date2string(date_list):#把datetime型的日期转化为字符型，才能用loc函数
    time_string=[]
    for each in date_list:
        time_string.append(each.strftime("%Y-%m-%d"))
    return time_string
    
HS_code="0001.HK,0002.HK,0003.HK,0004.HK,0005.HK,0006.HK,0011.HK,0012.HK,0016.HK,0017.HK,0019.HK,0023.HK,0027.HK,0066.HK,0083.HK,0101.HK,0135.HK,0144.HK,0151.HK,0175.HK,0267.HK,0288.HK,0293.HK,0386.HK,0388.HK,0688.HK,0700.HK,0762.HK,0823.HK,0836.HK,0857.HK,0883.HK,0939.HK,0941.HK,0992.HK,1038.HK,1044.HK,1088.HK,1109.HK,1113.HK,1299.HK,1398.HK,1928.HK,2018.HK,2318.HK,2319.HK,2388.HK,2628.HK,3328.HK,3988.HK"
HS_inA_code="0038.HK,0042.HK,0107.HK,0168.HK,0177.HK,0187.HK,0300.HK,0317.HK,0323.HK,0338.HK,0347.HK,0358.HK,0386.HK,0390.HK,0525.HK,0548.HK,0553.HK,0564.HK,0568.HK,0588.HK,0670.HK,0719.HK,0753.HK,0763.HK,0811.HK,0857.HK,0874.HK,0895.HK,0902.HK,0914.HK,0921.HK,0939.HK,0991.HK,0995.HK,0998.HK,1033.HK,1053.HK,1055.HK,1057.HK,1065.HK,1071.HK,1072.HK,1088.HK,1108.HK,1138.HK,1157.HK,1171.HK,1186.HK,1211.HK,1288.HK,1336.HK,1375.HK,1398.HK,1513.HK,1618.HK,1635.HK,1766.HK,1776.HK,1800.HK,1812.HK,1898.HK,1919.HK,1988.HK,2009.HK,2039.HK,2196.HK,2202.HK,2208.HK,2238.HK,2318.HK,2333.HK,2338.HK,2600.HK,2601.HK,2607.HK,2611.HK,2628.HK,2727.HK,2866.HK,2880.HK,2883.HK,2899.HK,3328.HK,3369.HK,3606.HK,3958.HK,3968.HK,3988.HK,3993.HK,6030.HK,6099.HK,6116.HK,6178.HK,6818.HK,6837.HK,6881.HK,6886.HK"
HS=w.wsd(HS_code, "close", "2017-09-29", "2017-10-07", "TradingCalendar=HKEX;PriceAdj=F")
Wind_name=w.wsd(HS.Codes, "sec_name", "2017-10-06", "2017-10-06", "TradingCalendar=HKEX")
HS_df=pd.DataFrame(data=HS.Data,columns=date2string(HS.Times),index=Wind_name.Data[0]).T

HS_inA=w.wsd(HS_inA_code, "close", "2017-09-29", "2017-10-07", "TradingCalendar=HKEX;PriceAdj=F")
Wind_name_inA=w.wsd(HS_inA.Codes, "sec_name", "2017-10-06", "2017-10-06", "TradingCalendar=HKEX")
HS_inA_df=pd.DataFrame(data=HS_inA.Data,columns=date2string(HS_inA.Times),index=Wind_name_inA.Data[0]).T

H_A=[]
for each1 in HS_inA_code.split(sep=','):
    for each2 in HS_code.split(sep=','):
        if each1==each2 :
            H_A.append(each1)

H_Adata=w.wsd(H_A, "close", "2017-09-29", "2017-10-07", "TradingCalendar=HKEX;PriceAdj=F")
Wind_name_HA=w.wsd(H_Adata.Codes, "sec_name", "2017-10-06", "2017-10-06", "TradingCalendar=HKEX")
HS_inA_df=pd.DataFrame(data=H_Adata.Data,columns=date2string(H_Adata.Times),index=Wind_name_HA.Data[0])