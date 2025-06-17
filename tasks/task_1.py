from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(map(str, args))
        kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        all_args = ",".join(filter(None, [args_str, kwargs_str]))
        print(f"Вызов: {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper
