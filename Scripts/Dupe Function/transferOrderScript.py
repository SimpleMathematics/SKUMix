import os
import requests
import json

def makeNew():

	transfer_order_id = "5aa041c9047ef6338d5358b1"
	transfer_order_dict = {}
	# transfer_order_dict["notes"] = "Testing new put123156"
	# print(type(transfer_order_dict["notes"]))


	#                        --------Gets a transfer_order--------
	headers = {'Authorization': os.environ['SKU_TOKEN'], "Content-Type": "application/json"}
	payload = {"id":transfer_order_id}
	transfer_order_get = requests.get("https://api.skulabs.com/transfer_order/get",headers=headers, params=payload)
	transfer_order_dict["items"] = transfer_order_get.json()["transfer_order"]["items"]
	transfer_order_dict["id"] = transfer_order_get.json()["transfer_order"]["_id"]
	transfer_order_dict["source_warehouse_id"] = transfer_order_get.json()["transfer_order"]["source_warehouse_id"]
	transfer_order_dict["destination_warehouse_id"] = transfer_order_get.json()["transfer_order"]["destination_warehouse_id"]
	# print(type(transfer_order_dict))
	                  
	#                        --------Edits a transfer_order--------


	payload = {
	  "transfer_order_id": transfer_order_dict["id"],
	  "items": transfer_order_dict["items"],
	  "source_warehouse_id": transfer_order_dict["source_warehouse_id"],
	  "destination_warehouse_id": transfer_order_dict["destination_warehouse_id"],
	  # "notes": transfer_order_dict["notes"]
	}

	transfer_order = requests.put("https://api.skulabs.com/transfer_order/update",headers=headers, data=json.dumps(payload))
	# print(transfer_order.json())
	return transfer_order_get.json()	

makeNew()

# #                       --------Makes new transfer_order--------
# headers = {'Authorization': os.environ['SKU_TOKEN'], "Content-Type": "application/json"}
# payload = {
# 	  "number": "testing",
# 	  "items": [
# 	    {
# 	      "item_id": "5a80f9bc172a8004ed5c063c",
# 	      "quantity": "1",
# 	      "destination_location_id": "5a7cf5457799e326c15d50b2",
# 	      "source_location_id": "5a80fae6b71e7f04ac171f80",
# 	      "_id": "5aa041c9047ef6338d5358b3",
# 	      "status": "Pending Transit"
# 	    }
# 	  ],
# 	  "source_warehouse_id": "58ab92ca12c0265dacc275ad",
# 	  "destination_warehouse_id": "58ab92ca12c0265dacc275ad",
# 	  "notes": "works12345698989898"
# 	}
# transfer_order = requests.post("https://api.skulabs.com/transfer_order/create", headers=headers, data=json.dumps(payload))
# print(transfer_order)