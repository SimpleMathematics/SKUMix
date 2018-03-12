import os
import requests
import json
from Div_Script import test


transfer_order_list = {}
transfer_order_list["notes"] = test()
print(type(test()))
print(test())

# #                        --------Gets a transfer_order--------
# headers = {'Authorization': os.environ['SKU_TOKEN'], "Content-Type": "application/json"}
# payload = {"id":"5aa041c9047ef6338d5358b1"}
# transfer_order_get = requests.get("https://api.skulabs.com/transfer_order/get",headers=headers, params=payload)
# transfer_order_list["items"] = transfer_order_get.json()["transfer_order"]["items"]
# transfer_order_list["id"] = transfer_order_get.json()["transfer_order"]["_id"]
# transfer_order_list["source_warehouse_id"] = transfer_order_get.json()["transfer_order"]["source_warehouse_id"]
# transfer_order_list["destination_warehouse_id"] = transfer_order_get.json()["transfer_order"]["destination_warehouse_id"]
# print(type(transfer_order_list))
                  
# # #                       --------Edits a transfer_order--------


# payload = {
#   "transfer_order_id": transfer_order_list["id"],
#   "items": transfer_order_list["items"],
#   "source_warehouse_id": transfer_order_list["source_warehouse_id"],
#   "destination_warehouse_id": transfer_order_list["destination_warehouse_id"],
#   "notes": transfer_order_list["notes"]
# }

# transfer_order = requests.put("https://api.skulabs.com/transfer_order/update",headers=headers, data=json.dumps(payload))
# print(transfer_order.json())



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