from Cryptography import Encrypter
from Cryptography import Decrypter
import os
import time
from GUI import MainPanel
if __name__ == "__main__":
    app = MainPanel()
    app.mainloop()
# #
# key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
# enc = Encrypter(key)
# dec = Decrypter(key)
# # clear = lambda: os.system('cls')
#
#
# def clear():
#     return os.system('cls')
#
#
# while True:
#     clear()
#     choice = int(input('''
# Press '1' to encrypt Data and Write to File.
# Press '2' to decrypt Data and Write to File.
# Press '3' to exit.\n
# '''))
#     clear()
#     if choice == 1:
#         password = str(input("Enter a password that will be used for Encryption/Decryption: "))
#         rePassword = str(input("Confirm password: "))
#         if password != rePassword:
#             break
#         else:
#             keyFileName = str(input("Enter Filename where you want to save your encrypted key: "))
#             f = open(keyFileName + ".txt", "w+")
#             f.write(password)
#             f.close()
#             enc.encrypt_file(keyFileName + ".txt")
#             print("Key Generated Successfully.")
#             time.sleep(5)
#             clear()
#             plaintext = str(input("Enter Plaintext: "))
#             plainTextFileName = str(input("Enter newname of file to save your encrypted text: "))
#             f = open(plainTextFileName + ".txt", "w+")
#             f.write(plaintext)
#             f.close()
#             enc.encrypt_file(plainTextFileName + ".txt")
#     elif choice == 2:
#         toBeDecryptedFile = str(input("Enter name of file to decrypt: "))
#         # decryptKeyFile = str(input("Enter name of the key file: "))
#         # decryptKey = str(input("Enter key: "))
#         #
#         # dec.decrypt_file(toBeDecryptedFile + ".txt.enc", )
#         # with open(toBeDecryptedFile + ".txt", 'rb') as fo:
#         #     message = fo.read()
#         # print("Decrypted text: ", message.decode())
#         # enc.encrypt_file(toBeDecryptedFile + ".txt")
#         isExist = os.path.exists(toBeDecryptedFile + ".txt.enc")
#         if not isExist:
#             print("File Not found..")
#             time.sleep(2)
#             clear()
#             continue
#         decryptKeyFile = str(input("Enter name of the key file: "))
#         isExist = os.path.exists(decryptKeyFile + ".txt.enc")
#         if not isExist:
#             print("File Not found..")
#             time.sleep(2)
#             clear()
#             continue
#         decryptKey = str(input("Enter key: "))
#         dec.decrypt_file(decryptKeyFile + ".txt.enc")
#         with open(decryptKeyFile + ".txt", 'rb') as fo:
#             decryptedKey = fo.read()
#         if decryptedKey.decode() != decryptKey:
#             print("Key not Match..")
#             time.sleep(2)
#             clear()
#             enc.encrypt_file(decryptKeyFile + ".txt")
#             continue
#         enc.encrypt_file(decryptKeyFile + ".txt")
#         dec.decrypt_file(toBeDecryptedFile + ".txt.enc", )
#         with open(toBeDecryptedFile + ".txt", 'rb') as fo:
#             message = fo.read()
#         print("Decrypted text: ", message.decode())
#         enc.encrypt_file(toBeDecryptedFile + ".txt")
#
#     elif choice == 3:
#         exit()
#     else:
#         print("Please select a valid option!")
