# Make sure that you have installed pycryptodome
# pip install pycryptodome

# Reference: code borrows from official documentation
# https://www.pycryptodome.org

# Import necessary modules from pycryptodome
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

# Step2: Generate new RSA key
# Create an RSA key pair with a key size of 2048 bits
def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    with open("asymmetric/keys/private.cryptodome.pem", "wb") as pr:
        pr.write(private_key)
    with open("asymmetric/keys/public.cryptodome.pem", "wb") as pu:
        pu.write(public_key)

# https://pycryptodome.readthedocs.io/en/latest/src/cipher/oaep.html
def encrypt_file(file_path, public_key_path, encrypted_file_path):
    with open(public_key_path, "rb") as f:
        public_key = RSA.import_key(f.read())
    with open(file_path, "rb") as f:
        data = f.read()
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_data = cipher.encrypt(data)
    with open(encrypted_file_path, "wb") as f:
        f.write(encrypted_data)

def decrypt_file(encrypted_file_path, private_key_path, decrypted_file_path):
    with open(private_key_path, "rb") as f:
        private_key = RSA.import_key(f.read())
    with open(encrypted_file_path, "rb") as f:
        encrypted_data = f.read()
    cipher = PKCS1_OAEP.new(private_key)
    data = cipher.decrypt(encrypted_data)
    with open(decrypted_file_path, "wb") as f:
        f.write(data)

if __name__ == "__main__":
    generate_keys()  # Generate keys and save to files
    encrypt_file("asymmetric/in/sensitive.txt", "asymmetric/keys/public.cryptodome.pem", "asymmetric/out/sensitive_cryptodome_enc")  # Encrypt the file and specify output path
    decrypt_file("asymmetric/out/sensitive_cryptodome_enc", "asymmetric/keys/private.cryptodome.pem", "asymmetric/out/sensitive_cryptodome_dec")  # Decrypt the file and specify output path
