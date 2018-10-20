import sqlite3


def initialize(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS USERS
             (ID INT PRIMARY KEY NOT NULL,
             TWITTERID INT UNIQUE NOT NULL,
             PUBLICKEY TEXT NOT NULL);''')
    conn.commit()
    conn.close()
    pass


# def find_user_db(database, username, service):
# #     pass
# #
# #
# # def create_user_db(database, username, service, public_key):
# #     pass

def find_user_db(database, username):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute('''SELECT PUBLICKEY FROM USERS WHERE TWITERID=?''', (username,))
    public_key = cursor.fetchone()
    conn.close()
    if public_key:
        return public_key
    return 'No user'


def create_user_db(database, username, public_key):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO USERS(TWITTERID, PUBLICKEY) VALUES(?,?)''', (username, public_key))
    conn.commit()
    conn.close()
    pass
