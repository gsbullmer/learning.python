from functools import wraps


def max_results(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(
                    'Result is too big ({0}). Max allowed is {1}.'
                    .format(result, threshold))
            return result
        return wrapper
    return decorator


@max_results(75)
def cube(n):
    return n ** 3


@max_results(100)
def square(n):
    return n ** 2


@max_results(1000)
def multiply(a, b):
    return a * b


print(cube(5))
print(square(11))
print(multiply(50, 300))
