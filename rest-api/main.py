#! ./venv/bin/python3

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

import tensorflow as tf
from tensorflow import keras

import re

app = Flask(__name__)
CORS(app, support_credentials=True)

model = tf.keras.models.load_model('./Air Quality ML/AirQModel.h5')

class File:
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data


@app.route('/upload_csv', methods = ['POST'])
@cross_origin(supports_credentials=True)
def upload_csv():
    data = request.get_data().decode('utf-8').replace('\r', '')

    file_start = data.split('\n')[0]
    file_chunks = data.split(file_start)

    files = []
    for file in file_chunks:
        if file in ['', '--\n']: continue
        lines = file.split('\n')
        headers = lines[1]
        file_name = re.findall('"([^"]*)"', headers)[1]
        data = lines[4:-2]
        files.append(File(file_name, data))

    print(files[0].data[0])

    return jsonify({'success': True})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
