def func(x):
    x = 7   # defining a local x, not changing the global one

x = 3
func(x)
print(x)    # prints: 3
