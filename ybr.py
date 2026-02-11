from flask import Flask, request, jsonify, redirect, make_response, send_file, send_from_directory, flash, url_for, after_this_request, render_template
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    title="Yellow Brick Road - Start"
    resp = make_response(render_template('index.html', title=title), 200)
    return resp # redirect('https://holly-merrick-liston.clientsecure.me', code=302)

@app.route('/bio/<name>')
def bio(name):
    title = f"Therapist Bio - {name}"
    name_lower = name.lower()
    resp = make_response(render_template(f'therapist-bio-{name_lower}.html', title=title, name=name))
    return resp

# @app.route('/holly')
# def holly():
#     resp = make_response(render_template('therapist-bio-holly.html'), 200)
#     return resp

@app.route('/brittani')
def brittani():
    title = f"Therapist Bio - Brittani"
    resp = make_response(render_template('therapist-bio-brittani.html', title=title), 200)
    return resp

@app.route('/forms/contact', methods=['POST'])
def formscontact():
    data = 'A squirrel was here and left nuffing.'
    if request.method == 'POST':
        data = request.get_data()
    return data

if __name__ == "__main__":
    from pathlib import Path
    path, file = os.path.split(Path( __file__ ).absolute())
    print(path)
    os.chdir(path)
    app.root_path = path
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'Mumpitz'
    app.run(port=6789)