import os
from bs4 import BeautifulSoup


os.chdir('C:\\Users\\SH\\Desktop\\SKUMix\\Templates\\Transfers\\SANDBOX')

def test():

	with open('SKUdiv.html', 'r',) as rf : 
	 rfdata = rf.read()
	soup = BeautifulSoup(rfdata, 'html.parser')  
	results = soup.find_all('div', class_='CH-first')



	records = []
	for result in results:

		tbody_tag = result.find('tbody', class_='CH-Dupe')

		tr_tag = result.find('tr')

		sku_link = result.find('<td id="sku" class="mdl-data-table__cell--non-numeric">sku_id</td>')
		for sku in result.find(id='sku'):
			sku.string.replace_with("sku_variable")

		fba_links = result.find('<td id="fba" class="mdl-data-table__cell--non-numeric"><a target="_blank" href="https://sellercentral.amazon.com/gp/fba/inbound-shipment-workflow/index.html#fba_id/summary/tracking">fba_id</a></td>')
		for fba_url in result.find_all('a'):
			fba_url['href'] = fba_url['href'].replace("fba_id", "fba_variable")
		fba_link = result.find('<td id="fba" class="mdl-data-table__cell--non-numeric">fba_id</td>')
		for fba in result.find(id='fba'):
			fba.string.replace_with("fba_variable")

		qty_link = result.find('<td id="qty" class="mdl-data-table__cell--non-numeric">00</td>')
		for qty in result.find(id='qty'):
			qty.string.replace_with("qty_varible")
		
		store_link = result.find('<td id="store" class="mdl-data-table__cell--non-numeric">store_id</td>')
		for store in result.find(id='store'):
			store.string.replace_with("store_variable")

		# a_tag = result.find('a').text[0:] + '***'
		records.append((tbody_tag, tr_tag, sku, fba_url, fba, qty))
		# print(type(records))
		# print(records)
	return result

	for i in results:
		print(tr_tag)

test()

# print("testing")







# Read in the file
# with open('SKUtranstemp.html', 'r', encoding="utf8") as rf : 
#  rfdata = rf.read() 
#  print(type(rfdata))
#  rfdata = rfdata[250:277]
#  new = rfdata.copy(rfdata)
#  print(rfdata)
 # print(rfdata)
# Replace the target string
# rfdata = rfdata.find("CH-first") 

# rfdata = "CH-first"
# CHfirst = [['sku_id', 'fba_id', 'store_id' ]]





# with open('SKUtranstempWF.html', 'w', encoding="utf8") as wf: 
#  wf.write(rfdata)





# Write the file out again
# word = "store_id"
# word2 = "fba_id"
# name = "file_name.html"
# if word and word2 in rfdata:
# 	newword = rfdata.replace(word, "testing")
# 	newword2 = rfdata.replace(word2, "testing")
# 	print("working", newword)
# else: print("Can't find", word)
# with open(name, 'w', encoding="utf8") as wf: 
#  wf.write(newword)
#  wf.write(rfdata)
