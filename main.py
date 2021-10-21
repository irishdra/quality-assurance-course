import os
import random
import string
from flask import Flask, request, send_from_directory

HOST = '0.0.0.0'
PORT = 3000
FOLDER_PATH = './serverdata'
FILE_PATH = '/data.txt'
FILE_NAME = 'data.txt'
FILE_SIZE = 1024

app = Flask(__name__)

data_to_write = ''.join(random.choices(string.ascii_uppercase + string.digits, k=FILE_SIZE))
file = open(FOLDER_PATH + FILE_PATH, 'w+')
file.write(data_to_write)
file.close()

@app.route('/', methods=['GET'])
def get_file():
    try:
        return send_from_directory(FOLDER_PATH, FILE_NAME)
    except FileNotFoundError:
        abort(404)

app.run(host=HOST, port=PORT)