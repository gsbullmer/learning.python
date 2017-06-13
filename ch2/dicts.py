"""dicts.py"""


a = dict(A=1, Z=-1)
b = {'A': 1, 'Z': -1}
c = dict(zip(['A', 'Z'], [1, -1]))
d = dict([('A', 1), ('Z', -1)])
e = dict({'Z': -1, 'A': 1})
print(a == b == c == d == e)    # True  # are they all the same?    # indeed!


# zip
print(list(zip(['h', 'e', 'l', 'l', 'o'], [1, 2, 3, 4, 5])))
# [('h', 1), ('e', 2), ('l', 3), ('l', 4), ('o', 5)]
print(list(zip('hello', range(1, 6))))  # equivalent, more pythonic
# [('h', 1), ('e', 2), ('l', 3), ('l', 4), ('o', 5)]


# basic
d = {}
d['a'] = 1  # let's set a couple of (key, value) pairs
d['b'] = 2
print(len(d))   # 2     # how many pairs?
print(d['a'])   # 1     # what is the value of 'a'?
print(d)    # {'a': 1, 'b': 2}  # how does `d` look now?
del d['a']  # let's remove `a`
print(d)    # {'b': 2}
d['c'] = 3  # let's add 'c': 3
print('c' in d)     # True  # membership is checked against the keys
print(3 in d)   # False     # not the values
print('e' in d)     # False
d.clear()   # let's clean everything from this dictionary
print(d)    # {}


# views
d = dict(zip('hello', range(5)))
print(d)    # {'e': 1, 'h': 0, 'o': 4, 'l': 3}
print(d.keys())     # dict_keys(['e', 'h', 'o', 'l'])
print(d.values())   # dict_values([1, 0, 4, 3])
print(d.items())    # dict_items([('e', 1), ('h', 0), ('o', 4), ('l', 3)])
print(3 in d.values())  # True
print(('o', 4) in d.items())    # True


# other methods
print(d)    # {'e': 1, 'h': 0, 'o': 4, 'l': 3}
d.popitem()     # ('e', 1)  # removes a random item (useful in algorithms)
print(d)    # {'h': 0, 'o': 4, 'l': 3}
print(d.pop('l'))   # 3     # remove item with key `l`
print(d.pop('not-a-key'))   # remove a key not in dictionary: KeyError
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'not-a-key'
print(d.pop('not-a-key', 'default-value'))  # with a default value?
# 'default-value'  # we get the default value
d.update({'another': 'value'})  # we can update dict this way
d.update(a=13)  # or this way (like a function call)
print(d)    # {'a': 13, 'another': 'value', 'h': 0, 'o': 4}
print(d.get('a'))   # 13    # same as d['a'] but if key is missing no KeyError
print(d.get('a', 177))  # 13    # default value used if key is missing
print(d.get('b', 177))  # 177   # like in this case
print(d.get('b'))       # key is not there, so None is returned


# setdefault
d = {}
print(d.setdefault('a', 1))     # 1     # 'a' is missing, we get default value
print(d)    # {'a': 1}  # also, the key/value pair ('a', 1) has now been added
print(d.setdefault('a', 5))     # 1     # let's try to override the value
print(d)    # {'a': 1}  # didn't work, as expected


# setdefault example
d = {}
d.setdefault('a', {}).setdefault('b', []).append(1)
print(d)    # {'a': {'b': [1]}}
