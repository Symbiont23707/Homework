
def call_once(func):
    """decorator which runs a function or method once and caches the result"""
    cache = None
    def wrapper(*args):
        nonlocal cache
        if cache is not None:
            result = cache
        else:
            result = func(*args)
            cache = result
        return result
    return wrapper

@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))
print(sum_of_numbers(999, 100))
print(sum_of_numbers(134, 412))
print(sum_of_numbers(856, 232))