from flask import Flask, request
from request.fileOpe import *
from flask_cors import cross_origin, CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/files', methods=['GET'])
def list_file():
    return json.dumps(getFiles())


@app.route('/delete', methods=['POST'])
def delete():
    fileName = request.form['fileName']
    verify = request.form['user']
    print(fileName + '     ' + verify)
    if verify == 'joy':
        deleteFile(fileName)
        m_json = {'status': 'okay'}
        return json.dumps(m_json)
    return json.dumps({'status': 'filed'})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
