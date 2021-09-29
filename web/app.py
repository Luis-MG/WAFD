from flask import Flask, redirect, url_for, render_template
import requests
import json

app = Flask(__name__,template_folder='template')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/admin')
def admin():
    return render_template("admin.html")

@app.route('/get_persons')
def get_persons():
    url = 'http://api/get_persons'
    response = requests.get(url) 
    response_json = json.loads(response.text)
    return response_json

@app.route('/add_person')
def add_person():
    url = 'http://api/add_person'
    response = requests.get(url) 
    response_json = json.loads(response.text)
    return response_json
    
@app.route('/delete_persons')
def delete_persons():
    url = 'http://api/delete_persons'
    response = requests.get(url) 
    response_json = json.loads(response.text)
    return response_json


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)