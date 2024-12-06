#!/bin/python3

from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
plaintext = b"So will i praise you Jesus"
ciphertext = cipher_suite.encrypt(plaintext)
print(f'Ciphertext: {ciphertext}')
decrypted_message = cipher_suite.decrypt(ciphertext)
print(f'Decrypted Message : {decrypted_message}')
