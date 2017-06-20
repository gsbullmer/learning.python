cubes = [k**3 for k in range(10)]   # a regular list
print(cubes)
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
print(type(cubes))
# <class 'list'>
cubes_gen = (k**3 for k in range(10))   # create as generator
print(cubes_gen)
# <generator object <genexpr> at 0x000001B856DF9518>
print(type(cubes_gen))
# <class 'generator'>
print(list(cubes_gen))
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
print(list(cubes_gen))
# []
