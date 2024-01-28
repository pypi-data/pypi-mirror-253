from functools import wraps

def func_ru(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        module_name = func.__module__
        name = func.__name__
        print(f"执行 {module_name}.{name} 函数")
        return func(*args, **kwargs)
    return wrapper

def func_ru2(func):
    def vv(*args, **kwargs):
        print(f"执行{func.__name__} 函数!!!")
        return func(*args, **kwargs)
    return vv