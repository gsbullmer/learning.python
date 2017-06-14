n = 39
remainders = []
while n > 0:
    remainder = n % 2   # remainder of division by 2
    remainders.append(remainder)    # we keep track of remainders
    n //= 2     # we divide n by 2

# reassign the list to its reversed copy and print it
remainders = remainders[::-1]
print(remainders)

# the same thing using divmod, which is more pythonic
n = 39
remainders = []
while n > 0:
    n, remainder = divmod(n, 2)
    remainders.append(remainder)

# reassign the list to its reversed copy and print it
remainders = remainders[::-1]
print(remainders)
