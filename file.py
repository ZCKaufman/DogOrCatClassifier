import os
from flask import jsonify, render_template, request, redirect, url_for
from flask import send_file

UPLOAD_FOLDER='./upload/'

def upload(filename):
    f = request.files['file']
    path = os.path.join(UPLOAD_FOLDER, filename)
    f.save(path)
    return "Upload success"

def download(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    return send_file(path, as_attachment=True)

def list_files():
    files = []
    for filename in os.listdir(UPLOAD_FOLDER):
        path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)
