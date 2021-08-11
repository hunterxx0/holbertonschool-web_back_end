#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ GET /api/v1/auth_session/login
    Return:
      - the Logged in User object JSON represented
    """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400
    try:
        user = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    for x in user:
        if not x.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    user = user[0]
    sID = auth.create_session(user.id)
    resp = jsonify(user.to_json())
    resp.set_cookie('_my_session_id', sID)
    return resp


@app_views.route(
    '/auth_session/logout',
    methods=['DELETE'],
    strict_slashes=False
)
def logout() -> str:
    """ DELETE /api/v1/auth_session/logout
    Return:
      - Log out the User object    
    """
    from api.v1.app import auth

    if not auth.destroy_session(request):
        return False, abort(404)
    return jsonify({}), 200
