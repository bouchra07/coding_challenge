from flask import Flask
from query_mongodb import MongoDb
from bson.json_util import dumps
import app_config


app = Flask(__name__)


@app.route('/', methods=["GET"])
def all_data():
    mongodb = MongoDb()
    df = mongodb.get_df_from_db()
    del df['_id']

    return df.to_json(orient='index')

@app.route('/<column>==<value>', methods=["GET"])
def specific_data(column,value):

    query = {column : value}
    mongodb = MongoDb()
    df = mongodb.get_df_from_db(app_config.collection_name,query)
    del df['_id']

    return df.to_json(orient='index')

@app.route('/<key>', methods=["GET"])
def search_by_keyword(key):
    mongodb = MongoDb()
    # df = mongodb.get_df_from_db()
    result = mongodb.get_items_by_keyword(key)
    list_cur = list(result)
    json_data = dumps(list_cur)
    return json_data

app.run(host='0.0.0.0', port=5000)