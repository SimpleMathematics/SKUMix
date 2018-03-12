import os
os.chdir('C:\\Users\\SH\\Desktop\\SKUMix\\Templates\\Transfers\\SANDBOX')

# Read in the file
with open('Testing.html', 'r') as rf : 
 rfdata = rf.read()
# Here is a method to find and change a value in the database.
fba_list = rfdata
	# spaces = datastore['office']['medical']
print(fba_list[10:])

	# for item in spaces:
	#     if item.get('use') == "examination" :
	#        item['price'] = 175

	# for item in datastore['office']['medical']: # This loop shows the change is not only in books, but is also in database
	#     if item.get('use') == "examination" :
	#         print('The {} rooms now cost {}'.format(item.get("use"), item.get("price")))