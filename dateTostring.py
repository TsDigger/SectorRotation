# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:16:12 2017

@author: hp
"""

import datetime
def date2string(date_list):#把datetime型的日期转化为字符型，才能用loc函数
    time_string=[]
    for each in date_list:
        time_string.append(each.strftime("%Y-%m-%d"))
    return time_string