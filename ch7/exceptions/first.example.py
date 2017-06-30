gen = (n for n in range(2))
print(next(gen))    # 0
print(next(gen))    # 1
print(next(gen))
# Traceback (most recent call last):
#   File "<stdin>", line 4, in <module>
#     print(next(gen))
# StopIteration
print(undefined_var)
# Traceback (most recent call last):
#   File "<stdin>", line 9, in <module>
#     print(undefined_var)
# NameError: name 'undefined_var' is not defined
mylist = [1, 2, 3]
print(mylist[5])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
mydict = {'a': 'A', 'b': 'B'}
print(mydict['c'])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'c'
print(1 / 0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
