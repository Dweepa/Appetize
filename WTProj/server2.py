
import json
import os
import time
from flask import Flask, Response, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.json_util import dumps

app = Flask(__name__, static_url_path='', static_folder='public')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

app.config['MONGO_DBNAME'] = 'food'
app.config['MONGO_URI'] = "mongodb://localhost/food"
CORS(app)
mongo = PyMongo(app)
from pymongo import MongoClient
client = MongoClient('127.0.0.1', 27017)
db = client['food']


@app.route('/api/buzz', methods=['GET'])
def buzz():
    com = mongo.db.comments
    docs_list = com.aggregate([{'$group': { '_id': "$rest", 'count': { '$sum': 1 } } }, { '$sort': { 'count': -1 } }])
    output=[]
    cnt=0
    #print(count)
    for i in docs_list:
        output.append({i['_id']:i['count']})
    output2=[]
    element = {}
    for record in output:
        cnt+=1
        
        keys2 = record.keys()
        search= keys2[0]
        records = db['restaurants'].find({ "rest": search })
        for rest in records:
            element["rest"]=rest["rest"]
            element["description"]=rest["description"]
            element["image"]= rest["image"]
            if(len(output2)<9):
                output2.append(element)
            element={}
    return Response(
        json.dumps(output2),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods':'*'
        }
    )

@app.route('/api/comments', methods=['GET', 'POST'])
def comments_handler():
    com = mongo.db.comments
    restaurant="Toscano"
    if request.method == 'POST':
        new_comment = request.form.to_dict()
        print(new_comment)
        new_comment['id'] = int(time.time() * 1000)
        print(new_comment)
        # todo: remove restaurant
        uid = com.insert({"id":new_comment['id'],"name":new_comment['author'],"message":new_comment['text'],"rest":restaurant, "rating":new_comment['rating']})

    docs_list = list(com.find())
    output=[]
    for i in docs_list:
        print(i)
        # todo: remove
        output.append({"id": i['id'],"author":i['name'],"text":i['message'],"rest":restaurant,"rating":i['rating']})

    return Response(
        json.dumps(output),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods':'*'
        }
    )

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 3000)), debug=True)
