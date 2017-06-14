# basic for loop
for number in [0, 1, 2, 3, 4]:
    print(number)
print()

# The same thing, but using range
for number in range(5):
    print(number)
print()

# more about ranges
print(list(range(10)))      # one value: from 0 to value (excluded)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(3, 8)))    # two values: from start to stop (excluded)
# [3, 4, 5, 6, 7]
print(list(range(-10, 10, 4)))  # three values: step is added
# [-10, -6, -2, 2, 6]
print()

# iterate over list
surnames = ['Rivest', 'Shamir', 'Adleman']
for position in range(len(surnames)):
    print(position, surnames[position])
print()

for position in range(len(surnames)):
    print(surnames[position][0], end='')
print()

# for..in
for surname in surnames:
    print(surname)
print()

# enumerate
for position, surname in enumerate(surnames):
    print(position, surname)
