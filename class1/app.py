from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Hello World</h1>
    <h1>Hello World</h1>
    <h1>Hello World</h1>
    <h1>Hello World</h1>
    <h1>Hello World</h1>
    <h1>Hello World</h1>
    <h1>Hello World</h1>
    """

@app.route('/login/<name>')
def login(name):
    return "Hello from Login to "+name

@app.route('/showhtml')
def showhtml():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True,port=8080)