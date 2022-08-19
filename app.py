from distutils.log import debug
from flask import Flask 
from flask_pymongo import PyMongo


app= Flask(__name__)
# app.config['MONGO_URI'] = 'mongodb+srv://admin123:0000@cluster0.vzqog5g.mongodb.net/flask_prac?retryWrites=true&w=majority'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/flask_prac'

mongo = PyMongo(app)


@app.route('/')
def basic():
    return

if __name__ == '__main__':
    app.run(debug =True)