from zhujie import zhujie
from json_table import json_table
from url_creat import url_creat_yongyi
from url import g
from rsgz.mulu.dirs import get_dirs_yiceng
import os
from color_set import color_list_search
from rsgz.file.files import get_files



def list_to_n_bei(the_list, n):
    matrix=[[l,]*n for l in the_list]
    return sum(matrix,[])

def get_zhutu_url_list(pic_l):
    r"""
    pic_l  几个颜色 目录里面的 图片列表
    """
    p_all = []
    for color_list in pic_l:
        pic_url_l = ''
        for pic in color_list:
            pic_url = ali_head + '/'.join(pic.split(os.sep)[-2:])
            pic_url_l = pic_url_l+pic_url
        p_all.append(pic_url_l)

    return p_all

xlsx=r"C:\Users\Administrator\Desktop\001.xlsx"
load_excel = xlsx
sku = '1932'  # 这个是唯一的
sku_true = '1932'  # 这个是变体的  大部分两个相等
ali_head = r"https://rsgz001.oss-cn-shenzhen.aliyuncs.com/mangguo/yongyi/{}/".format(sku)
fupath = r"C:\Users\Administrator\Desktop\工作记录\泳衣\{}".format(sku)
color_list = 'blue,grey,red,yellow'.split(',')   # 8357d_Blue_S
size_list = "XS,S,M,L,XL,2XL,3XL,4XL,5XL,6XL".split(",")
sku_l = [(sku+"_"+color_list[i]+"_"+size_list[j]) for i in range(len(color_list)) for j in range(len(size_list))]
# https://rsgz001.oss-cn-shenzhen.aliyuncs.com/mangguo/yongyi/8258/video/blue.mp4
video_url_list = sum([[j]*len(size_list) for j in [(ali_head+r"1video/"+i+".mp4") for i in color_list]], [])
fengmian_url = sum([[j]*len(size_list) for j in [(ali_head+i+"/1.png") for i in color_list]], [])
pic_l = [get_files(i) for i in get_dirs_yiceng(fupath) if "原图" not in i and "video" not in i]  # 这是本地地址  # 列出四个目录 blue green yellow的图片地址
pic_len_l = [len(i) for i in pic_l]  # 几个图片目录 图片数量 [ 7 7 7 7]
pic_fu_l =list_to_n_bei(the_list=get_zhutu_url_list(pic_l), n=len(size_list))  # https://rsgz001.oss-cn-shenzhen.aliyuncs.com/mangguo/yongyi/1932/blue/1.png
title = "Женские повседневные пляжные купальники"
ke = 0.322
chengben = 29
yongjin1 = 1.35  # 15 俄罗斯卢布 ≈ 1.3470 人民币   Ozon 对每个签收妥投的货物向卖家收取15卢布的佣金  # 销售佣金12%  卖家配送佣金8.9 左右就是100卢布
guahaofei = 13.5
wuliu = guahaofei + 76.5*(ke+0.01)
lirun = 20
price = '%.2f' % ((chengben+lirun+yongjin1+wuliu)*(1+0.11)*0.1449)  # 美元
print("售价:{}元--{}卢布--{}美元".format('%.2f' % (float(price)/0.1449), ('%.2f' % (float(price)/0.1449/0.0897)), price))
price_pre = '%.2f' % (float(price)/0.6)  # 美元  打6折
print("原价格{}元--{}卢布--{}美元, ".format('%.2f' % (float(price_pre)/0.1449), ('%.2f' % (float(price_pre)/0.1449/0.0897)), price_pre))
tax = "不征税"  #
type1 = "运动泳衣分开"  # 商用型
package_weight = "320"  # 包裹重量 g
package_width = "100"  # 宽度
package_height = "50"  # 高度
package_length = "100"  # 长度
# main_photo = url_creat(lei)
main_photo1 = g(r"https://rsgz001.oss-cn-shenzhen.aliyuncs.com/mangguo/yongyi/{}/1.jpg".format(sku_true), l=color_list)
main_photo2 = list_to_n_bei(the_list=main_photo1, n=len(size_list))
other_photo = pic_fu_l
brand = "无品牌"
card = sku  # 卡片
product_color1 = "黑"  # 商品颜色  这个颜色不起作用
size1_l = "40,42,44,46,50,52,54,56,58,60".split(',')  # 俄罗斯尺码
size2_l = "XS[40-42](77-82cm),S[42-44](87-92cm),M[44-46](92-97cm),L[46-50](97-102cm),XL[50-52](102-107cm),2XL[52-54](107-112cm),3XL[54-56](112-117cm),4XL[56-58](117-122cm),5XL[58-60](122-127cm),6XL[60-62](127-132cm)".split(',') # 制造商尺码
product_color2_l_e_wen = color_list_search(color_list_eng=color_list)  # 颜色名称
product_color2_l_e_wen2 = list_to_n_bei(the_list=product_color2_l_e_wen, n=len(size_list))
type2 = "独立泳衣 "  # 泳衣类型
gender = "女性"  # 性别
key_words = r"С высокой талией,Купальники раздельные женские белые,С шортиками,Купальники раздельные женские розовые,Коричневый,Недорогие,Купальники раздельные женские прозрачные,Купальники раздельные женские желтые,Купальники раздельные женские зеленые,Купальники раздельные женские синие"  # 关键字
TargetAudience ="成人"  # 目标受众
season = "适合任何季节"  # 季节
model_height = "170 厘米"  # 模特身高
model_measurements = "ОГ - 90, ОТ - 65, ОБ - 95"  # 模特三围
cloth_size = "52"  # 展示图 服装尺寸
collect = "2023春夏"  # 收集
country_of_manufacture = "中国"  # 制造国
print_type = "花卉"  # 印花种类
comments = zhujie  # 注解
care_instructions = "Стирка при температуре не выше 39 градусов, ручная стирка.Не сушите купальный костюм в сушилке, он может деформироваться."  # 保养说明
material = "涤纶"  # 材料
material_ingredient = "Нейлон 20% полиэстер 80%"  # 材料成分
gasket_inner_material = "聚酯纤维"  # 垫片/内部材料
filler = "聚酯纤维"  # 填充材料
temperature_range = "18°С -37°С"# 温度范围， °С
style = "海滩"  # 风格
type_of_exercise = "游泳"  # 运动种类
clothing_type = "高腰"  # 服装类型
button_type = "其它"  # 扣子类型
waist = "标准"  # 腰
clothing_package_type = "包"  # 服装包装类型
JSON_size_table =json_table  # JSON 大小表
# JSON_rich_content = json_rich  # JSON 丰富内容
breast_support_level = "平均"  # 乳房支撑水平