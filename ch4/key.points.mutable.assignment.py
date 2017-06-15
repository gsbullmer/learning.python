def func(x):
    x[1] = 42   # this affects the caller!
    x = 'something else'    # this points x to a new string object

x = [1, 2, 3]
func(x)
print(x)    # prints: [1, 42, 3]
