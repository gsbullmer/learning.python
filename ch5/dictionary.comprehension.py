from string import ascii_lowercase
lettermap = dict((k, c) for c, k in enumerate(ascii_lowercase, 1))
print(lettermap)
lettermap = {c: k for k, c in enumerate(ascii_lowercase, 1)}
print(lettermap)
