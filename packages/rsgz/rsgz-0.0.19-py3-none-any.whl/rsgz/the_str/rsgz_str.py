import random

# 打印字符串的装饰器
def print_string(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)  # 打印第一个参数,即字符串
        return result
    return wrapper

# 返回新的 随机字符串
def rand_title(the_str,n):
    r"""
    返回新的 随机字符串
    the_str = r"Feature,Gorgeous,Fresh,Hot Sale,Simple,Fashion "
    new_title = rand_title(the_str, n=3) # Gorgeous Feature Simple
    """
    the_str = the_str.replace(" ,", ",").replace(", ", ",")
    the_str_list = the_str.split(",")  # ['Feature', 'Gorgeous', 'Fresh', 'Hot Sale', 'Simple', 'Fashion ']
    random.shuffle(the_str_list)
    the_str_list = the_str_list[0:n]
    the_str = ' '.join(the_str_list).title().replace("'S", "'s")
    return the_str.replace("  "," ")

# 将字符串转化为列表
def str_to_list(the_str):
    r"""
    将字符串转化为列表
    the_str = r"Feature,Gorgeous,Fresh"
    the_list = str_to_list(the_str)  # ['Feature', 'Gorgeous', 'Fresh']
    """
    return the_str.split(",")

# 列表转化为字符串
def list_to_str(the_list, fengefu):
    r"""
    fengefu = " "
    the_list = ["123", "aabb", "jiu_s12", "rsgz"]
    the_str = list_to_str(the_list, fengefu)  # 123 aabb jiu_s12 rsgz
    注意 列表里面不能有数字 如果有请转化为字符串格式
    """
    return fengefu.join(the_list)

# 字符串转化为字典
def str_to_dict1(str1):
    r"""
    字符串转化为字典
str1 = "HUAWEI,华为;MI,小米;OPPO,OPPO;VIVO,VIVO"
dict1 = str_to_dict1(str1)
print(dict1)
{'HUAWEI': '华为', 'MI': '小米', 'OPPO': 'OPPO', 'VIVO': 'VIVO'}
    """
    list1 = str1.split(";")
    dict_all = {}
    for i in list1:
        the_dict = "{'" + i.replace(",", "':'") + "'}"  # 拼接字典
        the_dict = eval(the_dict)
        dict_all.update(the_dict)
    return dict_all

# 字符串转化为字典2
def str_to_dict2(str1):
    r"""
    str1 = "HUAWEI,华为;MI,小米"
    dict1 = str_to_dict2(str1)
    print(dict1)  # {'HUAWEI': '华为', 'MI': '小米'}
    """
    dict_all = {}
    for i in [dict([tuple(i.split(","))]) for i in str1.split(";")]:
        dict_all.update(i)
    return dict_all

if __name__ == '__main__':
    pass