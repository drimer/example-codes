from functools import wraps


def double_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_value = func(*args, **kwargs)
        try:
            return orig_value * 2
        except TypeError:
            return orig_value

    return wrapper
