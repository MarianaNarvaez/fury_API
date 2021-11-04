import os
from datetime import datetime, timedelta
from melitk.kvsclient import KVSDataBase, Item, exceptions
import logging


logging.basicConfig(
    format='%(asctime)s - %(levelname)s : %(message)s', level=logging.INFO)

#os.environ["KEY_VALUE_STORE_TESTPRODUCTION_CONTAINER_NAME"] = "testproduction"
#os.environ["KEY_VALUE_STORE_TESTPRODUCTION_END_POINT_READ"] = "http://localhost:6001"
#os.environ["KEY_VALUE_STORE_TESTPRODUCTION_END_POINT_WRITE"] = "http://localhost:6001"

class KVS_Storage:

    def __init__(self):
        self.kvs_client = self.connect()
    

    def connect(self):
        try:
            kvs_db = KVSDataBase(config={"KVS_CONTAINER_NAME": "testproduction"})
            return kvs_db

        except exceptions.KVSConnectionError:
            print('Error creating KVS connection, ')
        except Exception as ex:
            print('Error creating connection, ', ex)

    def save(self, key, val):
        item = Item(key, val)
        self.kvs_client.save(item)

    def get_val(self, ite_item_id):
        ite_item_id = self.kvs_client.get(ite_item_id) 
        if ite_item_id != None:
            rel = ite_item_id.value
        else: 
            ite_item_id = "No se encontro el valor"
        return ite_item_id

    def delete(self, ite_item_id):
        self.kvs_client.delete(ite_item_id)

    def update(self, key, val):
        item = Item(key, val)
        self.kvs_client.update(item)



