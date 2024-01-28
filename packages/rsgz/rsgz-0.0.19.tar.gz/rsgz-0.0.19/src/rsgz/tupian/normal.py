import os,time
from PIL import Image
from rsgz.file.files import get_files
from multiprocessing.pool import ThreadPool  # 线程池



# 放大图片
def fangda(path_fu,size_x,size_y):
    r"""
    批量放大图片，没有格式要求
    只能是等比例放大 (x=y才放大！！！)
    size_x,size_y = 900,900
    path_fu = r"C:\Users\Administrator\Desktop\444"
    fangda(path_fu,size_x,size_y)
    """
    for dirpath, dirnames, filenames in os.walk(path_fu):
        for filename in filenames:
            pic = os.path.join(dirpath, filename)
            if '.png' in pic or '.jpeg' in pic or 'jpg' in pic:
                im = Image.open(pic)
                x1, y1 = im.size
                if x1 == y1:  # 500 500 400 400 800 800
                    if x1 != size_x and y1 != size_y:
                        print(pic, im.size)
                        img = im.resize((size_x,size_y))
                        img.save(pic, quality=100, subsampling=100)
                        print("{} 修改尺寸--->{}*{}成功！".format(pic, size_x, size_y))

# 检查尺寸
def check_pic_sizex_sizey(path_fu, sizex,sizey):
    r"""
    批量检查文件夹里面的图片尺寸是否是sizex sizey
    sizex,sizey=900,900
    path_fu = r"C:\Users\Administrator\Desktop\linshi-user"
    check_pic_sizex_sizey(path_fu, sizex,sizey)
    """
    for dirpath, dirnames, filenames in os.walk(path_fu):
        for filename in filenames:
            pic = os.path.join(dirpath, filename)
            if '.png' in pic or '.jpg' in pic or '.jpeg' in pic:
                im = Image.open(pic)
                x1, y1 = im.size
                if x1 != sizex and y1 != sizey:
                    print(pic, im.size)

# 添加背景
def png_add_beijing_to_jpg(dir1,pic_background):
    r"""
    将png图片添加背景得到jpg 图片
    芒果公司要求：请注意 这里面的 pic_background  背景图片 一定要 修改成900*900 png 格式的
    dir1 = r"C:\Users\Administrator\Desktop\xxx"
    pic_background = r"C:\Users\Administrator\Desktop\芒果代码\套图\bei2-900.png"  # 这是你定义的背景图  通常是白色墙壁 但是也可能出现其他背景图
    png_add_beijing_to_jpg(dir1,pic_background)
    """

    # 原始的贴图函数
    def tietu(logo, logo_loc_xy, pic, save_imageFile):
        # mark = Image.open(waterPic)
        with Image.open(logo).convert("RGBA") as mark:  # 打开水印
            with Image.open(pic).convert("RGBA") as picture:  # 打开原图
                layer = Image.new('RGBA', picture.size, (0, 0, 0, 0))  # 新建一个层
                layer.paste(mark, logo_loc_xy)  # 层里面贴水印  等于层和水印一条船了
                out = Image.composite(layer, picture, layer)  # 层与原图结合就行了
                out.save(save_imageFile, quality=255, subsampling=0)

    # 文件集合 # 所有文件
    def all_file(dir1):
        pic_full_set = []
        for dirpath, dirnames, filenames in os.walk(dir1):
            for filename in filenames:
                pic_full = os.path.join(dirpath, filename)
                if '.png' in str(pic_full.split(os.sep)[-1]):
                    pic_full_set.append(pic_full)
                    # print(pic_full)
        return pic_full_set

    # 开始贴图
    def tie(tu, pic_background):
        try:
            logo = tu
            logo_loc_xy = 0, 0
            pic = pic_background
            # pic = r"E:\R1\原图\beijing\bei2.png"
            save_imageFile = tu.replace(".png", '@.png')
            tietu(logo, logo_loc_xy, pic, save_imageFile)

            im = Image.open(save_imageFile)
            im = im.convert('RGB')
            xin_pic = save_imageFile.replace('@.png', '.jpg')
            im.save(xin_pic, quality=100, subsampling=0)
            os.remove(save_imageFile)
        except:
            print("{}有问题!".format(tu))

    # 所有图片生成jpg
    def start_creat(pic_full_set, pic_background):
        pool = ThreadPool(processes=10)
        for t in pic_full_set:
            pool.apply_async(func=tie, args=(t, pic_background,))
            print(t, "正在处理!")
        pool.close()
        pool.join()

    start = time.time()
    # dir1 = r"C:\Users\Administrator\Desktop\444-900"
    # pic_background = r"C:\Users\Administrator\Desktop\芒果代码\紫冰做图\bei2-900.png"  # 这是你定义的背景图  通常是白色墙壁 但是也可能出现其他背景图
    pic_full_set = all_file(dir1)
    start_creat(pic_full_set, pic_background)
    print('[info]耗时：%s' % (time.time() - start))

# 批量去除 图片名 杂字符串
def remove_pic_str(path_fu, *remove_str):
    r"""
    批量去除 图片名 杂字符串
    path_fu = r"C:\Users\Administrator\Desktop\333"  # 这个文件夹里面的所有图片
    remove_str = ['-removebg-preview','_']  # 这个就是需要去除的字符串列表  元素数量任意
    remove_pic_str(path_fu, *remove_str)
    """
    for dirpath, dirnames, filenames in os.walk(path_fu):
        for filename in filenames:
            pic = os.path.join(dirpath, filename)
            if '.png' in pic or '.jpg' in pic or '.jpeg' in pic:
                # new_name = pic.split(os.sep)[-1].replace('-removebg-preview','').replace('_', ' ').title().replace('Png', 'png')
                pic_name = pic.split(os.sep)[-1]
                qian = os.path.dirname(pic)
                for str in remove_str:
                    pic_name = pic_name.replace(str, '')
                pic_name = pic_name.lower()
                new_name = os.path.join(qian,pic_name)
                os.rename(pic, new_name)
                if __name__ == '__main__':
                    print(new_name)

# 删除Thumbs.db文件
def remove_Thumbs(path):
    r"""
    path = r"C:\Users\Administrator\Desktop\假模长袖"
    remove_Thumbs(path)
    """
    for i in get_files(path):
        if "Thumbs.db" in i:
            print(i)
            os.remove(i)

# 路径提示
def lujing_tishi(pic):
    r"""
    pic = r"C:\Users\Administrator\Desktop\vvvvv\1.jpg"
    """
    print("传进图片:  {}\n".format(pic))
    print("后缀名:  {}, {}".format(pic.split(".")[-1], 'pic.split(".")[-1]'))
    print("后缀名:  {}, {}".format(os.path.splitext(pic)[1], "os.path.splitext(pic)[1]"))
    print("文件名:  {}, {}".format(pic.split(os.sep)[-1].split(".")[0], 'pic.split(os.sep)[-1].split(".")[0]'))
    print("文件名1:  {}, {}".format(pic.split(os.sep)[-1], "pic.split(os.sep)[-1]"))
    print('当前文件:  {}, {}'.format(__file__, "__file__"))
    print("父目录:  {}, {}".format(os.path.dirname(pic), "os.path.dirname(pic)"))
    print("文件名:  {}, {}".format(os.path.basename(pic), "os.path.basename(pic)"))
    print("传进图片:  {}".format(pic))
    print("预测目录1:  {}, {}".format(os.path.splitext(pic)[0], "os.path.splitext(pic)[0]"))
    print("预测目录2:  {}, {}".format(os.path.splitext(pic)[0]+"\\n.jpg", 'os.path.splitext(pic)[0]+"\\n.jpg"'))
    print("预测目录3:  {}, {}".format(os.path.dirname(pic)+"\\output"+pic.split(os.sep)[-1].split(".")[0]+"\\n.jpg", 'os.path.dirname(pic)+"\\output"+pic.split(os.sep)[-1].split(".")[0]+"\\n.jpg"'))
    print("预测目录4:  {}, {}".format(os.path.dirname(__file__)+"\\output"+pic.split(os.sep)[-1].split(".")[0]+"\\n.jpg", 'os.path.dirname(__file__)+"\\output"+pic.split(os.sep)[-1].split(".")[0]+"\\n.jpg"'))

# 文件夹内修改名字为 pic_rename_123
def pic_rename_123(dirs, start):
    r"""
    dirs = r"C:\Users\Administrator\Desktop\实验"
    pic_rename_123(dirs, start = 90)
    """
    allfile = get_files(dirs)
    for i in range(0, len(allfile)):
        pic = allfile[i]
        pic_finall = os.path.join(os.path.dirname(pic), "@@@-"+str(i + start) + os.path.splitext(pic)[1])
        os.rename(pic, pic_finall)
        print(pic,"--->",pic_finall)

    allfile2 = get_files(dirs)
    for i in range(0, len(allfile2)):
        pic = allfile2[i]
        os.rename(pic, pic.replace("@@@-", ""))

# 查看图片通道数
def view_channel(path_dir):
    r"""
    from PIL import Image
    path_dir = r"C:\Users\Administrator\Desktop\vvvvv"
    to_3channel(path_dir)
    """

    for pic in get_files(path_dir):
        img = Image.open(pic)
        print(len(img.split()))

# 4-->3 图片通道转换
def channel4_to_3(pic):
    r"""
    from PIL import Image
    channel4_to_3()
    """

    if Image.open(pic).mode=="RGB":
        print(pic, "{}-->channel 3".format(Image.open(pic).mode))
    elif Image.open(pic).mode=="RGBA":
        print(pic, "{}-->channel 4".format(Image.open(pic).mode))
    elif Image.open(pic).mode == "CMYK":
        print(pic, "{} channel 4-->channel 3".format(Image.open(pic).mode))
        Image.open(pic).convert("RGB").save(pic, quality=100, subsampling=0)
    else:
        print(pic, "{}".format(Image.open(pic).mode))

if __name__ == '__main__':
    # size_x, size_y = 800, 800
    # path_fu = r"C:\Users\Administrator\Desktop\xx"
    # fangda(path_fu, size_x, size_y)
    im_path = r"C:\Users\Administrator\Desktop\新建文件夹"
    for p in get_files(im_path):
        channel4_to_3(p)