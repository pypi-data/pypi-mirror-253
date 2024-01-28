from pickle import dump,load
import os


def save_variable(v, filename):
    r"""
    data_file = r"character_name_data_file.py"  # 存储数据文件
    add_data = [1,2,3]  # 存储数据

    try:  # 第一次使用代码里的数据
        results = load_variable(data_file)
        if results == None:
            results = []
    except FileNotFoundError as e:    #
        print("数据为空,初始化为: []")
        results = []

    # 在程序最后面加上这句用于保存数据
    results +=add_data
    save_variable(results, data_file)
    print(results)

    """
    if os.path.exists(filename) == False:  # 文件不存在就新建
        with open(filename, 'w') as f:
            pass

    f = open(filename, 'wb')
    dump(v, f)
    f.close()
    return filename

def load_variable(filename):
    if os.path.getsize(filename) > 0:
        f = open(filename, 'rb')
        r = load(f)
        f.close()
        return r
    else:
        return



if __name__ == '__main__':
    r"""
    32位python的限制是 536870912 个元素。
    64位python的限制是 1152921504606846975 个元素
    """
    data_file = r"character_name_data_file.py"  # 存储数据文件
    add_data = [1,2,3]  # 存储数据

    try:  # 第一次使用代码里的数据
        results = load_variable(data_file)
        if results == None:
            results = []
    except FileNotFoundError as e:    #
        print("数据为空,初始化为: []")
        results = []

    # 在程序最后面加上这句用于保存数据
    results +=add_data
    save_variable(results, data_file)
    print(results)