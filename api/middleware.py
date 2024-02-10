from urllib.parse import urlparse
from urllib.parse import parse_qs
import sqlite3

import utiles.mac
import logging
import json
import time
from datetime import date
from datetime import datetime


logging.basicConfig(filename='example.txt', filemode='w', level=logging.DEBUG)


def register(url, self):
    logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path),
                 str(self.headers))
    try:
        parsed_url = urlparse(url)
        user_email = parse_qs(parsed_url.query)['email'][0]
        password = parse_qs(parsed_url.query)['password'][0]
        hash = utiles.mac.generate_hmac(password)

        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        sql = 'SELECT * FROM users WHERE email="' + user_email + '"'
        cursor.execute(sql)
        rows = len(cursor.fetchall())

        if rows == 0:
            cursor.execute('INSERT INTO users (email, password, hash) VALUES (?, ?, ?)',
                           (user_email, password, hash))
            conn.commit()
            return True
        else:
            return False
    except:
        return False


def login(url, self):
    content_length = int(self.headers['Content-Length'])
    post_data = self.rfile.read(content_length)
    logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                 str(self.path), str(self.headers), post_data.decode('utf-8'))

    data = json.loads(post_data.decode('utf-8'))
    user_email = data['email']
    password = data['password']

    logging.info(post_data.decode('utf-8'))

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    sql = 'SELECT * FROM users WHERE email="' + user_email + '"'
    cursor.execute(sql)
    results = cursor.fetchone()

    # test output results
    # f = open("debug.txt", "a")
    # f.write(str(results[1]))
    # f.close()

    row_user_id = results[0]
    row_user_hash = results[3]

    logging.info("ROW?", results[0])

    if results[0] is not None:
        hash = utiles.mac.generate_hmac(password)

        if row_user_hash == hash:
            logging.info(hash)
            # generate token
            access_token = utiles.mac.generate_hmac(str(time.gmtime()))
            token_time = today = datetime.now()
            cursor.execute(
                'INSERT INTO token ( user_id, access_token, created_date) VALUES (?, ?, ?)',
                (row_user_id, access_token, token_time))
            conn.commit()
        return True
    else:
        return False
