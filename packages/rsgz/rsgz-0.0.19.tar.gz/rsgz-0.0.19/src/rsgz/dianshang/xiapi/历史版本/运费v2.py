from forex_python.converter import CurrencyRates


r"""
pip install forex-python -i https://pypi.tuna.tsinghua.edu.cn/simple 
"""


# def money_converter(from_currency, to_currency, amount):
#     r"""
#     美元:USD
#     人民币:CNY
#     欧元:EUR
#     日元:JPY
#     巴西币:BRL
#     马来西亚:MYR
#
#     巴西币
#     money_converter(from_currency='BRL', to_currency='CNY', amount=xxx)
#     money_converter(from_currency='CNY', to_currency='BRL', amount=xxx)
#
#     马来币
#     money_converter(from_currency='MYR', to_currency='CNY', amount=xxx)
#     money_converter(from_currency='CNY', to_currency='MYR', amount=xxx)
#     """
#     c = CurrencyRates()
#     result = c.convert(from_currency, to_currency, amount)
#     # c.convert()
#     return result


def china_to_baxi(renminbi, huilv=0.7575):
    # 1人民币=0.7575巴西雷亚尔
    return renminbi*huilv

def waibi_to_china(waibi, huilv=0.7575):
    return waibi/huilv


def baxi(国家, 套餐, 重量):
    r"""
    返回运费
    """

    shipping_cost = ''  # 运费

    def quzheng(weight, weight_unit):
        r"""
        用来对续重重量取整
        weight = 180
        weight_unit=10     通常这个是单位重量
        quzheng(weight, weight_unit)  # 18
        """
        if weight%weight_unit==0:
            return int(weight / weight_unit)
        else:
            return int(weight // weight_unit)+1

    if 国家 == "巴西" and 套餐 == "zone a":
        if 重量<30:
            shipping_cost = 20
        elif 30<=重量<100:
            increment = quzheng(weight=重量, weight_unit=10)
            shipping_cost = 20 + increment * 1.4
        elif 重量>100:
            increment = quzheng(weight=重量, weight_unit=10)
            shipping_cost = 20 + increment * 0.9

    if 国家 == "巴西" and 套餐 == "zone b":
        if 重量 < 30:
            shipping_cost = 23
        elif 30 <= 重量 < 100:
            increment = quzheng(weight=重量, weight_unit=10)
            shipping_cost = 23 + increment * 1.4
        elif 重量 > 100:
            increment = quzheng(weight=重量, weight_unit=10)
            shipping_cost = 23 + increment * 0.9

    if 国家 == "巴西" and 套餐 == "zone c":
        if 重量 < 30:
            shipping_cost = 25
        elif 30 <= 重量 < 100:
            increment = quzheng(weight=重量, weight_unit=10)
            shipping_cost = 25 + increment * 1.4
        elif 重量 > 100:
            increment = quzheng(weight=重量, weight_unit=10)
            shipping_cost = 25 + increment * 0.9

    # print("运费:{}巴西币".format(shipping_cost))
    return shipping_cost

if __name__ == '__main__':
    父sku = 8279
    成本 = 22

    汇率 = 0.76
    利润 = 12
    折扣 = 0.5
    境内运费 = 1.8
    佣金费率 = 0.08
    交易手续费 = 0.02
    活动服务费 = 0.06
    国家 = "巴西"
    套餐 = "zone a"

    shipping_cost1_BRL = baxi(国家="巴西", 套餐="zone a", 重量=180)  # 巴西币
    shipping_cost2_BRL = baxi(国家="巴西", 套餐="zone b", 重量=180)
    shipping_cost3_BRL = baxi(国家="巴西", 套餐="zone c", 重量=180)

    shipping_cost1_CNY = waibi_to_china(shipping_cost1_BRL, huilv=0.7575)
    shipping_cost2_CNY = waibi_to_china(shipping_cost2_BRL, huilv=0.7575)
    shipping_cost3_CNY = waibi_to_china(shipping_cost3_BRL, huilv=0.7575)

    # 1*0.1
    print("zone a运费:{}巴西币  {}人民币".format(shipping_cost1_BRL, shipping_cost1_CNY))
    print("zone b运费:{}巴西币  {}人民币".format(shipping_cost2_BRL, shipping_cost2_CNY))
    print("zone c运费:{}巴西币  {}人民币".format(shipping_cost3_BRL, shipping_cost3_CNY))