from functools import wraps
from time import time


def record(output):
    """可以参数化的装饰器"""

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            output(func.__name__, time() - start)
            return result

        return wrapper()

    return decorate



