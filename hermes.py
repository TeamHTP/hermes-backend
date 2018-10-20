from flask import Flask, request, jsonify
from users import *


app = Flask(__name__)
database = 'hermes.db'
initialize(database)


@app.route('/api/v1/twitter/public_key/get', methods=['GET'])
def twitter_public_key_get():
    twitter_user_id = request.args.get('user_id', '')
    result = twitter_public_keys_select(database, twitter_user_id)

    reponse = {
        'api_version': '0.1.0',
        'source': '/api/v1/twitter/public_key/get',
        'success': False,
        'data': {
            'twitterUserId': result['twitterUserId']
        }
    }

    if 'publicKey' in result:
        reponse['success'] = True
        reponse['data']['publicKey'] = result['publicKey']
    else:
        reponse['errors'] = []
        reponse['errors'].append({
            'details': 'Twitter user id not found'
        })

    return jsonify(reponse)

@app.route('/api/v1/twitter/public_key/update', methods=['GET'])
def twitter_public_key_update():
    twitter_user_id = request.args.get('user_uid', '')
    public_key = request.args.get('public_key', '')
    result = twitter_public_keys_insert_or_replace(database, twitter_user_id, public_key)

    reponse = {
        'api_version': '0.1.0',
        'source': '/api/v1/twitter/public_key/update',
        'success': True,
        'data': {
            'twitterUserId': result['twitterUserId'],
            'publicKey': result['publicKey']
        }
    }

    return jsonify(reponse)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
