# AES Encryption

import os
import os.path
from Cryptography import Encrypter

class KeyGeneration:
    def createkeyfile(keyfile, keyvalue):
        f = open(keyfile + ".txt", "w+")
        f.write(keyvalue)
        f.close()
        key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
        Encrypter(key).encrypt_file(keyfile + ".txt")
        return True

    def createplaintextfile(plaintextfilename, plaintext):
        f = open(plaintextfilename + ".txt", "w+")
        f.write(plaintext)
        f.close()
        key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
        Encrypter(key).encrypt_file(plaintextfilename + ".txt")
        return "PlainText File Generated."

    def checkforfileexist(filename):
        is_exist = os.path.exists(filename + ".txt.enc")
        return is_exist

