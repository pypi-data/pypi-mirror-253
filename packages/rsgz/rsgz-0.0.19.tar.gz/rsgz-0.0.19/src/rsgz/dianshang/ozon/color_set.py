color_set = r"""red-->红色-->Красный
blue-->蓝色-->Голубой
green-->绿色-->Зеленый
pink-->粉红色-->розовый
grey-->灰色-->серый
cyan-->青色-->Cyan
brown-->棕色-->Коричневый
black-->黑色-->Черный
purple-->紫色-->Фиолетовый
yellow-->黄色-->Желтый"""

# 写法一
def color_set_replace(search_color):
    ret = ''
    l1 = color_set.split('\n')
    for l2 in l1:
        l3 = l2.split("-->")
        if search_color.lower()==l3[0]:
            ret=l3[2]
    return ret

# 英文列表转换成俄文列表
def color_list_search(color_list_eng):
    c_all=[]
    for c in color_list_eng:
        c_all.append(color_set_replace(search_color=c))
    return c_all

if __name__ == '__main__':
    # ret = color_set_replace(search_color="red")
    # print(ret)
    ret2 = color_list_search(color_list_eng=["red","yellow","black"])
    print(ret2)  # ['Красный', 'Желтый', 'Черный']