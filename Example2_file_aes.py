# import required module
from cryptography.fernet import Fernet

# key generation
key = Fernet.generate_key()

# string the key in a file
with open('keys/filekey.key', 'wb') as filekey:
    filekey.write(key)

# opening the key
with open('keys/filekey.key', 'rb') as filekey:
	key = filekey.read()

# using the generated key
fernet = Fernet(key)

# opening the original file to encrypt
with open('assets/sensitive.csv', 'rb') as file:
	original = file.read()
	
# encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and 
# writing the encrypted data
with open('assets/sensitive_encryp.csv', 'wb') as encrypted_file:
	encrypted_file.write(encrypted)

# decryption
# using the key
fernet = Fernet(key)

# opening the encrypted file
with open('assets/sensitive_encryp.csv', 'rb') as enc_file:
	encrypted = enc_file.read()

# decrypting the file
decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# writing the decrypted data
with open('assets/sensitive_decryp.csv', 'wb') as dec_file:
	dec_file.write(decrypted)
