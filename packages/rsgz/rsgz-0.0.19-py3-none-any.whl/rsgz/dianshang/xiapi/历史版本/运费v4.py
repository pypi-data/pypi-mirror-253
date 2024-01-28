

# 转换成外币
def china_to_baxi(renminbi, huilv=0.7575):
    # 1人民币=0.7575巴西雷亚尔
    return renminbi*huilv

# 外币转换成国内币
def waibi_to_china(waibi, huilv=0.7575):
    return waibi/huilv

# 巴西运费
def baxi_yunfei(国家, 套餐, 重量):
    r"""
    返回运费
    """

    shipping_cost = ''  # 运费

    if 国家 == "巴西" and 套餐 == "zone a":
        if 重量<30:
            shipping_cost = 20

        elif 30<=重量<100:
            increment = (重量-30)/10
            shipping_cost = 20 + increment * 1.4

        elif 重量>100:
            increment = (重量-100)/10
            shipping_cost = 20 + 7*1.4+ increment * 0.9

    if 国家 == "巴西" and 套餐 == "zone b":
        if 重量<30:
            shipping_cost = 23

        elif 30<=重量<100:
            increment = (重量-30)/10
            shipping_cost = 23 + increment * 1.4

        elif 重量>100:
            increment = (重量-100)/10
            shipping_cost = 23 + 7*1.4+ increment * 0.9

    if 国家 == "巴西" and 套餐 == "zone c":
        if 重量<30:
            shipping_cost = 25

        elif 30<=重量<100:
            increment = (重量-30)/10
            shipping_cost = 25 + increment * 1.4

        elif 重量>100:
            increment = (重量-100)/10
            shipping_cost = 25 + 7*1.4+ increment * 0.9

    # print("运费:{}巴西币".format(shipping_cost))
    return shipping_cost

# 折前售价          提现手续费没算
def shoujia(国家, 套餐, 汇率, 成本, 利润, 境内运费, 重量, 佣金费率,交易手续费,活动服务费=None):
    r"""
    返回原价格
    """
    国外运费_BRL = baxi_yunfei(国家, 套餐, 重量)
    国外运费_CNY = waibi_to_china(waibi=国外运费_BRL, huilv=汇率)

    # print("国外运费_CNY",国外运费_CNY)
    # print("境内运费", 境内运费)
    try:
        if 活动服务费!=None:
            总运费 = 国外运费_CNY + 境内运费  # 人民币
            print("总运费=国外运费_CNY+境内运费={}+{}={}".format(国外运费_CNY,境内运费,总运费) )

            原价格 = (成本+利润+总运费)*(1+佣金费率+交易手续费+活动服务费)
            print("原价格=(成本+利润+总运费)*(1+佣金费率+交易手续费+活动服务费)="
                  "({}+{}+{})*(1+{}+{}+{})={}".format(成本, 利润, 总运费, 佣金费率, 交易手续费, 活动服务费, 原价格))
            print("1", 48.68+12.8 +35.8+77.55) # 174.82
            print("2", 174-155)  # 19
            print("3", 110.02*0.1658)  # 18.24131
            print('4 订单收入=', 72.38 - 国外运费_CNY - 72.38*0.16)
            return 原价格
        else:
            总运费 = 国外运费_CNY + 境内运费  # 人民币
            原价格 = (成本 + 利润 + 总运费) * (1 + 佣金费率 + 交易手续费)
            return 原价格
    except:
        print("出错了")


if __name__ == '__main__':
    父sku = 8279
    成本 = 22
    重量 = 180
    汇率 = 0.76
    利润 = 12
    折扣 = 0.5
    境内运费 = 1.8
    佣金费率 = 0.08
    交易手续费 = 0.02
    活动服务费 = 0.06
    国家 = "巴西"
    套餐 = "zone a"

    shipping_cost1_BRL = baxi_yunfei(国家="巴西", 套餐="zone a", 重量=重量)  # 巴西币
    shipping_cost2_BRL = baxi_yunfei(国家="巴西", 套餐="zone b", 重量=重量)
    shipping_cost3_BRL = baxi_yunfei(国家="巴西", 套餐="zone c", 重量=重量)

    shipping_cost1_CNY = waibi_to_china(shipping_cost1_BRL, huilv=0.7575)
    shipping_cost2_CNY = waibi_to_china(shipping_cost2_BRL, huilv=0.7575)
    shipping_cost3_CNY = waibi_to_china(shipping_cost3_BRL, huilv=0.7575)

    # 1*0.1
    print("zone a运费:{}巴西币  {}人民币".format(shipping_cost1_BRL, shipping_cost1_CNY))
    print("zone b运费:{}巴西币  {}人民币".format(shipping_cost2_BRL, shipping_cost2_CNY))
    print("zone c运费:{}巴西币  {}人民币".format(shipping_cost3_BRL, shipping_cost3_CNY))

    原价 = shoujia(国家=国家, 套餐=套餐, 汇率=汇率,
                 成本=成本, 利润=利润, 境内运费=境内运费, 重量=重量,
                 佣金费率=佣金费率, 交易手续费=交易手续费, 活动服务费=活动服务费)
    print(原价)

r"""
这版本直接除尽  但是总的计算结果和官方有问题 运费是对的
"""