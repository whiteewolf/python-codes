import sys
import hashlib

if sys.version_info < (3, 6):
    import sha3

str = input("Message : ")

str_encoded = str.encode()

sha3 = hashlib.sha384(str_encoded)

print(sha3.hexdigest())