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
