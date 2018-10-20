from flask import Flask, request


app = Flask(__name__)


@app.route('/user/find', methods=['GET'])
def find_user():
    username = request.args.get('user_uid', '')
    service = request.args.get('user_service', '')
    print(username)
    print(service)


@app.route('/user/create', methods=['GET'])
def create_user():
    username = request.args.get('user_uid', '')
    service = request.args.get('user_service', '')
    public_key = request.args.get('user_public_key', '')
    print(username)
    print(service)
    print(public_key)


if __name__ == '__main__':
    app.run()
