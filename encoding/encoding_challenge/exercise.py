import base64
import codecs
import json

from Crypto.Util.number import *
from pwn import *  # pip install pwntools

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

for k in range(101):
    received = json_recv()

    #print("Received type: ")
    #print(received["type"])
    #print("Received encoded value: ")
    #print(received["encoded"])

    encoded = received["encoded"]
    encoding = received["type"]
    decoded = ""

    if encoding == "base64":
        decoded = base64.b64decode(encoded).decode()
    elif encoding == "hex":
        decoded = bytes.fromhex(encoded).decode('utf-8')
    elif encoding == "rot13":
        decoded = codecs.decode(encoded, 'rot_13')
    elif encoding == "bigint":
        decoded = long_to_bytes(int(encoded, 16)).decode('utf-8') 
    elif encoding == "utf-8":
        decoded = "".join([chr(b) for b in encoded])

    print("Decoded value: " + str(decoded))
    to_send = {
        "decoded": decoded
    }
    json_send(to_send)

# json_recv()
# received = json_recv()

# print("Received type: ")
# print(received["type"])
# print("Received encoded value: ")
# print(received["encoded"])

# encoded = received["encoded"]
# encoding = received["type"]
# decoded = ""

# if encoding == "base64":
#     #decoded = base64.b64decode(self.challenge_words.encode()).decode() # wow so encode
#     decoded = base64.b64decode(encoded).decode()
# elif encoding == "hex":
#     byte_str = bytes.fromhex(encoded)
#     decoded = byte_str.decode('utf-8')
# elif encoding == "rot13":
#     decoded = codecs.decode(encoded, 'rot_13')
# elif encoding == "bigint":
#     byte_str = long_to_bytes(encoded)
#     tmp = byte_str.decode('utf-8')
#     byte_str_2 = bytes.fromhex(tmp)
#     decoded = byte_str_2.decode('utf-8')
# elif encoding == "utf-8":
#     decoded = [chr(b) for b in encoded]

# print("Decoded value: " + str(decoded))
# to_send = {
#     "decoded": decoded
# }
# json_send(to_send)

# json_recv()
