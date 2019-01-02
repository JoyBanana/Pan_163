from flask import Flask, request, render_template
from request.fileOpe import *
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('download.html')


@app.route('/files', methods=['GET'])
def list_file():
    return json.dumps(getFiles())


@app.route('/delete', methods=['POST'])
def delete():
    fileName = request.form['fileName']
    deleteFile(fileName)
    return render_template('download.html')


if __name__ == '__main__':
    app.run()
