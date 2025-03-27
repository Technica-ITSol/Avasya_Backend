from flask import request, jsonify
from login.services import login_services

def user_login():
    if request.method == 'OPTIONS':
        return '', 200
    data = request.get_json()
    userid = data.get("email")
    password = data.get("password")
    
    if login_services.check_user_exists(userid):
        if login_services.authenticate_user(userid, password):
            return jsonify({"message": f"Welcome {userid}"})
        else:

            return jsonify({"error": "Password mismatched"}), 401
    else:
        return jsonify({"error": "Invalid User Details"}), 404


def society_login():
    data = request.get_json()
    userid = data.get("userid")
    password = data.get("password")
    
    if login_services.check_society_exists(userid):
        if login_services.authenticate_society(userid, password):
            return jsonify({"message": f"Welcome {userid}"})
        else:
            return jsonify({"error": "Password mismatched"}), 401
    else:
        return jsonify({"error": "Invalid User Details"}), 404

def admin_login():
    data = request.get_json()
    userid = data.get("userid")
    password = data.get("password")
    
    if userid == "admin" and password == "admin":
        return jsonify({"message": "Welcome Technica-ITSol"})
    return jsonify({"error": "Invalid Admin Attempt of Login"}), 403

