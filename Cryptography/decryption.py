# AES Decryption
from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path


class Decrypter:
    def __init__(self, key):
        self.key = key

    def decrypt(self, ciphertext):
        key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext)
        # with open(file_name[:-4], 'wb') as fo:
        #     fo.write(dec)
        # os.remove(file_name)
        return dec
