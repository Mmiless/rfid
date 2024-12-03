from mfrc522 import SimpleMFRC522
from pprint import pprint
from cryptography.fernet import Fernet
import json
import requests

symKey = b'UEbJAk-waFRWtpquNTFR0Z35PQlU6oxLlbG6bnYXM30='
cipher = Fernet(symKey)

def sendRequest(idEnc):

	print("sending")
	headers = {
		'Content-Type': 'application/json',
		'Authorization': None   # not using HTTP secure
	}

	# send request to server to login
	response = requests.post("http://172.20.10.3:3001/log-in", headers=headers, json={'id':idEnc.decode()})
	pprint(response.json()) 
	main()

def main():
	mrfc = SimpleMFRC522()

	while (1):
		try:
			id, not_id = mrfc.read()
			print(id)
			# encrypt id
			idBytes = json.dumps(id).encode()
			idEnc = cipher.encrypt(idBytes)
			print(idEnc)
			sendRequest(idEnc)
			break

		except:
			continue

if __name__ == "__main__":
	main()

