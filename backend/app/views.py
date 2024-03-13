from app import app
from flask import render_template, url_for, redirect, flash, request
from flask_jwt_extended import jwt_required


@app.route('/', methods=['GET'])
@jwt_required()
def home():
    return 'Greetings from the API!'

@app.route('/add', methods=['POST'])
def add():
    post_data = request.get_json()
    response_object = {'status': 'success'}
    response_object['addition'] = post_data['a'] + post_data['b']
    return response_object, 201

