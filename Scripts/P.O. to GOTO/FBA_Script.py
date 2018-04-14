# P.O. to Transfer Order

import json
from pprint import pprint
from html.parser import HTMLParser

with open('LECR (12th-123).txt', mode='r') as rf:

	notedata = json.load(open('LECR (12th-123).txt'))
	for shipments in notedata['shipment']:
		sku = shipments['sku'][0:]
		fba = shipments['fba'][0:]
		qty = shipments['qty'][0:]
		print(sku, fba, qty)


with open('LECR (12th-123).html', mode='r+') as wf:
	
	temp = wf.read()
	tempdata = json.dumps(temp, indent=2)
	# print(tempdata)

	class MyHTMLParser(HTMLParser):
		def handle_starttag(self, tag, attrs):
			print("start tag:", tag)

		def handle_endtag(self, tag):
			print("end tag :", tag)

		def handle_data(self, data):
			print("Encountered some data  :", data)
		
parser = MyHTMLParser()
tempdatasort = parser.feed(tempdata)










# new_string = json.dumps(data, indent=2, sort_keys=True)
# print (new_string)