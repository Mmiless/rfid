from cryptography.fernet import Fernet

symKey = Fernet.generate_key()
print(str(symKey))
