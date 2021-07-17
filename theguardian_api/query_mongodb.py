from pymongo import MongoClient
import app_config
import pandas as pd

class MongoDb:
    def __init__(self, conn_string=app_config.conn_string, db_name=app_config.db_name):
        self.client = MongoClient(conn_string)
        self.db = self.client[db_name]

    def get_df_from_db(self, collection_name=app_config.collection_name, query={}):
        cursor = self.db[collection_name].find(query)
        df = pd.DataFrame(list(cursor))

        return df

