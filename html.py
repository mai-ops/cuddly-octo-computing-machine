# parse total cc market cap from web:
#
# MM June 2017
#
#  <strong>Total Market Cap: <span id="total-marketcap"
#   data-usd="105,136,188,156" data-btc="42,549,379">
#
#
import requests
import re
import calendar
import time

global myLine
myLine = ""

while (1):
    f = open('ccMCpy.txt','a+')
    r = requests.get('https://coinmarketcap.com/')
    t = r.text
    ts = t.split('\n')
    for line in ts:
        if re.search(r'"total-marketcap"', line) != None:
            myLine = line
            break
    ls = re.split("\"", myLine)
    usd = int(ls[3].replace(',', ''))
    now = str(calendar.timegm(time.gmtime()))
    writeString = now + "," + str(usd) + "\n"
    print writeString
    f.write(writeString)
    f.close() # to ensure data is stored;
    time.sleep(600)
