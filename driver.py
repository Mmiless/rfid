from mfrc522 import SimpleMFRC522

mrfc = MFRC522()

while(1):
	try:
		id = mrfc.read()
		print(f"ID: ${id}")
	except AUTHERROR:
		continue




