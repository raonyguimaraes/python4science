#!/usr/bin/env python
# -*- coding: utf-8 -*-

#withdrawal numbers already sorted  

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from bs4 import BeautifulSoup
import re
#maps
import urllib, urllib2, json

filename = "D_MEGA.HTM"
saved_data = open(filename)

resultados = []

soup = BeautifulSoup(saved_data)

tables = soup.find_all("table")

for table in tables:
	# print table.tbody
	rows = table.findAll('tr')
	for tr in rows:
		cols = tr.findAll('td')
	  	if len(cols)>0:
	  		print cols
	  		resultado = []
	  		resultado.append(cols[2].text)
	  		resultado.append(cols[3].text)
			resultado.append(cols[4].text)
			resultado.append(cols[5].text)
			resultado.append(cols[6].text)
			resultado.append(cols[7].text)
			resultados.append(resultado)

print len(resultados)	  		
