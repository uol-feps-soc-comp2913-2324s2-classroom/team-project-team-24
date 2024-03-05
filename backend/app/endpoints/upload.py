# endpoints/upload.py
from flask import Blueprint, Response
from flask import request
from ..models import User, Route


bp = Blueprint('upload', __name__)

@bp.route('/upload', methods=('POST',))
def upload():
    # data = request.get_json()
    # print(data)
    print("BLEEP")
    return Response(status=418)

# @bp.route('/register', methods=('POST',))
# def register():
#     data = request.get_json()
#     password = data['password']
#     username = data['username']

#     user = User.query.filter_by(username=username).first()
#     if user is None:
#         user = User(
#             username=username,
#             password=password
#         )

#         user.add()    
#         access_token = create_access_token(identity=user.id)
#         refresh_token = create_refresh_token(identity=user.id)

#         response = jsonify()
#         set_access_cookies(response, access_token)
#         set_refresh_cookies(response, refresh_token)

#         return response, 201
#     else:
#         return jsonify(message="Unable to create user."), 400
