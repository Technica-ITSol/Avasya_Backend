import re
import sqlite3

def validate_email(email):
    return re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)

def validate_password(password):
    return len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isalpha() for c in password)

def validate_contact_number(number):
    return number.isdigit() and 10 <= len(number) <= 15

def connect_db():
    return sqlite3.connect("LoginCredentialsDetails.db")

def register_user(full_name, email, password, contact_number, whatsapp_number, emergency_contact, flat_number, role):
    if not all([full_name, email, password, contact_number, emergency_contact, flat_number, role]):
        return {'message': 'All fields are required!', 'status': 400}
    if not validate_email(email):
        return {'message': 'Invalid email format!', 'status': 400}
    if not validate_password(password):
        return {'message': 'Password must be at least 8 characters long with letters and numbers!', 'status': 400}
    if not validate_contact_number(contact_number) or not validate_contact_number(emergency_contact):
        return {'message': 'Invalid contact number format!', 'status': 400}
    
    db = connect_db()
    cursor = db.cursor()
    
    if role == 'Society Head':
        status = 'Pending Admin Approval'
        table = "SocietyDetails"
    else:
        status = 'Pending Society Head Approval'
        table = "UserDetails"
    
    query = f"""
        INSERT INTO {table} (Userid, Password, Society_Name, Ph_number, Email_id)
        VALUES (?, ?, ?, ?, ?)
    """
    values = (full_name, password, email, contact_number, whatsapp_number)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    db.close()
    
    if role == 'Society Head':
        return {'message': 'Your request is pending admin approval.', 'status': 201}
    else:
        return {'message': 'Your request is pending society head approval.', 'status': 201}