from Crypto.Cipher import AES
from pkcs7 import PKCS7Encoder
import base64


def encrypt(shared_key, IV, clear_text):
	aes = AES.new(shared_key, AES.MODE_CBC, IV)
	aes.block_size = 128
	return base64.b64encode(aes.encrypt(PKCS7Encoder().encode(clear_text)))

def decrypt(shared_key, IV, cipher_text):
	aes_decrypter = AES.new(shared_key, AES.MODE_CBC, IV)
	aes_decrypter.block_size = 128
	return PKCS7Encoder().decode(aes_decrypter.decrypt(base64.b64decode(cipher_text)))


if __name__ == "__main__":
	shared_key = "abc123ty9TW1abc123ty9TW1"
	IV = "rTF25nTrrTF25nTr" #in my case that I was trying to replicate the IV was known

	clear_text = "Testing 123"
	cipher_text = encrypt(shared_key, IV, clear_text)
	print(cipher_text)

	clear_text = decrypt(shared_key, IV, cipher_text)
	print(clear_text)

