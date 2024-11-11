import cryptography
from cryptography.fernet import Fernet
#salt
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# key without salt
key = Fernet.generate_key()
print(key)

file = open('keys/key.key', 'wb') #wb = write bytes
file.write(key)
file.close()

# new key with a salt
password_provided = 'secret'
password = password_provided.encode()

salt = b"\xb9\x1f|}'S\xa1\x96\xeb\x154\x04\x88\xf3\xdf\x05"

kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend())

key = base64.urlsafe_b64encode(kdf.derive(password))
print(key)

# Get the key from the file
file = open('keys/key.key', 'rb')
key = file.read()
file.close()

#  Open the file to encrypt
with open('assets/sensitive.csv', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

# Write the encrypted file
with open('assets/sensitive.csv.encrypted', 'wb') as f:
    f.write(encrypted)


