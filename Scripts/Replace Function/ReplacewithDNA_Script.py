import os
os.chdir('C:\\Users\\SH\\Desktop\\SKUMix\\Templates\\Transfers\\DNA')

# Read in the file
with open('SKUtranstemp.html', 'r', encoding="utf8") as rf : 
 rfdata = rf.read() 
# Replace the target string
rfdata = rfdata.replace('store_id', 'DNA') 
# Write the file out again
with open('SKUtranstempWF.html', 'w', encoding="utf8") as wf: 
 wf.write(rfdata)
