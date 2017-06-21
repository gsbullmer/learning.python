from time import sleep, time


def f():
    sleep(.3)


def g():
    sleep(.5)


t = time()
f()
print('f took:', time() - t)   # f took: 0.30044984817504883

t = time()
g()
print('g took:', time() - t)   # g took: 0.5003244876861572
