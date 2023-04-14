import jwt
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'

@app.route('/api/v1/login', methods=['POST'])
def login():
    # Your code to authenticate user and generate JWT token
    payload = {'username': 'example', 'exp': datetime.utcnow() + timedelta(minutes=30)}
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'token': token})

@app.route('/api/v1/user', methods=['GET'])
def get_user():
    token = request.headers.get('Authorization').split()[1]
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401
    # Your code to fetch user data from database or other API
    return jsonify(user_data)
