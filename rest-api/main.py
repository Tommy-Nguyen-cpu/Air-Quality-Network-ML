#! ./venv/bin/python3

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

# import tensorflow as tf
# from tensorflow import keras
import pandas as pd

import re
from io import StringIO

app = Flask(__name__)
CORS(app, support_credentials=True)

# model = tf.keras.models.load_model('../Air Quality ML/AirQModel.h5')

class File:
    def __init__(self, filename, cols, data):
        self.filename = filename
        self.cols = cols
        self.data = data
        self.getDF()
    
    def getDF(self):
        self.df = pd.read_csv(
            StringIO('\n'.join(self.data)),
            sep = ',',
            header = None,
            names = self.cols,
        )

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
        cols = lines[4].split(',')
        data = lines[5:-2]
        files.append(File(file_name, cols, data))

    return jsonify({'success': True})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
