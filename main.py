from flask import Flask, request


app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():
    username = request.args.get('user_uuid', '')
    service = request.args.get('user_service', '')
    pass


@app.route('/user/create', methods=['GET'])
def create_user():
    username = request.args.get('user_uid', '')
    service = request.args.get('user_service', '')
    public_key = request.args.get('user_public_key', '')
    pass


if __name__ == '__main__':
    app.run()
