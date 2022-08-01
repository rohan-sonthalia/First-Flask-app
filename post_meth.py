from flask import Flask, jsonify

app = Flask(__name__)

usersList = ['Aaron', 'Bianca', 'Cat', 'Danny', 'Elena']

@app.route('/')
def intro():
    return "Welcome to my API"

@app.route('/users', methods=['GET'])
def users():
    return jsonify({ 'users': [user for user in usersList] })

@app.route('/users/<int:id>', methods=['GET'])
def userById(id):
    return jsonify({ 'username': usersList[id]  })

@app.route('/users/<string:name>', methods=['GET'])
def getUserByName(name):
    if name in usersList:
        return "User exists"
    else :
        return "User does not exist"

@app.route('/users/<string:name>', methods=['POST'])
def addUserByName(name):
    usersList.append(name)
    return jsonify({ 'message': 'New user added'  })

app.run(debug=True)
