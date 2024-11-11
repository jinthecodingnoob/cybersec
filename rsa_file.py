# Reference: code borrows from official documentation
# https://stuvel.eu/python-rsa-doc/

import rsa

# Step 1: Generate RSA keys
public_key, private_key = rsa.newkeys(2048)

# Step 2: Function to encrypt a file
def encrypt_file(input_file, output_file, pub_key):
    with open(input_file, 'rb') as f:
        data = f.read()
    encrypted_data = rsa.encrypt(data, pub_key)
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)

# Step 3: Function to decrypt a file
def decrypt_file(input_file, output_file, priv_key):
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = rsa.decrypt(encrypted_data, priv_key)
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

# Example usage
input_filename = 'asymmetric/in/sensitive.txt'
encrypted_filename = 'asymmetric/out/sensitive_enc'
decrypted_filename = 'asymmetric/out/sensitive_dec'

# Encrypt the file
encrypt_file(input_filename, encrypted_filename, public_key)

# Decrypt the file
decrypt_file(encrypted_filename, decrypted_filename, private_key)

# Save the keys
with open('asymmetric/keys/public_key.pem', 'wb') as f:
    f.write(public_key.save_pkcs1('PEM'))

with open('asymmetric/keys/private_key.pem', 'wb') as f:
    f.write(private_key.save_pkcs1('PEM'))

print("Encryption and Decryption completed. Files are ready for download.")

# Read for PEM oe DER formats
# https://www.ssl.com/guide/pem-der-crt-and-cer-x-509-encodings-and-conversions/