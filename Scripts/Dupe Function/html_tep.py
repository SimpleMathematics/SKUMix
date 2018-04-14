import os
import io
import json
from transferOrderScript import makeNew

html = makeNew()
# print(type(html), "here ")
# print(html['transfer_order'].keys(),"KEYS")
html_dict = {}

html_dict['5aa041c9047ef6338d5358b1'] =  html['transfer_order']['number']
html_dict["items"] = html['transfer_order']["items"]
id_number = html_dict['5aa041c9047ef6338d5358b1']
file_name = id_number + ".html"
html_dict['qty'] = html_dict["items"], ['quantity']
# print(html_dict.get(['qty']))
for line in html['transfer_order']:
	line = line.split(html_dict["items"])
html_dict["items"] = line[0].strip()
html_dict["qty"] = line[1].strip()
if html_dict["items"] in html_dict:
	html_dict["items"].append(html_dict["qty"])
else:
	html_dict["items"] = html_dict["qty"]
print(html_dict)
with open('div.html', 'w') as file:
	html_dict['transfer_order_items'] =  html['transfer_order']["items"]
# print(html_dict['transfer_order_items'][1]['quantity'])

file.write('<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">\n')
file.write('<link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">\n')
file.write('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">\n')
file.write('<div class="mdl-grid--no-spacing">\n')
file.write('\t<div class="mdl-cell mdl-cell--4-col">\n')
file.write('\t\t<table class="mdl-data-table mdl-js-data-table mdl-data-table--selectable mdl-shadow--2dp">\n')
file.write('\t\t\t<thead>\n')
file.write('\t\t\t\t<th class="mdl-data-table__cell--non-numeric">' + "SKU" + "</th>\n")
file.write('\t\t\t\t<th class="mdl-data-table__cell--non-numeric">' + "FBA Shipment ID" + "</th>\n")
file.write('\t\t\t\t<th class="mdl-data-table">' + "Quantity" + "</th>\n")
file.write('\t\t\t\t<th class="mdl-data-table__cell--non-numeric">' + "Destination" + "</th>\n")
file.write('\t\t\t</thead>\n')
file.write('\t\t\t<tbody>\n')
# print(html['transfer_order']["items"])
	# print(html['transfer_order']["items"][1]['quantity'])
file.write('\t\t\t\t<tr>\n')
file.write("\t\t\t\t\t<td>" + "SKU_HERE" + "</td>\n")
file.write("\t\t\t\t\t<td>" + "FBA_ID_HERE" + "</td>\n")
file.write("\t\t\t\t\t<td>" + ["qty"] + "</td>\n")
file.write("\t\t\t\t\t<td>" + "Destination_Here" + "</td>\n")
file.write('\t\t\t\t</tr>\n')
file.write('\t\t\t</tbody>\n')
file.write('\t\t</table>\n')	
file.write('\t</div>\n')
file.write('</div>\n')
# print(html)

file.close()