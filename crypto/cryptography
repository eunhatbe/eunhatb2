from cryptography.fernet import Fernet
# create key
key = Fernet.generate_key()
# crypto
cipher_suite = Fernet(key)

cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")

plain_text = cipher_suite.decrypt(cipher_text)

print("encrypt_text", cipher_text)
print("dncrypt_text", plain_text)



