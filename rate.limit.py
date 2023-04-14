from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["100 per day", "10 per hour"]
)

@app.route('/api/v1/user', methods=['GET'])
@limiter.limit("5 per minute")
def get_user():
    # Your code to fetch user data from database or other API
    return jsonify(user_data)
