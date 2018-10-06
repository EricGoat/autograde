from flask import Flask, jsonify
app = Flask(__name__)
test_data = {'ok': True, 'data': ['thing1', 'thing2']}


@app.route("/")
def hello_world():
    return jsonify(test_data)
