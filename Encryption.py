from cryptography.fernet import Fernet

key = Fernet.generate_key()  # store in a secure location
# PRINTING FOR DEMO PURPOSES ONLY, don't do this in production code
print("Key:", key.decode())

def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)

key = Fernet.generate_key()
print(key.decode())

message = 'John Doe'
token = encrypt(message.encode(), key)
print(token)

token.decode()

decrypt(token, key).decode()

#####################################################################
>>> import json
>>> import base64
>>> d = {"alg": "ES256"} 
>>> s = json.dumps(d)  # Turns your json dict into a str
>>> print(s)
{"alg": "ES256"}
>>> type(s)
<class 'str'>
>>> base64.b64encode(s)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.2/base64.py", line 56, in b64encode
    raise TypeError("expected bytes, not %s" % s.__class__.__name__)
TypeError: expected bytes, not str
>>> base64.b64encode(s.encode('utf-8'))
b'eyJhbGciOiAiRVMyNTYifQ=='

import base64
# Base64 encoded string
encoded_string = "BijQQlCyBnROt+evGRIicg==" # BijQQlCyBnROt+evGRIicg==
# Decode the Base64 string
decoded_bytes = base64.b64decode(encoded_string)
print(f"Decoded bytes: {decoded_bytes}")
decoded_string = decoded_bytes.decode('ascii') # ascii
print(f"Decoded string: {decoded_string}")


import hashlib

s = "Order~CREATED"
res = hashlib.md5(s.encode())
print(res.hexdigest())

import base64

data = b"0628d04250b206744eb7e7af19122272"
encoded = base64.b64encode(data)
print(encoded) # Output: b'R2Vla3NGb3JHZWVrcw=='


