import imghdr,os
from rsgz.file.files import get_files
import ffmpy


# 查看所有图片格式
def view_picture_format(pic_dir):
    r"""
    查看所有图片格式
    pic_dir = r'C:\Users\Administrator\Desktop\xxxx'
    view_picture_format(pic_dir)
    """
    # pic_dir = r'C:\Users\Administrator\Desktop\xxxx'
    pic_set = get_files(dir_path=pic_dir)
    for pic in pic_set:
        print(imghdr.what(pic), pic)

# 查看 指定 图片格式
def view_specify_picture_format(pic_dir,pic_format):
    r"""
    查看 指定 图片格式
    pic_dir = r'C:\Users\Administrator\Desktop\xxxx'
    pic_format = r"webp"
    view_specify_picture_format(pic_dir,pic_format)
    ------
    webp C:\Users\Administrator\Desktop\xxxx\杂B90\blue.jpg
    webp C:\Users\Administrator\Desktop\xxxx\杂B90\green.jpg
    webp C:\Users\Administrator\Desktop\xxxx\杂B90\purple.jpg
    webp C:\Users\Administrator\Desktop\xxxx\杂B90\wine red.jpg
    """
    # pic_dir = r'C:\Users\Administrator\Desktop\xxxx'
    pic_set = get_files(dir_path=pic_dir)
    for pic in pic_set:
        if imghdr.what(pic)==pic_format:
            print(imghdr.what(pic), pic)


# 调用ffmpeg 转换格式
def format_pic(path, geshi):
    r"""
    path = r"C:\Users\Administrator\Desktop\xxx"
    format_pic(path,geshi='jpg')
    """
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            old_pic = os.path.join(dirpath, filename)
            if geshi not in old_pic and "Thumbs.db" not in old_pic and ".ini" not in old_pic:
                new_pic = os.path.splitext(old_pic)[0]+'.'+geshi
                ff = ffmpy.FFmpeg(inputs={old_pic: None},outputs={new_pic: None})
                ff.run()
            # os.remove(old_pic)

            if geshi not in old_pic:
                os.remove(old_pic)

if __name__ == '__main__':
    pic_dir = r'C:\Users\Administrator\Desktop\xxxx'
    pic_format = r"webp"
    # view_specify_picture_format(pic_dir,pic_format)
    path = r"C:\Users\Administrator\Desktop\xxx"

    pic_dir = r'C:\Users\Administrator\Desktop\AAA'
    view_picture_format(pic_dir)