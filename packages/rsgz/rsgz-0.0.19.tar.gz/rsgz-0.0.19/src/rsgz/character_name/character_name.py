from rsgz.the_data.data import save_variable, load_variable




def zhuijia_name(name):
    r"""
    name = "萧天 林琅天"
    zhuijia_name(name)
    """
    # data_file = r"character_name_data_file.txt"
    data_file = r"character_name_data_file.py"
    try:  # 从第二次开始则读取txt数据
        results = load_variable(data_file)

        if results == None:
            results = []
    except FileNotFoundError as e:  # 第一次使用代码里的数据
        print("数据为空,初始化为: []")
        results = []

    # 在程序最后面加上这句用于保存数据
    # results ={'name': 'rsgz'}
    character_name_list = []
    character_name_list = results + name.split(" ")
    save_variable(character_name_list, data_file)
    print(character_name_list)

if __name__ == '__main__':
    name = "尸骸仙帝 药老"
    zhuijia_name(name)