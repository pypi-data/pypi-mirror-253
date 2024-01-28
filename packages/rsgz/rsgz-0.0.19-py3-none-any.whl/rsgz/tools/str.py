
# 打印字符串的装饰器
def print_string(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)  # 打印第一个参数,即字符串
        return result
    return wrapper