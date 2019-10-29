from flask import Flask, render_template, redirect, request, jsonify

from flask_pymongo import PyMongo

app = Flask(__name__)

# app.config['MONGO_URI'] = 'mongodb+srv://mansoor:mansoor11@flask-app-yd5cz.mongodb.net/test?retryWrites=true&w=majority'

# mongo = PyMongo(app)

users = [
    {
        "name": "ali",
        "password": "abc"
    },
    {
        "name": "hussain",
        "password": "abc1"
    },
    {
        "name": "ali1",
        "password": "abc1"
    },{
        "name": "ali2",
        "password": "abc2"
    },
    {
        "name": "ali3",
        "password": "abc4"
    },
    {
        "name": "ali4",
        "password": "abc4"
    },
    {
        "name": "ali5",
        "password": "abc5"
    },
    {
        "name": "ali6",
        "password": "abc7"
    },
]

@app.route('/')
def index():
    return jsonify({"message": "Hello from 5001", "users": users})




@app.route('/test', methods=["POST"])
def test():
    data = request.form
    data = dict(data)
    for i, v in enumerate(users):
        if(data['userName'] == v['name'] and data['password'] == v['password']):
            # login = mongo.db.login
            # result = login.insert_one(data)
            # print(result.inserted_id)
            return redirect('http://127.0.0.1:5000/home')
    return redirect('http://127.0.0.1:5000/login')

if __name__ == "__main__":
    app.run(debug=True, port=5001)