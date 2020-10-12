from functools import wraps
from threading import RLock


def singlethon(cls):
    instance = {}
    locker = RLock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instance:
            with locker:
                if cls not in instance:
                    instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapper()
