# This is not intended to be run


# single decorator
def func(arg1, arg2, ...):
    pass
func = decorator(func)


# is equivalent to the following:
@decorator
def func(arg1, arg2, ...):
    pass


# multiple decorators
def func(arg1, arg2, ...):
    pass
func = deco1(deco2(func))


# is equivalent to the following:
@deco1
@deco2
def func(arg1, arg2, ...):
    pass


# decorator with arguments
def func(arg1, arg2, ...):
    pass
func = decoarg(argA, argB)(func)


# is equivalent to the following:
@decoarg(argA, argB)
def func(arg1, arg2, ...):
    pass
