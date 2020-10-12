from functools import wraps
from time import time


class Record():
    def __init__(self, output):
        self.output = output

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            self.output(func.__name__, time() - start)
            return result

        return wrapper()
