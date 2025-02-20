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


@app.route('/recs')
def recs():
    return core.get_recs()

@app.route('/find', methods=['POST'])
def find():
    data = request.json
    query = data.get('q')
    return core.process_query(query)

if __name__ == "__main__":
    env = os.environ.get('ENVIRONMENT')
    app.run(debug = env=='development', host='0.0.0.0', port=5001)