word = 'Hello'
letters1 = set(c for c in word)
letters2 = {c for c in word}
print(letters1)     # prints: {'l', 'H', 'e', 'o'}
print(letters1 == letters2)     # prints: True