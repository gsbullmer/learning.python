def func(x):
    x[1] = 42   # this affects the caller!

x = [1, 2, 3]
func(x)
print(x)    # prints: [1, 42, 3]
