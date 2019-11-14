from flask import Flask, request, jsonify  #jsonify is to output data in Json format from python format

#To initialize app.....define app using flask
app = Flask(__name__)

languages = [{"name":"python"}, {"name":"C"}, {"name":"C++"}, {"name":"Ruby"}]
@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'it works'})

@app.route('/lang', methods=['GET'])
def returnlang():
    return jsonify({"languages":languages})

#To get a particular name
@app.route('/lang/<string:name>', methods=['GET'])
def return_lang(name):
    langs = [language for language in languages if language['name']== name]
    return jsonify({'language': langs[0]})


#TO CREATE A POST REQUEST......we will append to the existing dictionary
@app.route('/lang', methods=['POST'])  #creating an end point
def postreq():
    language ={"name": request.json.get("name")}   #creating a format to add a new name to the existing dicitonary in json format
    languages.append(language)   #adding the new name to the existing dicitonary
    return jsonify({'languages':languages})

#PUT REQUEST
@app.route('/lang/<string:name>', methods=['PUT'])
def returnput(name):
    user = [user for user in languages if user['name'] == name]
    user[0]['name'] =request.json['name'] 
    return jsonify({'languages': user[0]})


#DELETE REQUEST
@app.route('/lang/<string:name>', methods=['DELETE'])
def removeone(name):
    user = [user for user in languages if user['name']==name]
    languages.remove(user[0])
    return jsonify({'language': languages})

#To run server
if __name__ == '__main__':
    app.run(debug=True)
