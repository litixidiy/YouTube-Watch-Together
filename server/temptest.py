from flask import Flask

#Creating an instance of Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
