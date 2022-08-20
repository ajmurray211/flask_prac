from flask import Flask, jsonify, request, redirect, url_for
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin

app= Flask(__name__)
cors = CORS(app)
# app.config['MONGO_URI'] = 'mongodb+srv://admin123:0000@cluster0.vzqog5g.mongodb.net/flask_prac?retryWrites=true&w=majority'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/flask_prac'
app.config['CORS_Headers'] = 'Content-Type'

mongo = PyMongo(app)

@app.route('/', methods = ['GET'])
def getAll():
    holder = list()
    currentCollection = mongo.db.flask_prac
    for i in currentCollection.find():
        holder.append({'name':i['name'], 'genre': i['favGenre'], 'game': i['favGame']})
    return jsonify(holder)

@app.route('/<name>', methods = ['GET'])
@cross_origin()
def getByName(name):
    currentCollection = mongo.db.flask_prac
    data = currentCollection.find_one({'name': name})
    return jsonify({'name':data['name'], 'genre': data['favGenre'], 'game': data['favGame']})

@app.route('/postData', methods = ['POST'])
def postData():
    currentCollection = mongo.db.flask_prac
    name = request.json['name']
    genre = request.json['genre']
    game = request.json['game']
    currentCollection.insert_one({'name': name, 'favGenre': genre, 'favGame': game})
    return jsonify({'name': name, 'genre': genre, 'game': game})

@app.route('/deleteData/<name>', methods = ['DELETE'])
def deleteData(name):
    currentCollection = mongo.db.flask_prac
    currentCollection.delete_one({'name': name})
    return redirect(url_for('getAll'))

@app.route('/updateData/<name>', methods = ['PUT'])
def updateData(name):
    currentCollection = mongo.db.flask_prac
    updatedName = request.json['name']
    currentCollection.update_one({'name':name}, {'$set': {'name': updatedName}})
    return redirect(url_for('getAll'))

if __name__ == '__main__':
    app.run(debug =True)