from mfrc522 import SimpleMFRC522

mrfc = SimpleMFRC522()

while(1):
	try:
		id, text = mrfc.read()
		print(f"ID: ${id}" + " Text: ${text}")
	except AUTHERROR:
		continue



