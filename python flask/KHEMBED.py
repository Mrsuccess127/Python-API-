#GET REQUEST
from flask import Flask, jsonify, request

app = Flask(__name__)

embedded = [{"name":"Nsisong Peters"}, {"name":"Jacob Zaccheus"}, {"name":"Adiele Oliver"}, {"name":"Ini-abasi Bernard"}, {"name":"Daniel Etukudo"}, {"name":"Elijah"}]

@app.route('/embed', methods=['GET'])
def embed():
    return jsonify({"embedded":embedded})

#To return a particular name
@app.route('/embed/<string:name>', methods=['GET'])
def returnsingle(name):
    member = [user for user in embedded if user['name']== name]
    return jsonify({'member': member[0]})

#POST REQUEST
@app.route('/embed', methods=['POST'])
def returnpost():
    user = {'name': request.json['name']}
    embedded.append(user)
    return jsonify({'embedded':embedded})

#PUT REQUEST
@app.route('/embed/<string:name>', methods=['PUT'])
def returnput(name):
    mem = [user for user in embedded if user['name']==name]
    mem[0]['name'] = request.json['name']
    return jsonify({"embedded":mem[0]})

#DELETE REQUEST
@app.route('/embed/<string:name>', methods=['DELETE'])
def removename(name):
    mem = [mem for mem in embedded if mem['name']==name]
    embedded.remove(mem[0])
    return jsonify({'embedded':embedded})

if __name__ == '__main__':
    app.run(debug=True)