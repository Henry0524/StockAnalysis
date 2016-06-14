# strings and collections
str1 = "i love python"

# print a string
print str1

#bytes are sequence of bytes
byte1 = b'python'

print byte1

#conversion of utf-8 to bytes and vice - versa
print str1.encode('utf-8')
print str1.decode('utf-8')


list1 = ['i', 'am', 'python']

# if you assign a string to a list object, each character becomes a list element 
list2 = list(str1)
print list2


# to logically assing words in a string to a list, use a split method
list2 = str1.split()
print list2

# string concatenation
print list1 + list2

#find the lenght of a string
print len(str1)

# add elements to the list using the append method
list1.append("version 3")
print list1

import urllib2
# reading from the web and storing in python

url = 'http://www.google.com/finance/info?q=BOM:524091,532683,500112'
socket1 = urllib2.urlopen(url)
data = socket1.read()

# returns a list of dictionaries
print data

url = 'http://www.google.com/finance/info?client=ig&q=NSE:NIFTY,NSE:SBIN%27'
socket1 = urllib2.urlopen(url)
data = socket1.read()
print data


"""
id     : ID,

t      : StockSymbol,ticker

e      : Index,

l      : LastTradePrice,

l_cur  : LastTradeWithCurrency,

ltt    : LastTradeTime,

lt_dts : LastTradeDateTime,

lt     : LastTradeDateTimeLong,

div    : Dividend,

yld    : Yield,

s      : LastTradeSize,

c      : Change,

c      : ChangePercent,

el     : ExtHrsLastTradePrice,

el_cur : ExtHrsLastTradeWithCurrency,

elt    : ExtHrsLastTradeDateTimeLong,

ec     : ExtHrsChange,

ecp    : ExtHrsChangePercent,

pcls_fix: PreviousClosePrice
"""