"""lists.py"""


# creation
print([])           # []            # empty list
print(list())       # []            # same as []
print([1, 2, 3])    # [1, 2, 3]     # as with tuples, items are comma separated
print([x + 5 for x in [2, 3, 4]])   # [7, 8, 9]         # Python is magic
print(list((1, 3, 5, 7, 9)))        # [1, 3, 5, 7, 9]   # list from a tuple
print(list('hello'))    # ['h', 'e', 'l', 'l', 'o']     # list from a string


# main methods
a = [1, 2, 1, 3]
a.append(13)        # we can append anything at the end
print(a)            # [1, 2, 1, 3, 13]
a.count(1)          # 2     # how many '1' are there in the list?
a.extend([5, 7])    # extend the list by another (or sequence)
print(a)            # [1, 2, 1, 3, 13, 5, 7]
print(a.index(13))  # 4     # position of '13' in the list (0-based indexing)
a.insert(0, 17)     # insert '17' at position 0
print(a)            # [17, 1, 2, 1, 3, 13, 5, 7]
print(a.pop())      # 7     # pop (remove and return) last element
print(a.pop(3))     # 1     # pop element at position 3
print(a)            # [17, 1, 2, 3, 13, 5]
a.remove(17)        # remove '17' from the list
print(a)            # [1, 2, 3, 13, 5]
a.reverse()         # reverse the order of the elements in the list
print(a)            # [5, 13, 3, 2, 1]
a.sort()            # sort the list
print(a)            # [1, 2, 3, 5, 13]
a.clear()           # remove all elements from the list
print(a)            # []


# extending
a = list('hello')       # makes a list from a string
print(a)                # ['h', 'e', 'l', 'l', 'o']
a.append(100)           # append 100, heterogeneous type
print(a)                # ['h', 'e', 'l', 'l', 'o', 100]
a.extend((1, 2, 3))     # extend using tuple
print(a)                # ['h', 'e', 'l', 'l', 'o', 100, 1, 2, 3]
a.extend('...')         # extend using string
print(a)            # ['h', 'e', 'l', 'l', 'o', 100, 1, 2, 3, '.', '.', '.']


# most common operations
a = [1, 3, 5, 7]
print(min(a))   # 1     # minimum value in the list
print(max(a))   # 7     # maximum value in the list
print(sum(a))   # 16    # sum of all values in the list
print(len(a))   # 4     # number of elements in the list
b = [6, 7, 8]
print(a + b)    # [1, 3, 5, 7, 6, 7, 8] # '+' with list means concatenation
print(a * 2)    # [1, 3, 5, 7, 1, 3, 5, 7]  # '*' has also a special meaning


# cool sorting
from operator import itemgetter
a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]
print(sorted(a))    # [(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
print(sorted(a, key=itemgetter(0)))
# [(1, 3), (1, 2), (2, -1), (4, 9), (5, 3)]
print(sorted(a, key=itemgetter(0, 1)))
# [(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
print(sorted(a, key=itemgetter(1)))
# [(2, -1), (1, 2), (5, 3), (1, 3), (4, 9)]
print(sorted(a, key=itemgetter(1), reverse=True))
# [(4, 9), (5, 3), (1, 3), (1, 2), (2, -1)]
