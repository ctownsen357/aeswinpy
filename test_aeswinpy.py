import unittest 
from aeswinpy import *

class AESTest(unittest.TestCase):
    def test_encrypt(self):
        shared_key = "SomeTestKey!2345"
        IV = "1234567890123456"
        clear_text = "this is a test."
        cipher_text = encrypt(shared_key, IV, clear_text)
        self.assertEqual(cipher_text, "+1A1ZV+oweRvqX4kruP7kw==")
        self.assertEqual(decrypt(shared_key, IV, cipher_text), clear_text)

if __name__ == '__main__':
        unittest.main()

