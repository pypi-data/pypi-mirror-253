

def start(重量列表, 成本, sku):
    print('sku:', sku)
    # 重量列表 = [0.151,0.151,0.161,0.17,0.186,0.182,0.199,0.209,0.218]
    print(len(重量列表))
    尺寸列表 = ["XS","S","M","L","XL","2XL","3XL","4XL","5XL","6XL"]
    # 成本=23
    利润=12
    国内运费=1.8
    折扣=0.5
    # point = 0.90 # 剩余点数  没免运
    point = 0.84 # 剩余点数  有免运
    # 8点佣金 2点手续费 6点免运


    r"""
    96.82-44.34-96.82*0.1=42.79
    """


    def xiapi(重量列表, 尺寸列表, 成本, 利润, point):
        一倍_list = []
        for i in range(len(重量列表)):
            重量 = float(重量列表[i]) * 1000+10
            藏价=(5+7*1.4+(重量-100)/10*0.9)/0.76
            全球商品价格 = 成本+国内运费+利润

            芒果价格 = (全球商品价格+藏价)/point*(1/(1-折扣))-藏价
            if i == 0:
                print(芒果价格-40)

            客户商品价格= (全球商品价格+藏价)/point

            # 一倍芒果价 = 客户商品价格 - 藏价-(1-point)*客户商品价格  # 客户商品价格 - 藏价- 0.1*客户商品价格
            # 一倍 = "{}-{}-(1-{})*{}=".format(format(客户商品价格, '.2f'), format(藏价, '.2f'), point, format(客户商品价格, '.2f'))

            藏价2 = (5+7*1.4+((float(重量列表[-1])*1000+10)-100)/10*0.9)/0.76
            藏价差 = 藏价2-藏价

            一倍芒果价 = 全球商品价格-藏价差
            一倍 = ''

            实际利润 = 客户商品价格*point-成本-国内运费-藏价
            利 = "{}*({})-{}-{}-{}={}".format(format(客户商品价格,'.2f'),point, 成本, 国内运费, format(藏价,'.2f'), format(实际利润,'.2f'))

            print("尺寸:", 尺寸列表[i], 重量列表[i], "2倍芒果价格:", format(芒果价格, '.2f'),"元","客户商品价格:", format(客户商品价格, '.2f'), "元=---->", format((客户商品价格*0.76), '.2f'), '巴西币', "藏价:", format(藏价, '.2f'), "元", "实际利润:", format(实际利润, '.2f'),'={}'.format(利), "一倍芒果价={}".format(一倍), format(一倍芒果价, '.2f'), 尺寸列表[i])
            一倍_list.append(format(一倍芒果价, '.2f'))
        return 一倍_list

    一倍_list = xiapi(重量列表, 尺寸列表, 成本, 利润, point)
    # print('\n尺寸列表', 尺寸列表)  # 尺寸
    # print('一倍_list', 一倍_list)  # 价格

    chi_price = dict(zip(尺寸列表, 一倍_list))
    print(float(重量列表[-1])+0.01)
    print(chi_price)  # 0.31

    # size_list = []
    # with open(r"tihuan.txt", 'r', encoding="utf-8") as f:
    #     for i in range(0,500):
    #         try:
    #             chi = f.readline().split('_')[-1].replace('\n', '').replace(' ', '')
    #             print(chi_price[chi])
    #         except:
    #             pass

重量列表 = [0.183,0.183,0.197,0.214,0.225,0.234,0.247,0.265,0.28,0.3]
成本 = 28
sku = 8130

start(重量列表, 成本, sku)
if len(重量列表)==9:
    print("XS, S, M, L, XL, 2XL, 3XL, 4XL, 5XL")