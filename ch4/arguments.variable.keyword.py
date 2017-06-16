def func(**kwargs):
    print(kwargs)

# all calls equivalent. They pring: {'a': 1, 'b': 42}
func(a=1, b=42)
func(**{'a': 1, 'b': 42})
func(**dict(a=1, b=42))
