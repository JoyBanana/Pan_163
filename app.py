from flask import Flask, request
from request.fileOpe import *
from flask_cors import cross_origin
import json

app = Flask(__name__)


@app.route('/files', methods=['GET'])
@cross_origin()
def list_file():
    return json.dumps(getFiles())


@app.route('/delete', methods=['POST'])
@cross_origin()
def delete():
    fileName = request.form['fileName']
    deleteFile(fileName)
    m_json = {'status': 'okay'}
    return json.dumps(m_json)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
