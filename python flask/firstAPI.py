from flask import Flask, request, jsonify  #jsonify is to output data in Json format from python format

#To initialize app.....define app using flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message':'it works'})

#To run server
if __name__ == 'main':
    app.run(debug=true, port=8080)


