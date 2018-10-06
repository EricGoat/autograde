from flask import Flask, jsonify
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'description': 'Walk Dogs'
    },
    {
        'id': 2,
        'description': 'Feed Cats'
    }
]

test_data = {'ok': True, 'data': tasks}


@app.after_request
def add_headers(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route("/")
def hello_world():
    return jsonify(test_data)
