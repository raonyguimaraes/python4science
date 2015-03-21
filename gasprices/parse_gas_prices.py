#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from bs4 import BeautifulSoup
import re
#maps
import urllib, urllib2, json

filename = "dataset/Gasolina Comum e Aditivada - Pesquisa de Preços - Mercado Mineiro.html"
saved_data = open(filename)

soup = BeautifulSoup(saved_data)

tables = soup.find_all("table")

#remove two tables from start
tables = tables[2::]
#remove one table from end
tables = tables[:-1]

postos_count = 0
postos = {}

for table in tables:
	# print table.tbody
	rows = table.findAll('tr')
	for tr in rows:
	  cols = tr.findAll('td')
	  # print 'td length', len(cols)
	  if  len(cols) == 3:
	  	postos_count +=1
	  	posto = cols[0].font.a.text
	  	postos[posto] = {}
	  	#endereco
	  	endereco = cols[0].div.div.text
	  	endereco = endereco.replace('\n', '').strip()
	  	endereco = re.sub(r'\s+', ' ', endereco)
	  	# print endereco
	  	postos[posto]['endereco'] = endereco
	  	
	  	#treat empty
	  	if cols[1].text != '-':
	  		gas_comum = cols[1].div.font.text
	  		postos[posto]['gas_comum'] = gas_comum
	  	if cols[2].text != '-':
	  		gas_aditivada = cols[2].div.font.text
	  		postos[posto]['gas_aditivada'] = gas_aditivada


def decode_address_to_coordinates(address):
        params = {
                'address' : address,
                'sensor' : 'false',
        }  
        url = 'http://maps.google.com/maps/api/geocode/json?' + urllib.urlencode(params)
        response = urllib2.urlopen(url)
        result = json.load(response)
        try:
                return result['results'][0]['geometry']['location']
        except:
                return None


for idx, posto in enumerate(postos):
	if 'gas_comum' in postos[posto]:
		# print postos[posto]
		address =  postos[posto]['endereco'].decode('utf-8')
		# print address
		coordinates = decode_address_to_coordinates(address)
		if coordinates:
			output = '''
		var posto%s = new google.maps.LatLng(%s,%s);
		var gas_value%s = "%s"
		var marker = new MarkerWithLabel({
		   position: posto%s,
		   draggable: true,
		   raiseOnDrag: true,
		   map: map,
		   labelContent: gas_value%s,
		   labelAnchor: new google.maps.Point(22, 0),
		   labelClass: "labels" // the CSS class for the label
		});
			''' % (idx, coordinates['lat'], coordinates['lng'], idx, postos[posto]['gas_comum'], idx, idx)
			print output