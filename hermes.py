from flask import Flask, request, jsonify, make_response
from users import *


app = Flask(__name__)
database = 'hermes.db'
initialize(database)


@app.route('/api/v1/twitter/public_key/get', methods=['GET'])
def twitter_public_key_get():
    twitter_user_id = request.args.get('twitter_user_id', '')
    result = twitter_public_keys_select(database, twitter_user_id)

    response_code = 500
    response_json = {
        'api_version': '0.1.0',
        'source': '/api/v1/twitter/public_key/get',
        'success': False,
        'data': {
            'twitterUserId': result['twitterUserId']
        }
    }

    if 'publicKey' in result:
        response_code = 200
        response_json['success'] = True
        response_json['data']['publicKey'] = result['publicKey']
    else:
        response_code = 404
        response_json['errors'] = []
        response_json['errors'].append({
            'details': 'Twitter user id not found'
        })

    return make_response((jsonify(response_json), response_code, {
        'Access-Control-Allow-Origin': 'https://twitter.com',
        'Access-Control-Allow-Methods': 'GET'
    }))

@app.route('/api/v1/twitter/public_key/update', methods=['GET'])
def twitter_public_key_update():
    twitter_user_id = request.args.get('twttier_user_id', '')
    public_key = request.args.get('public_key', '')
    result = twitter_public_keys_insert_or_replace(database, twitter_user_id, public_key)

    response_code = 200
    response_json = {
        'api_version': '0.1.0',
        'source': '/api/v1/twitter/public_key/update',
        'success': True,
        'data': {
            'twitterUserId': result['twitterUserId'],
            'publicKey': result['publicKey']
        }
    }

    return make_response((jsonify(response_json), response_code, {
        'Access-Control-Allow-Origin': 'https://twitter.com',
        'Access-Control-Allow-Methods': 'GET'
    }))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
