from pic import print_color_name
import os,re,pyperclip,random

huilv = 1.5984  # 1马来西亚林吉特=1.5984人民币

def start(重量列表, 成本, sku, 利润, point, 尺寸列表):
    print(sku, '      <---sku')
    # 重量列表 = [0.151,0.151,0.161,0.17,0.186,0.182,0.199,0.209,0.218]
    print(len(重量列表), '      <---重量数量')
    # 尺寸列表 = ["XS","S","M","L","XL","2XL","3XL","4XL","5XL","6XL"]
    # 成本=23
    # 利润=12
    # 利润=12
    国内运费=2
    折扣=0.5
    # point = 0.90 # 剩余点数  没免运
    # point = 0.84 # 剩余点数  有免运
    # 8点佣金 2点手续费 6点免运


    r"""
    96.82-44.34-96.82*0.1=42.79
    """
    kehuduan_list = []

    def xiapi(重量列表, 尺寸列表, 成本, 利润, point):
        一倍_list = []
        for i in range(len(重量列表)):
            重量 = float(重量列表[i]) * 1000+10
            藏价=(重量/10*0.15)*huilv  # 人民币
            全球商品价格 = 成本+国内运费+利润

            芒果价格 = (全球商品价格+藏价)/point*(1/(1-折扣))-藏价
            if i == 0:
                print(芒果价格-40)


            客户商品价格= (全球商品价格+藏价)/point  # 这个相当于客户端价格等于  全球价格+藏价  最后除以去除所有费用之外的点数
            kehuduan_list.append(format(客户商品价格/huilv+random.random()/3, '.2f'))  # 马来西亚币

            # 一倍芒果价 = 客户商品价格 - 藏价-(1-point)*客户商品价格  # 客户商品价格 - 藏价- 0.1*客户商品价格
            # 一倍 = "{}-{}-(1-{})*{}=".format(format(客户商品价格, '.2f'), format(藏价, '.2f'), point, format(客户商品价格, '.2f'))

            藏价2 = (float(重量列表[-1])/10*0.15)*huilv  # 人民币
            藏价差 = 藏价2-藏价

            一倍芒果价 = 全球商品价格-藏价差
            一倍 = ''

            实际利润 = 客户商品价格*point-成本-国内运费-藏价
            利 = "{}*({})-{}-{}-{}={}".format(format(客户商品价格,'.2f'),point, 成本, 国内运费, format(藏价,'.2f'), format(实际利润,'.2f'))

            if i==0:
                print("尺寸:", 尺寸列表[i], 重量列表[i], "2倍芒果价格:", format(芒果价格-40, '.2f'), "元", "客户商品价格:", format(客户商品价格, '.2f'), "元=---->", format((客户商品价格 / huilv), '.2f'), '马来西亚币', "藏价:", format(藏价, '.2f'), "元", "实际利润:", format(实际利润, '.2f'), '={}'.format(利), "一倍芒果价={}".format(一倍), format(一倍芒果价/2, '.2f'), 尺寸列表[i])
            else:
                print("尺寸:", 尺寸列表[i], 重量列表[i], "2倍芒果价格:", format(芒果价格, '.2f'),"元","客户商品价格:", format(客户商品价格, '.2f'), "元=---->", format((客户商品价格 / huilv), '.2f'), '马来西亚币', "藏价:", format(藏价, '.2f'), "元", "实际利润:", format(实际利润, '.2f'),'={}'.format(利), "一倍芒果价={}".format(一倍), format(一倍芒果价, '.2f'), 尺寸列表[i])
            一倍_list.append(format(一倍芒果价, '.2f'))

        price_arr = kehuduan_list
        shou_price = format(float(kehuduan_list[-1])/2+random.random()/3, '.2f')
        print("马来西亚币 价格列表:")
        print("price_arr =", price_arr)
        print("shou_price={}\n 尺寸{}个".format(shou_price,len(kehuduan_list)))
        return 一倍_list, price_arr, shou_price

    一倍_list, price_arr, shou_price = xiapi(重量列表, 尺寸列表, 成本, 利润, point)

    chi_price = dict(zip(尺寸列表, 一倍_list))
    print(float(重量列表[-1])+0.01)
    print(chi_price)  # 0.31

    return price_arr, shou_price


def new_weights(weight):
    new_weight = weight.split('\n')
    for i in new_weight:
        if i == '':
            new_weight.remove(i)

    print(['0001 ', '0002 ', '0003 ', '0004 ', '0005 ', '0006', '0007 ', '0008 ', '0009 ', '0010 '])
    print(new_weight)
    return new_weight


# point = 0.90 # 剩余点数  没免运
shouxufei = 0.0742*(1+0.06)+0.0212*(1+0.06)+0.053
point = 1-shouxufei # 剩余点数  有免运
尺寸列表 = ["XS","S","M","L","XL","2XL","3XL","4XL","5XL","6XL"]
# 尺寸列表 = ["XS","S","M","L","XL","2XL","3XL","4XL","5XL"]
# 尺寸列表 = ["S","M","L","XL","2XL","3XL","4XL","5XL"]




dir_path = r"\\R1\r1\新泳衣\泳衣老款\2010\2010"
利润 = 12
成本 = 25
weight = r"""
0.14
0.14
0.145
0.15
0.155
0.164
0.174
0.184
0.191
0.198
"""


重量列表 = new_weights(weight)

print(dir_path)
if len(重量列表)==9:
    print("XS, S, M, L, XL, 2XL, 3XL, 4XL, 5XL")

print_color_name(dir_path)
sku = re.findall(r"\d+",dir_path.split(os.sep)[-1])[0]

price_arr, shou_price = start(重量列表, 成本, sku, 利润, point,尺寸列表)


copy_str = r"""
// size_arr = ['XS','S','M','L','XL','2XL','3XL','4XL','5XL','6XL']
size_num = document.getElementsByClassName("variation-edit-item")[1].getElementsByClassName("option-container")[0].getElementsByClassName("options-item drag-item").length
var size_arr = new Array(size_num);

num = document.getElementsByClassName("variation-edit-item")[0].getElementsByClassName("option-container")[0].getElementsByClassName("options-item drag-item").length
var yanse_arr = new Array(num);
console.log("颜色:", yanse_arr.length,"种")
console.log("尺寸:", size_arr.length,"种")

price_arr = {}
shou_price = {}

// 价格
for(var yanse_i =1;yanse_i<=yanse_arr.length;yanse_i++){{
    size_arr_web = []
    price_arr_web = []
    for(var size_i =1;size_i<=size_arr.length;size_i++){{
        tou = '/html/body/div[1]/div[2]/div/div/div/div/div/div[1]/section[3]/div/div[2]/div/div[1]/div[3]/div[2]/div[1]'

        // 尺寸
        size_xpath = tou+'/div[1]/div[2]/div['+String(yanse_i)+']/div[2]/div['+String(size_i)+']/div'
        size = $x(size_xpath)[0].innerText
        size_arr_web.push(size)

        // 价格
        //                 /div[2]/div/div[2]/div[1]/div[2]/div['+String(yanse_i)+']/div/div['+String(size_i)+']/div[1]/div/div/div/div/div/div/input
        price_xpath = tou+'/div[2]/div/div[2]/div[1]/div[2]/div['+String(yanse_i)+']/div/div['+String(size_i)+']/div[1]/div/div/div/div/div/div/input'
        el=$x(price_xpath)[0]
        el.value=price_arr[size_i-1]
        var event = document.createEvent('HTMLEvents');
        event.initEvent("input", true, true);
        event.eventType = 'message';
        el.dispatchEvent(event);

        price = $x(price_xpath)[0].value
        price_arr_web.push(price)
    }}
    console.log(size_arr_web)
    console.log(price_arr_web)
}}

shou_xpath = '/html/body/div[1]/div[2]/div/div/div/div/div/div[1]/section[3]/div/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/input'
el=$x(shou_xpath)[0]
el.value=shou_price
var event = document.createEvent('HTMLEvents');
event.initEvent("input", true, true);
event.eventType = 'message';
el.dispatchEvent(event);
""".format(price_arr, shou_price)

pyperclip.copy(copy_str)