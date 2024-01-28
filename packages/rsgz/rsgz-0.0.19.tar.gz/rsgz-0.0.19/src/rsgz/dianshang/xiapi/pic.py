import re
from rsgz.tupian.normal import *
from rsgz.file.files import *
from rsgz.the_list.rsgz_list import *

def print_color_name(pic_dir):
    # pic_dir = r"\\R1\r1\新泳衣\泳衣老款\8126"
    longlist = get_files(pic_dir)
    name_list = get_base_name(longlist)
    new = get_not_number(name_list)
    new = list(map(lambda x:x.replace('.jpg', '').replace('.png','').replace('.jpeg','').replace('-',''),new))
    new = quchong_list(new)
    new = daxie_shouzimu(new)

    print(re.findall('\d+',pic_dir.split('\\')[-1])[0])
    print(print_list(new, fenge=','))
    print("XS,S,M,L,XL,2XL,3XL,4XL,5XL,6XL")