from rsgz.file.files import get_files
from rsgz.tupian.normal import lujing_tishi
import os

def url_creat_chenshan(lei):
    pic_path = r"\\192.168.0.200\e\李江涛\图集\成品\F短袖圆领\短袖圆领F06\F短袖圆领6-14\25333-25342"
    pic_l= get_files(pic_path)
    path_l = []
    for pic in pic_l:
        p = pic.split(os.sep)[-2:]
        path1 = r"https://rsgz001.oss-cn-shenzhen.aliyuncs.com/mangguo/{}/{}/{}".format(lei, p[0], p[1])
        if path1.split(os.sep)[-1].split(".")[-1]=="jpeg":
            path_l.append(path1)

    # # 为了ozon 做两份传输
    # if len(path_l)<=5:
    #     pass
    # if len(path_l)==6:
    #
    #     pass
    # if len(path_l)==7:
    #     pass
    # if len(path_l)==8:
    #     pass
    # if len(path_l)==9:
    #     pass
    # if len(path_l)==10:
    #     pass
    return path_l


def url_creat_yongyi():
    pass

if __name__ == '__main__':
    for i in url_creat_chenshan(lei="F06"):
        print(i)