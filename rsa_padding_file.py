# import all libraries to support rsa and padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import os

# in this example we are not storing keys
# you can easily modify code to do that 
# using previous examples from lectorial 5.

# another way to create key is manually
# BUT SHOULD THIS BE DONE?

def generate_keys():
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    # Generate public key
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_file(file_path, public_key, output_path):
    # Read the file's data
    with open(file_path, "rb") as file:
        plaintext = file.read()
    
    # Encrypt the data
    ciphertext = public_key.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    # Write the encrypted data to the specified output file
    with open(output_path, "wb") as file:
        file.write(ciphertext)

def decrypt_file(encrypted_file_path, private_key, output_path):
    # Read the encrypted data
    with open(encrypted_file_path, "rb") as file:
        ciphertext = file.read()
    
    # Decrypt the data
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    # Write the decrypted data back to the specified output file
    with open(output_path, "wb") as file:
        file.write(plaintext)

# Main function to generate keys, encrypt and decrypt
def main():
    private_key, public_key = generate_keys()

    # Specify your file path here
    file_path = "asymmetric/in/sensitive.txt"
    encrypted_file_path = "asymmetric/out/sensistive_enc"
    decrypted_file_path = "asymmetric/out/sensitive_dec"
    
    encrypt_file(file_path, public_key, encrypted_file_path)
    decrypt_file(encrypted_file_path, private_key, decrypted_file_path)

if __name__ == "__main__":
    main()

'''

RATIONALE:

Textbook RSA

- takes a plaintext message m, a public key (e,n) (that's usually not kept secret) and 
- creates a ciphertext c = m^e mod n and 
- can be decrypted with the secret key (d) via m = c^d mod n 

This may leak information. 

For example, if you were using textbook RSA to send a simple message that's one of a few options 
(e.g., it's a yes/no message or an order to buy X shares of a stock), an attacker could just encrypt
all the likely messages with public key and see which one exactly matches the true ciphertext.


'''
