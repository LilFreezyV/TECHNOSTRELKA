from flask import Flask, jsonify, request
import core
import os

app = Flask('SearchEngine')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    uid, status = core.login(username, password)
    return jsonify({
        'uid': uid,
        'status': status
    })

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    uid, status = core.register(
        data.get('username'),
        data.get('surname'),
        data.get('name'),
        data.get('number'),
        data.get('email'),
        data.get('password')
    )
    return jsonify({
        'uid': uid,
        'status': status
    })


@app.route('/recs')
def recs():
    return core.get_recs()

@app.route('/find', methods=['POST'])
def find():
    data = request.json
    query = data.get('q')
    return core.find_by_query(query)

if __name__ == "__main__":
    env = os.environ.get('ENVIRONMENT')
    # app.run(debug = env=='development', host='0.0.0.0', port=5001)
    app.run(debug=True, host='0.0.0.0', port=5001)