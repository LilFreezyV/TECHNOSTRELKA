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



@app.route('/recs', methods=['POST'])
def recs():
    data = request.json
    uid = data.get('uid')
    res, status = core.get_recs(uid)
    return jsonify({
        'content': res,
        'status': status
    })


@app.route('/find', methods=['POST'])
def find():
    data = request.json
    uid = data.get('uid')
    query = data.get('q')
    return core.find_by_query(query, uid)


if __name__ == "__main__":
    env = os.environ.get('ENVIRONMENT')
    # app.run(debug = env=='development', host='0.0.0.0', port=5001)
    app.run(debug=True, host='0.0.0.0', port=5001)
