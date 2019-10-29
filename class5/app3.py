from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://mansoor:mansoor11@flask-app-yd5cz.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def index():
    usersData = mongo.db.usersData
    data = usersData.find({},{'password': 0, '_id': 0})
    data1 = []
    for i in data:
        # i['_id'] = str(i['_id'])
        data1.append(i)
    print(data1)
    return jsonify({"msg": "Hello PostMan", "data": data1})

@app.route('/findEmail', methods=["POST"])
def findEmail():
    data = dict(request.form)
    usersData = mongo.db.usersData
    data = usersData.find({"userName": data['userName'] },{'password': 0, '_id': 0})
    data1 = []
    for i in data:
        data1.append(i)
    return jsonify({"data": data1})

@app.route('/findUserName/<userName>')
def findUserName(userName):
    usersData = mongo.db.usersData
    data = usersData.find({"userName": userName },{'password': 0, '_id': 0})
    data1 = []
    for i in data:
        data1.append(i)
    return jsonify({"data": data1})


app.run(debug=True)