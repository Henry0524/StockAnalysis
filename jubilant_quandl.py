# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 20:48:46 2016

@author: HOME
"""

import quandl
import matplotlib.pyplot as plt

data = quandl.get("NSE/JUBILANT")
print data

stock_date = [x for x in data.index.values if str(x)[:4] == '2015' ]
print stock_date

stock_price = []
for i in xrange(len(stock_date)):
    stock_price.append(data['Open'].ix[i])
print stock_price

plt.plot(stock_date,stock_price)
sample = 30
plt.xticks(stock_date[::sample])
plt.show()