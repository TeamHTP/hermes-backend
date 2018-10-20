import sqlite3


def initialize(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS TwitterPublicKey
        (
            TwitterId TEXT PRIMARY KEY,
            PublicKey TEXT NOT NULL
        );
        ''')
    conn.commit()
    conn.close()

def twitter_public_keys_select(database, twitter_user_id):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT PublicKey
        FROM TwitterPublicKey
        WHERE TwitterId=?
    ''', (twitter_user_id,))
    select_result = cursor.fetchone()
    conn.close()

    result = {
        'twitterUserId': twitter_user_id
    }

    if select_result:
        (public_key,) = select_result
        result['publicKey'] = public_key
    
    return result

def twitter_public_keys_insert_or_replace(database, twitter_user_id, public_key):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT OR REPLACE
        INTO TwitterPublicKey(TwitterId, PublicKey)
        VALUES(?,?)
    ''', (twitter_user_id, public_key))
    conn.commit()
    conn.close()

    result = {
        'twitterUserId': twitter_user_id,
        'publicKey': public_key
    }

    return result
