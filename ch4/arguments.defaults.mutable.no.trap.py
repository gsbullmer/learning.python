def func(a=None, b=None):
    if a is None:
        a = []
    if b is None:
        b = {}
    print(a)
    print(b)
    print('#' * 12)
    a.append(len(a))    # this will affect a's default value
    b[len(a)] = len(a)  # and this will affect b's one

func()
func(a=[1, 2, 3], b={'B': 1})
func()
