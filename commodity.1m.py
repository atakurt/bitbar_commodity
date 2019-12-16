#!/usr/bin/python
# -*- coding: utf-8 -*-
# <bitbar.title>Commodity Tracker</bitbar.title>
# <bitbar.version>1.0</bitbar.version>
# <bitbar.author>ismail ata kurt</bitbar.author>
# <bitbar.author.github>atakurt</bitbar.author.github>

import urllib2
import json
from bs4 import BeautifulSoup

# get gold prices

url = "https://www.kuveytturk.com.tr/en/finance-portal/"
result = urllib2.urlopen(url).read()

soup = BeautifulSoup(result, 'html.parser')
prices = soup.find_all('table',class_='table-white')

gol_prices = prices[0].find_all('tr')[1].find_all('td')
buy =  gol_prices[1].get_text()
sell =  gol_prices[2].get_text()

print "GAU Buy : " + buy
print "GAU Sell : " + sell