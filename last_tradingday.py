# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 12:05:16 2017

@author: thinkpad
"""

import datetime
from WindPy import *
w.start()

def getpreviousday(tradingdate):
    previousday=w.tdaysoffset(-1, tradingdate, "")
    return previousday.Data[0][0].strftime("%Y-%m-%d")
    
import time
tradingDay=getpreviousday(time.strftime('%Y-%m-%d',time.localtime(time.time())))

