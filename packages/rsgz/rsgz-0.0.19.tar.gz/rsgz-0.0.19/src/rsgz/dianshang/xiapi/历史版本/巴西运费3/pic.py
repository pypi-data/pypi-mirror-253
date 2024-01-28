from rsgz.tupian.normal import *
from rsgz.file.files import get_files, get_base_name

pic_base_dir = r"\\R1\王哥0801\已出货1011\P好未传\P已出货8284未传"
pintu = os.path.join(str(pic_base_dir), '1pintu')  # 拼图  \\R1\王哥0801\已出货1011\已传\已出货8304\8304\1pintu
show_img = os.path.join(str(pic_base_dir), '2show-img')  # 展示图   有背景单图组合图
attribute_pic = os.path.join(str(pic_base_dir), '3attribute-pic')  # 属性图  有背景单张图

remove_str = ['0','1','2','3','4','5','6','7','8','9','(',')','（','）','_','-']
remove_pic_str(pintu, *remove_str)
remove_pic_str(show_img, *remove_str)
remove_pic_str(attribute_pic, *remove_str)

r"""
['black4.jpg']
['black5.jpg', 'blue5.jpg', 'grey5.jpg', 'pink5.jpg', 'rose5.jpg']
['black1.jpg', 'blue1.jpg', 'grey1.jpg', 'pink1.jpg', 'rose1.jpg']
--->
['black.jpg']
['black.jpg', 'blue.jpg', 'grey.jpg', 'pink.jpg', 'rose.jpg']
['black.jpg', 'blue.jpg', 'grey.jpg', 'pink.jpg', 'rose.jpg']
"""

pintu_pic_list = get_files(pintu)  # ['black.jpg']
show_img_pic_list = get_files(show_img)  # ['black.jpg', 'blue.jpg', 'grey.jpg', 'pink.jpg', 'rose.jpg']
attribute_pic_pic_list = get_files(attribute_pic)  # ['black.jpg', 'blue.jpg', 'grey.jpg', 'pink.jpg', 'rose.jpg']

get_base_name(pintu_pic_list) #  ['black.jpg']
get_base_name(show_img_pic_list)  # ['black.jpg', 'blue.jpg', 'grey.jpg', 'pink.jpg', 'rose.jpg']
get_base_name(attribute_pic_pic_list)  # ['black.jpg', 'blue.jpg', 'grey.jpg', 'pink.jpg', 'rose.jpg']

color_pic = get_base_name(attribute_pic_pic_list)  # ['black.jpg', 'blue.jpg', 'grey.jpg', 'pink.jpg', 'rose.jpg']
color_list = list(map(lambda x:x.replace('.jpg','').replace('.jpeg','').replace('.png','').title(), color_pic))  # ['Black', 'Blue', 'Grey', 'Pink', 'Rose']

if __name__ == '__main__':
    print(color_pic)
    print(color_list)