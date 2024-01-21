from Crypto.Util.number import *

long_int = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
byte_str = long_to_bytes(long_int)

print(byte_str.decode('utf-8'))