from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from cryptography.fernet import Fernet
import json

import tools

symKey = b'UEbJAk-waFRWtpquNTFR0Z35PQlU6oxLlbG6bnYXM30='
cipher = Fernet(symKey)

app = Flask('RFID Management Server')
CORS(app, origins="http://localhost:3000")

@app.route('/log-in', methods=['POST'])
def log_in_callback():
    # decrypt received id
    idEnc = request.get_json()
    id = json.loads(cipher.decrypt(idEnc.get('id')))    
    tools.login(id)
    return jsonify({'Response': 'Logged in'})

# this request sends a name to logout from web client, not an id. No need to encrypt/decrypt. 
@app.route('/log-out', methods=['POST'])
def log_out_callback():
    name = request.get_json().get('name')
    tools.logout(name)
    return jsonify({'Response': 'Logged out'})

@app.route('/is-logged-in', methods=['POST'])
def is_logged_in_callback():
    # sends a 0/1 to indicate is user is logged in. If 1, also sends the name of the user
    isLoggedIn, name = tools.is_logged_in()
    return jsonify({'isLoggedIn': isLoggedIn, 'name': name})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3001)