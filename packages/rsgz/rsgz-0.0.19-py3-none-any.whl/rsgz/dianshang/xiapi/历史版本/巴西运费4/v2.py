from prettytable import PrettyTable
from settings import fu_sku, weight_list, size_list, color_list,base_path,商品成本价



# 巴西境外运费
def yunfei(重量=None, 国家="巴西", 套餐="zone c"):
    shipping_cost=guke_yunfei=laoban_yunfei=''
    if 国家 == "巴西" and 套餐 == "zone c":
        if 重量 < 30:
            shipping_cost = 25
            guke_yunfei = 20
            laoban_yunfei = 5

        elif 30 <= 重量 < 100:
            increment = (重量 - 30) / 10
            shipping_cost = 25 + increment * 1.4
            guke_yunfei = 20
            laoban_yunfei = 5 + increment * 1.4

        elif 重量 > 100:
            increment = (重量 - 100) / 10
            shipping_cost = 25 + 7 * 1.4 + increment * 0.9
            guke_yunfei = 20
            laoban_yunfei = 5 + 7 * 1.4 + increment * 0.9

    return shipping_cost, guke_yunfei, laoban_yunfei


# 显示人民币定价
def RMB_price(weight):
    tb = PrettyTable(["原价[￥]", "利润[￥]",'全球价格[￥]'])
    lirun_2_4 = []
    lirun_12_14 = []

    for i in range(0, 200):
        售价 = i
        # 重量 = (weight+0.01)*1000  # 这里自动加了10g
        # 汇率 = 0.76
        利润 = 售价 - 商品成本价 - 1.8

        if 1.8<利润<5:
            tb.add_row([i, format(利润, '.2f'), i*2])
            lirun_2_4.append(i)

        if 11.8<利润<16:
            tb.add_row([i, format(利润, '.2f'), i * 2])
            lirun_12_14.append(i)

    print(tb)
    dijia = lirun_2_4[0]  # [124, 126, 128] 124
    normal_price = lirun_12_14[0] # [146, 148, 150, 152] 146

    return dijia, normal_price

# 计算最终重量列表
def calculation_weight_list(weight_list):
    r"""
    计算最终重量列表
    传进原始的重量列表参数 因为需要两个作为一组 对重量进行分阶

    """

    print('weight_list:', weight_list)
    the_weight_list = [float(i) for i in weight_list]
    print('the_weight_list:',the_weight_list)  # [0.18, 0.187, 0.186, 0.207, 0.223, 0.232, 0.269, 0.268, 0.283]

    new_weight_list = []
    for i in range(len(the_weight_list)):
        if i%2!=0:  # 2个重量为一组 分阶
            new_weight_list.append(the_weight_list[i])
    print('偶数位重量:',new_weight_list)  # [0.187, 0.207, 0.232, 0.268]
    if len(the_weight_list)%2!=0:  # 重量数量 是奇数位
        new_weight_list.append(the_weight_list[-1])
    print('最终重量列表', new_weight_list)
    return new_weight_list

# 列表划分价格阶梯
def jieti_price(weight_list):
    r"""
    参数：阶梯重量
    返回：阶梯价格  有高价和低价
    """
    new_weight_list = calculation_weight_list(weight_list)
    dijia_list, normal_price_list = [], []
    for i in new_weight_list:
        dijia, normal_price = RMB_price(weight=i)
        dijia_list.append(dijia)
        normal_price_list.append(normal_price)

    return dijia_list, normal_price_list

# 输出尺寸-价格 映射
def size_price(size_list, dijia_list, normal_price_list):
    try:
        print("{}-{}-->{}-{}".format(size_list[0],size_list[1],dijia_list[0], normal_price_list[0]))
    except:
        pass
    try:
        print("{}-{}-->{}".format(size_list[2],size_list[3],normal_price_list[1]))
    except:
        pass
    try:
        print("{}-{}-->{}".format(size_list[4],size_list[5],normal_price_list[2]))
    except:
        pass
    try:
        print("{}-{}-->{}".format(size_list[6],size_list[7],normal_price_list[3]))
    except:
        pass
    try:
        print("{}-->{}".format(size_list[8],normal_price_list[4]))
    except:
        pass

dijia_list, normal_price_list = jieti_price(weight_list)
print('低价列表:',dijia_list)
print('高价列表', normal_price_list)


print("尺寸", end=':')
for i in size_list:
    print(i, end=',')

print("\n颜色", end=':')
for i in color_list:
    print(i, end=',')

if len(size_list)*len(color_list)>50:
    print("\n子sku 大于50")

print('\n父sku:',fu_sku)
print("价格设置:")
size_price(size_list, dijia_list, normal_price_list)

last_weight = 0
try:
    if str(weight_list[-1]+0.01)[4]!='0':
        # print('0000')
        # print(str(weight_list[-1]+0.01)[0:4])
        # print(float(str(weight_list[-1]+0.01)[0:4]))
        last_weight = float(str(weight_list[-1]+0.01)[0:4])+0.01
except:
    pass

print("克重:", weight_list[-1],'+10g=', weight_list[-1]+0.01,'+10g=', last_weight)


r"""
\\R1\王哥0801\已出货1011\已传\已到货8282
mkdir xxx\1pintu xxx\2show-img xxx\3attribute-pic
Beach Casual Bikini Charming Role Play Costume New Style Summer
"""