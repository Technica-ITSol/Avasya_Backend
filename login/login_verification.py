# Login verification program
import sqlite3

conn = sqlite3.connect("../LoginCredentialsDetails.db")
cursor = conn.cursor()

def userlogin(userid, password):
    if check_user_exists(userid):
        if authenticate_user(userid, password):
            text = f"Welcome {userid}"
            return text
        else:
            return "Password mismatched"
    else:
        return "Invalid User Details"

def check_user_exists(user_id):
    cursor.execute("SELECT 1 FROM UserDetails WHERE Userid = ? LIMIT 1", (user_id,))
    exists = cursor.fetchone() is not None
    return exists

def authenticate_user(user_id, password):    
    cursor.execute("SELECT Password FROM UserDetails WHERE userid = ?", (user_id,))
    result = cursor.fetchone()
    if result and result[0] == password:
        return True  # Authentication successful
    return False

def societylogin(userid, password):
    if check_society_exists(userid):
        if authenticate_society(userid, password):
            text = f"Welcome {userid}"
            return text
        else:
            return "Password mismatched"
    else:
        return "Invalid User Details"

def check_society_exists(user_id):
    cursor.execute("SELECT 1 FROM SocietyDetails WHERE Userid = ? LIMIT 1", (user_id,))
    exists = cursor.fetchone() is not None
    return exists

def authenticate_society(user_id, password):    
    cursor.execute("SELECT Password FROM SocietyDetails WHERE Userid = ?", (user_id,))
    result = cursor.fetchone()
    if result and result[0] == password:
        return True  # Authentication successful
    return False

def adminlogin(userid,password):
    if userid=="admin" & password=="admin":
        return "Welcome Technica-ITSol"
    return "Invalid Admin Attempt of Login"

userid = input("Userid: ")
password = input("Password: ")
LoginType = input("Login Type: ")
if LoginType=="User"or"user":
    print(userlogin(userid,password))
elif LoginType=='Society'or"society":
    print(societylogin(userid,password))
elif LoginType=="admin"or"Admin":
    print(adminlogin(userid,password))