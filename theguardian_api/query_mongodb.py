from pymongo import MongoClient
import re
import app_config
import pandas as pd

class MongoDb:
    def __init__(self, conn_string=app_config.conn_string, db_name=app_config.db_name):
        self.client = MongoClient(conn_string)
        self.db = self.client[db_name]

    def get_df_from_db(self, collection_name, query={}):
        cursor = self.db[collection_name].find(query)
        df = pd.DataFrame(list(cursor))
        del df['_id']

        return df

    def get_items_by_keyword(self, keyword ,collection_name):
        rgx = re.compile('.*' + keyword + '.*', re.IGNORECASE)  # compile the regex

        result = self.db[collection_name].find({'article_headline': rgx})

        return result