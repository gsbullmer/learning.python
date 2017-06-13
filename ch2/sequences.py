"""sequences.py"""


# strings
# 4 ways to make a string
str1 = 'This is a string. We built it with single quotes.'
str2 = "This is also a string, but built with double quotes."
str3 = '''This is built using triple quotes,
          so it can span multiple lines.'''
str4 = """This too
          is a multiline one
          built with triple double-quotes."""
print(str4)     # A     # this is not supposed to be a print statement
# 'This too\nis a multiline one\nbuilt with triple double-quotes.'
print(str4)     # B
# This too
# is a multiline one
# built with triple double-quotes.


# encode / decode
s = "This is üŋíc0de"   # unicode string: code points
print(type(s))  # <class 'str'>
encoded_s = s.encode('utf-8')  # utf-8 encoded version of s
print(encoded_s)
# b'This is \xc3\xbc\xc5\x8b\xc3\xadc0de'  # result: bytes object
print(type(encoded_s))  # another way to verify it
# <class 'bytes'>
print(encoded_s.decode('utf-8'))    # let's revert to the original
# 'This is üŋíc0de'
bytes_obj = b"A bytes object"   # a bytes object
print(type(bytes_obj))  # <class 'bytes'>


# length
print(len(str1))    # 49


# indexing and slicing
s = "The trouble is you think you have time."
print(s[0])     # 'T'   # indexing at position 0, which is the first char
print(s[5])     # 'r'   # indexing at position 5, which is the sixth char
print(s[:4])    # 'The '    # slicing, we specify only the stop position
print(s[4:])    # slicing, we specify only the start position
# 'trouble is you think you have time.'
print(s[2:14])  # slicing, both start and stop positions
# 'e trouble is'
print(s[2:14:3])    # slicing, start, stop and step (every 3 chars)
# 'erb '
print(s[:])     # quick way of making a copy
# 'The trouble is you think you have time.'
