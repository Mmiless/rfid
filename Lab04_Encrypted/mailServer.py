from flask import Flask
from flask import jsonify
from flask import request
from cryptography.fernet import Fernet

import argparse
import json
import mailboxManager

symKey = b'UEbJAk-waFRWtpquNTFR0Z35PQlU6oxLlbG6bnYXM30='
cipher = Fernet(symKey)
loggedIn = 0

app = Flask('RaspberryPi Mailbox Server')

"""
The @app.route() above the function is called a decorator. We will skip
explaining decorators in detail for brevity. The functions below, such as
get_mailbox_callback(), are callbacks that get called when certain types
of HTTP request are received by the Flask server. With the decorator's
input arguments below and the Flask server initialization in
if __name__ == '__main__':, this first callback is set to be specifically
called when a GET request is sent to the URL "http://0.0.0.0:[port]/mailbox"
"""

@app.route('/log-in', methods=['POST'])
def log_in_callback():
    """
    Summary: A callback which for when GET is called on [host]:[port]/mailbox

    Returns:
        string: A JSON-formatted string containing the response message
    """

    idEnc = request.get_json()
    id = json.loads(cipher.decrypt(idEnc.get('rfid')))    
    print(id)

    
    
    # Check that the password is valid
    if str(id) in json.loads(jsonify(mailbox_manager.get_id())):
           # Use Flask's jsonify function to format the dictionary as JSON
        response = jsonify({'Response': 'Password does not match'})
        
    else:
        response = jsonify({'Response': 'Password does not match'})

    # The object returned will be sent back as an HTTP message to the requester
    return response

# TODO: Use Flash's route() decorator to add support to your HTTP server for
# handling GET requests made to the URL '/mailbox/search'
#
# Use get_mailbox_callback() as an example. You'll need to use mailboxManager
# for this request as well, so make sure to spend some time understanding how
# it works and the features it provides.
#
# Your implementation should handle reasonable error cases as well, such as an
# incorrect password.

@app.route('/mailbox', methods=['GET'])
def get_mailbox_callback():
    """
    Summary: A callback which for when GET is called on [host]:[port]/mailbox

    Returns:
        string: A JSON-formatted string containing the response message
    """

    # Since we have `from flask import request` above, the 'request' object
    # will (magically) be available when the callback is called. `request` is
    # the object that stores all the HTTP message data (header, payload, etc.).
    # We will skip explaining how this object gets here because the answer is
    # a bit long and out of the scope of this lab.

    # Extract the key/value field for password
    paramEnc = request.args.get('params')
    paramDnc = cipher.decrypt(paramEnc.encode())
    params = json.loads(paramDnc.decode())
    id = params.get('id')


    # Check that the password is valid
    if str(id) in json.loads(jsonify(mailbox_manager.get_id())):
        # Use Flask's jsonify function to format the dictionary as JSON
        response = jsonify(mailbox_manager.get_id())

    else:
        response = jsonify({'Response': 'ID does not match'})

    # The object returned will be sent back as an HTTP message to the requester
    return response

# TODO: Use Flash's route() decorator to add support to your HTTP server for
# handling GET requests made to the URL '/mailbox/search'
#
# Use get_mailbox_callback() as an example. You'll need to use mailboxManager
# for this request as well, so make sure to spend some time understanding how
# it works and the features it provides.
#
# Your implementation should handle reasonable error cases as well, such as an
# incorrect password.

@app.route('/mailbox/search/', methods=['GET'])
def search_mailbox_callback():

    paramEnc = request.args.get('params')
    paramDnc = cipher.decrypt(paramEnc.encode())
    params = json.loads(paramDnc.decode())
    print("Decrypted params:", params)

    id = params.get('id')
    searchF = params.get('field')
    searchT = params.get('text')

        # Check that the password is valid
    if str(id) in json.loads(jsonify(mailbox_manager.get_id())):
            # Use Flask's jsonify function to format the dictionary as JSON 
        response = jsonify({'Response': mailbox_manager.get_id(searchF, searchT)})

    else:
        if str(id) == None:
            response = jsonify({'Response': 'Missing password'})

        else:
            response = jsonify({'Response': 'Password does not match'})






    # The object returned will be sent back as an HTTP message to the requester
    return response


@app.route('/mailbox/delete', methods=['DELETE'])
def delete_mail_callback():
    """
    Summary: A callback for when DELETE is called on [host]:[port]/mailbox/delete

    Returns:
        string: A JSON-formatted string containing the response message
    """

    # Get the payload containing the list of mail ids to delete
    payloadEnc = request.get_json()
    payload = json.loads(cipher.decrypt(payloadEnc.get('payload')))    
    print(payload)

    # Check that the password is valid
    if str(payload['id']) in json.loads(jsonify(mailbox_manager.get_id())):
        num_deleted = mailbox_manager.delete_id(payload['mail_ids'])
        response = jsonify({'Response': '{} emails deleted'.format(num_deleted)})

    else:
        if str(payload['id']) == None:
            response = jsonify({'Response': 'Missing password'})

        else:
            response = jsonify({'Response': 'Password does not match'})

    # The object returned will be sent back as an HTTP message to the requester
    return response

@app.route('/add-id', methods=['POST'])
def post_mail_callback():
    """
    Summary: A callback for when POST is called on [host]:[port]/mailbox/send-mail

    Returns:
        string: A JSON-formatted string containing the response message
    """

    # Get the payload containing the sender, subject and body parameters
    payloadEnc = request.get_json()
    payload = json.loads(cipher.decrypt(payloadEnc.get('payload')))
    print(payload)


    mailbox_manager.add_mail(payload)
    response = {'Response': 'Mail sent'}

    # The object returned will be sent back as an HTTP message to the requester
    return json.dumps(response)

if __name__ == '__main__':
    # Set up argparse, a Python module for handling command-line arguments
    parser = argparse.ArgumentParser(prog='mailServer',
            description='Script to start up mail server')

    

    args = parser.parse_args()

    mailbox_manager = mailboxManager.mailboxManager()

    app.run(debug=False, host='0.0.0.0', port=5000)

