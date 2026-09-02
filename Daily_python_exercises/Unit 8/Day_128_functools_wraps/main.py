from functools import wraps
import time


def time_taken_bad(function):
    def wrapper(*args, **kwargs):
        """Calculates the time that has took to do the function"""
        x = time.time()
        result = function(*args, **kwargs)
        print(f"It took {(time.time() - x)*1000} ms")
        return result
    return wrapper

@time_taken_bad
def multiply(a, b):
    """It multiplies a*b and returns the result"""
    return a*b


def time_taken_good(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        """Calculates the time that has took to do the function"""
        x = time.time()
        result = function(*args, **kwargs)
        print(f"It took {(time.time() - x)*1000} ms")
        return result
    return wrapper

@time_taken_good
def divide(a, b):
    """It divides a*b and returns the result"""
    return a/b

print(multiply.__name__)
print(multiply.__doc__)

print(divide.__name__)
print(divide.__doc__)


