from flask import Flask
from flask_cors import CORS
from login.handler.login_handler import user_login  # Import the user_login function

app = Flask(__name__)

# Enable CORS for the specified routes
CORS(app, resources={r"/avasya/*": {"origins": "http://localhost:8080"}})

# Register the login route
app.add_url_rule('/avasya/resident/login', view_func=user_login, methods=['POST', 'OPTIONS'])

if __name__ == '__main__':
    app.run(debug=True)