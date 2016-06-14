url = 'http://www.google.com/finance/info?q=BOM:524091,532683,500112'
socket1 = urllib2.urlopen(url)
data = socket1.read()