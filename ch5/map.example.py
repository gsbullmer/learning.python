print(map(lambda *a: a, range(3)))  # withough wraping in list...
# <map object at 0x000002B69B38D550>    # we get the iterator object
print(list(map(lambda *a: a, range(3))))    # wrapping in list...
# [(0,), (1,), (2,)]    # we get a list with its elements
print(list(map(lambda *a: a, range(3), 'abc')))     # 2 iterables
# [(0, 'a'), (1, 'b'), (2, 'c')]
print(list(map(lambda *a: a, range(3), 'abc', range(4, 7))))    # 3
# [(0, 'a', 4), (1, 'b', 5), (2, 'c', 6)]
# map stops as the shortest iterator
print(list(map(lambda *a: a, (), 'abc')))   # empty tuble is shortest
# []
print(list(map(lambda *a: a, (1, 2), 'abc')))   # (1, 2) shortest
# [(1, 'a'), (2, 'b')]
print(list(map(lambda *a: a, (1, 2, 3, 4), 'abc')))     # 'abc' shortest
# [(1, 'a'), (2, 'b'), (3, 'c')]
