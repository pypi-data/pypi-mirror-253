from prettytable import PrettyTable


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

# 计算利润
def dv(商品成本价, 重量, 售价, 汇率):
    总运费, 顾客运费, 老板_跨境物流成本_藏价  = yunfei(重量=重量, 国家="巴西", 套餐="zone c")  # 巴西币
    总运费, 顾客运费, 老板_跨境物流成本_藏价 = 总运费 / 汇率, 顾客运费 / 汇率, 老板_跨境物流成本_藏价 / 汇率  # 人民币
    佣金费率, 活动服务费费率, 交易手续费费率, 提现手续费 = 0.08, 0.00, 0.02, 0.00
    利润 = 售价*(1-佣金费率-活动服务费费率-交易手续费费率-提现手续费)-商品成本价-老板_跨境物流成本_藏价
    return 利润

# 显示人民币定价
def RMB_price(weight):
    tb = PrettyTable(["原价[￥]", "利润[￥]",'全球价格[￥]'])
    lirun_2_4 = []
    lirun_12_14 = []

    for i in range(40, 200):
        商品成本价 = 22
        重量 = (weight+0.01)*1000
        汇率 = 0.76
        利润 = dv(商品成本价=商品成本价, 重量=重量, 售价=i, 汇率=汇率)
        if 2<利润<5:
            tb.add_row([i, format(利润, '.2f'), i*2])
            lirun_2_4.append(i*2)

        if 12<利润<16:
            tb.add_row([i, format(利润, '.2f'), i * 2])
            lirun_12_14.append(i*2)

    print(tb)
    dijia = lirun_2_4[0]  # [124, 126, 128] 124
    normal_price = lirun_12_14[0] # [146, 148, 150, 152] 146