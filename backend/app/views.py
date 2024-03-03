from app import app
from flask import render_template, url_for, redirect, flash, request
import json


@app.route('/', methods=['GET'])
def home():
    return 'Greetings from the API!'

@app.route('/add', methods=['POST'])
def add():
    post_data = request.get_json()
    response_object = json.dumps({'status': 'success'})
    response_object['addition'] = post_data['a'] + post_data['b']
    return response_object, 201

