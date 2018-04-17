# P.O. to Transfer Order
import json

with open('LECR (12th-123).json', mode="r") as rf:
	note = {}
	newnote = []
	notedata = json.load(rf)
	for shipments in notedata['shipment']:
		note['sku'] = shipments['sku'][0:]
		note['fba'] = shipments['fba'][0:]
		note['qty'] = shipments['qty'][0:]
		newnote.append(note['sku'][0:])

with open('testing.html', mode="w") as wf:

	for notes in note:
		wf.write(note['sku'])


		print(note['sku'])
		# print(note['sku'], note['fba'], note['qty'])

# print(notedata, type(notedata))

