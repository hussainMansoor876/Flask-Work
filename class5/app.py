from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://mansoor:mansoor11@flask-app-yd5cz.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)
print(mongo)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/home')
def home():
    return "Hello from Home Page"

@app.route('/signupAuth', methods=["POST"])
def signupAuth():
    data = dict(request.form)
    print(data)
    usersData = mongo.db.usersData
    result = usersData.find_one({"email": data['email']})
    print(result)
    if(result):
        return redirect('/signup')
    # for i in result:
    #     print(i)
    bcrypt_password = bcrypt.hashpw(data['password'].encode('utf8'), bcrypt.gensalt(12))
    data['password'] = bcrypt_password
    usersData.insert_one(data)
    return redirect('/login')

@app.route('/loginAuth', methods=["POST"])
def loginAuth():
    data = dict(request.form)
    usersData = mongo.db.usersData
    findEmail = usersData.find_one({"email": data['email']})
    if(findEmail):
        checkPassword = bcrypt.checkpw(data['password'].encode('utf8'), findEmail['password'])
        if(checkPassword):
            return redirect('/home')
        return redirect('/login')
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)





