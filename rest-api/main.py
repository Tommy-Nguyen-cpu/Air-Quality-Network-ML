from file import File

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

import re


app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/upload_csv', methods = ['POST'])
@cross_origin(supports_credentials=True)
def upload_csv():
    data = request.get_data().decode('utf-8').replace('\r', '')

    file_start = data.split('\n')[0]
    file_chunks = data.split(file_start)

    files = {}
    for file in file_chunks:
        if file in ['', '--\n']: continue
        lines = file.split('\n')
        headers = lines[1]
        file_name = re.findall('"([^"]*)"', headers)[1]
        cols = lines[4].split(',')
        data = lines[5:-2]
        f = File(file_name, cols, data)
        files[f.filename] = f.pred.to_csv(index=False)

    return jsonify({'success': True, 'results': files})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
