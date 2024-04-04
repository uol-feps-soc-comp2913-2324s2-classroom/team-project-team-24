# endpoints/friends.py
from flask import Blueprint, Response, request, jsonify
from flask_jwt_extended import get_current_user, jwt_required
from app import db, app
from app.db_functions import *
from app.models import User
import os

bp = Blueprint('account', __name__, url_prefix='/account')

@bp.route('/set-details', methods=['POST'])
@jwt_required()
def set_account_details():
    # recieve user ID and new password
    user = get_current_user()

    # OLD CODE
    # data = request.get_json()

    # Retrieve JSON data
    data = request.form.to_dict()
    # Retrieve profile photo file
    profile_photo = request.files.get('profilePhoto')
    
    print(data)
    print(request.files["profilePhoto"].read().decode("utf-8"))

    # OLD CODE
    # # I don't mind if any/all of the data is missing
    # if data.get('name') is not None:
    #     user.name = data['name']

    # if data.get('email') is not None:
    #     user.email = data['email']

    # if data.get('age') is not None:
    #     user.age = data['age']

    # if data.get('gender') is not None:
    #     user.gender = data['gender']

    
    # Handle JSON data
    if 'name' in data:
        user.name = data['name']

    if 'email' in data:
        user.email = data['email']

    if 'age' in data:
        user.age = data['age']

    if 'gender' in data:
        user.gender = data['gender']

    # Handle profile photo upload
    if profile_photo:
        # Save the uploaded file
        filename = save_uploaded_file(profile_photo)
        # Update user's profile_photo attribute with file path
        user.profile_photo = filename

    db.session.commit()

    return Response(f"Details successfully updated", 200)

# TODO: INSERT SAVE PROFILE PIC
# def save_uploaded_file(file):
#     # Create a unique filename
#     filename = secure_filename(file.filename)
#     filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
#     # Save the file to disk
#     file.save(filepath)
    
#     return filename

@bp.route('/get-details', methods=['GET'])
@jwt_required()
def get_account_details():
    # recieve user
    user = get_current_user()
    membership = MembershipPlan.query.filter_by(id=user.membership_id).first()

    # return trails
    return jsonify({
        "name": user.username,
        "email": user.email,
        "profilePhoto": user.profile_picture,
        "membershipTier": membership.name if membership is not None else None,
        "gender": user.gender,
        "age": user.age,
        "paymentRegularity": membership.payment_regularity if membership is not None else None
    })

@bp.route('/change-password', methods=['POST'])
@jwt_required()
def change_password():
    # recieve user ID and new password
    user = get_current_user()
    password = request.form.get("password")

    # ensure new password given
    if password == None:
        return jsonify({"error": "Missing new password"}), 400

    # change password
    user.password = hash_pwd(password)
    db.session.commit()

    return Response(f"Password successfully changed", 200)

@bp.route('/delete', methods=['GET'])
@jwt_required()
def delete_account():
    # recieve user
    user = get_current_user()

    # delete account
    db.session.delete(user)
    db.session.commit()

    return Response(f"Account deleted", 200)
