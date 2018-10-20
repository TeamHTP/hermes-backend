from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/user/find', methods=['GET'])
def find_user():
    username = request.args.get('user_uid', '')
    service = request.args.get('user_service', '')
    return jsonify([username, service])


@app.route('/user/create', methods=['GET'])
def create_user():
    username = request.args.get('user_uid', '')
    service = request.args.get('user_service', '')
    public_key = request.args.get('user_public_key', '')
    return jsonify([username, service, public_key])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
