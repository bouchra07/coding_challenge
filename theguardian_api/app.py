from flask import Flask
from query_mongodb import MongoDb

app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def all_data():
    mongodb = MongoDb()
    df = mongodb.get_df_from_db()
    del df['_id']

    return df.to_json(orient='index')


app.run(host='0.0.0.0', port=5000)