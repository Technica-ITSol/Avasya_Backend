import sqlite3

conn = sqlite3.connect("LoginCredentialsDetails.db", check_same_thread=False)
cursor = conn.cursor()

def check_user_exists(user_id):
    cursor.execute("SELECT 1 FROM UserDetails WHERE Email_id = ? LIMIT 1", (user_id,))
    exists = cursor.fetchone() is not None
    return exists

def authenticate_user(user_id, password):    
    cursor.execute("SELECT Password FROM UserDetails WHERE Email_id = ?", (user_id,))
    result = cursor.fetchone()
    if result and result[0] == password:
        return True  # Authentication successful
    return False

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
