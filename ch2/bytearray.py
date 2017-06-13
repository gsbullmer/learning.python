"""bytearray.py"""


print(bytearray())      # bytearray(b'')    # empty bytearray object
print(bytearray(10))    # zero-filled instance with given length
# bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
print(bytearray(range(5)))  # bytearray from iterable of integers
# bytearray(b'\x00\x01\x02\x03\x04')
name = bytearray(b'Lina')  # A - bytearray from bytes
print(name.replace(b'L', b'l'))     # bytearray(b'lina')
print(name.endswith(b'na'))         # True
print(name.upper())                 # bytearray(b'LINA')
print(name.count(b'L'))             # 1
