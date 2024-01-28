import pic
from rsgz.mulu.dirs import mkdir

base_path = r"\\R1\王哥0801\已出货1011\P好未传\P已出货8287未传"
fu_sku = 8287
商品成本价 = 31

v1 = r"xxx\1pintu"
v2 = r"xxx\2show-img"
v3 = r"xxx\3attribute-pic"
try:
    mkdir(base_path, v1)
    mkdir(base_path, v2)
    mkdir(base_path, v3)
except:
    pass

# 重量列表
weight_list =[
0.198,
0.209,
0.219,
0.242,
0.256,
0.260,
0.273,
0.287,
0.303
]

# 尺寸列表
size_list =['S','M','L','XL','2XL','3XL','4XL','5XL','6XL']

# 颜色列表  自动获取
color_list = pic.color_list

if __name__ == '__main__':
    print('weight_list:',weight_list)
