

r"""
下面是常见的列表操作 不想记住那些复杂的 自己自定义一个挺好记的
"""

# 函数作用域列表
def func_to_list(func, the_list):
    r"""
    函数作用于 列表中每个元素  返回新列表
    func=lambda x: 2 + 4 * x
    list1 = list(range(0, 18))
    the_list = func_to_list(func, list1)
    """
    new_list = list(map(func, the_list))
    return new_list

# 移除最后一个元素
def list_remove_last_element(the_list):
    r"""
    移除最后一个列表元素
    the_list = list(range(0, 3))
    the_list = list_remove_last_element(the_list)  # [0, 1]
    """
    the_list.pop()
    return the_list

# 移除第一个元素
def list_remove_first_element(the_list):
    r"""
    移除第一个列表元素
    the_list = list(range(0, 3))
    the_list = list_remove_first_element(the_list)  #[1, 2]
    """
    del the_list[0]
    return the_list

# 添加第一个元素
def list_add_first_element(the_list, ele):
    r"""
    列表开头 添加元素
    list1 = list(range(0, 3))
    new_list = list_add_first_element(list1,"帅气")  # ['帅气', 0, 1, 2]
    """
    the_list.insert(0, ele)
    return the_list

# 指定位置添加元素
def list_add_index_element(the_list, ele, index):
    r"""
    指定位置添加列表元素
    list1 = list(range(0, 3))
    new_list = list_add_index_element(list1,"帅气", 2)  # [0, 1, '帅气', 2]
    """
    the_list.insert(index, ele)
    return the_list

# 列表反序
def list_fanxu(the_list):
    r"""
    the_list = [0,2,5]
    new_list = list_fanxu(the_list)  # [5, 2, 0]
    """
    return the_list[::-1]

# 列表转化为字典
def list_to_dict(the_list):
    r"""
    the_list = ['迪迦', '荒天帝', '萧炎']
    print(list_to_dict(the_list)) # {1: '迪迦', 2: '荒天帝', 3: '萧炎'}
    """
    dict_new = enumerate(the_list, start=1)
    return dict(dict_new)

# 随机列表元素
def rand_list(the_list):
    r"""
    随机列表元素
    the_list = [1,2,3,4]
    print(rand_list(the_list))  # [2, 1, 3, 4]
    """
    import random

    random.shuffle(the_list)
    return the_list

# 列表去重
def quchong_list(the_list):
    r"""
    列表去重 位置不变
    the_list = ['a',1, 10, 'b', 1, 3, 9, 9, 'a']
    print(quchong_list(the_list))  # ['a', 1, 10, 'b', 3, 9]
    """

    dic = {}
    dic = dic.fromkeys(the_list).keys()
    return list(dic)

# 元素首字母大写
def daxie_shouzimu(the_list):
    new_list = list(map(lambda x:x.title(), the_list))
    return new_list

# 输出元素
def print_list(the_list, fenge=None):
    return '{}'.format(fenge).join(str(i) for i in the_list)

# 枚举数据
def meiju(str1):
    r"""
    枚举数据
    str1 = "a b c"
    meiju(str1)
    0 a
    1 b
    2 c
    """

    # iterable ="a b c".split(" ")
    iterable = str1.split(" ")
    for i, item in enumerate(iterable):
        print(i, item)

if __name__ == '__main__':
    the_list = ['a', 1, 10, 'b', 1, 3, 9, 9, 'a']
    print(quchong_list(the_list))  # ['a', 1, 10, 'b', 3, 9]