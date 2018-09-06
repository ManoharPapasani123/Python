import sys
import pandas as pd
import pymongo
import json
import  os

mng_client = pymongo.MongoClient('localhost', 27017)
mng_db = mng_client['mydb'] # Replace mongo db name
collection_name = 'agent' # Replace mongo db collectionname
db_cm = mng_db[collection_name]
# cdir = os.path.dirname(__file__)
# file_res = os.path.join(cdir, filepath)

data = pd.read_excel('E:/AZ_Agent.xlsx')
data_json = json.loads(data.to_json(orient='records'))
db_cm.remove()
db_cm.insert(data_json,check_keys=False,continue_on_error=False,manipulate=True)
print('success')
mng_client.close()