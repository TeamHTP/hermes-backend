from flask import Flask, request, jsonify
from users import *

app = Flask(__name__)
database = 'hermes.db'


@app.route('/user/find', methods=['GET'])
def find_user():
    username = request.args.get('user_uid', '')
    # service = request.args.get('user_service', '')
    public_key = find_user_db(database, username)
    # return jsonify([username, service])
    return jsonify([public_key])


@app.route('/user/create', methods=['GET'])
def create_user():
    username = request.args.get('user_uid', '')
    # service = request.args.get('user_service', '')
    public_key = request.args.get('user_public_key', '')
    create_user_db(username, public_key)
    # return jsonify([username, service, public_key])
    return jsonify([username, public_key])


if __name__ == '__main__':
    initialize(database)
    app.run(host='0.0.0.0')
