#from storage import KVS_Storage
#from app.item.storage import KVS_Storage
from .storage import KVS_Storage
from melitk.connectors import Presto
import pandas as pd



class ITEM:

    def __init__(self, **kwargs):
        self.kvs_item = KVS_Storage()

    def insert_all_items(self):

        presto = Presto(user="******", password="*******")

        QueryUY = """
        SELECT...
        FROM 
        LIMIT 60
        """

        df = pd.read_sql(QueryUY, presto.engine)
        data = df.set_index('ite_item_id').T.to_dict() 
        
        for key, val in data.items():
            self.kvs_item.save(key, {'ite_item_title': val['ite_item_title'],'ite_date_created':val['ite_date_created'],'ite_condition':val['ite_condition']})
        
        return {'data': data}, 5
  
    def get(self, ite_item_id):
        val = self.kvs_item.get_val(ite_item_id)
        return val
        
    def add_item(self, ite_item_id, ite_item_title, ite_date_created, ite_condition):
        self.kvs_item.save(ite_item_id, {'ite_item_title':ite_item_title, 'ite_date_created': ite_date_created,'ite_condition':ite_condition})
        return "Save successful"

    def del_item(self, ite_item_id):
        self.kvs_item.delete(ite_item_id)
        return "Delete successful"

    def update_item(self, ite_item_id, ite_item_title, ite_date_created, ite_condition):
        self.kvs_item.update(ite_item_id, {'ite_item_title':ite_item_title, 'ite_date_created': ite_date_created,'ite_condition':ite_condition})
        return "Update successful"

    