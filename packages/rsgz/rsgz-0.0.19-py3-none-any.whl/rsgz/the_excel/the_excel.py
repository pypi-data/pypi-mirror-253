import os,re
import openpyxl
from rsgz.file.files import get_files
from rsgz.file.files import paixu_file
from rsgz.the_str.rsgz_str import print_string

# 展示 excel 表名列表
def show_excel_tablename(excel_file):
    r"""
    excel_file = r"\\R1\r1\已经完成\Excel\DDD"
    """

    def rsgz_format(jianju, v_name, jianju_s):
        r"""
        jianju  字符串间距
        v_name  变量名
        jianju_s  批量间距
        """
        len_str = jianju - len(v_name.encode('GBK')) + len(v_name) + jianju_s
        return len_str

    # excel_list = get_files(r"\\R1\r1\已经完成\Excel\DDD")
    excel_list = get_files(excel_file)

    # 排序
    excel_list = paixu_file(file_list=excel_list, jiangxu=0)
    # for i in excel_list:
    #     print(i)

    for one_file in excel_list:
        wb = openpyxl.load_workbook(one_file)

        n1 = one_file.split(os.sep)[-1]
        n2 = wb.worksheets[0].title
        n3 = wb.worksheets[-1].title
        jianju_s = -5
        print('{n1:<{len1}}'
              '{n2:<{len2}}'
              '{n3:<{len3}}'.format(n1=n1, n2=n2, n3=n3,
                                    len1=rsgz_format(22, n1, jianju_s),
                                    len2=rsgz_format(22, n2, jianju_s),
                                    len3=rsgz_format(22, n3, jianju_s)))

# 字母和数字映射
def generate_alpha2num(length=260):
    r"""
    alpha2num = generate_alpha2num(length=100)
    print(alpha2num)
    {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7}
    """
    alpha2num = {}
    for num in range(1, length + 1):
        if num <= 26:
            alpha2num[chr(num + 64).upper()] = num  # 字母A的编号是65
        elif num > 26:
            if num - 26<=26:
                alpha2num['A'+chr(num - 26 + 64).upper()]=num
            if num-26>26:
                yu = (num - 26) // 26

            column_letter = ''
            while shengyu>0:
                if shengyu % 26== 0:  # 如果能整除
                    column_letter = "Z" + column_letter
                shengyu = shengyu // 26

            alpha2num[column_letter] = num-26
    return alpha2num

# 转换单元格坐标
# cell_to_num(cell="CV100",length=200)--->(100, 100)
@print_string
def cell_to_num(cell, length):
    r"""
    cell_to_num(cell="CV100",length=200)--->(100, 100)
    这个转换还是有问题
    """
    alpha2num = generate_alpha2num(length=length)
    pattern = re.compile(r'[a-zA-Z]+')
    col_letter = pattern.search(cell).group()
    col_num = alpha2num[col_letter.upper()]
    row = re.search(r'\d+', cell).group()
    row = int(row)
    return (col_num, row)

# column_to_name(100)-->CV
def column_to_name(colnum):
    r"""
    column_to_name(100)-->CV
    """
    if type(colnum) is not int:
        return colnum
    str = ''
    while(not(colnum//26 == 0 and colnum % 26 == 0)):
        temp = 25
        if(colnum % 26 == 0):
            str += chr(temp+65)
        else:
            str += chr(colnum % 26 - 1 + 65)
        colnum //= 26
    return str[::-1]

# colname_to_num("CV")-->100
def colname_to_num(colname):
    r"""
    colname_to_num("CV")-->100
    """
    colname = re.search(r'\D+', colname).group()

    if type(colname) is not str:
        return colname
    col = 0
    power = 1
    for i in range(len(colname)-1,-1,-1):
        ch = colname[i]
        col += (ord(ch)-ord('A')+1)*power
        power *= 26
    return col


if __name__ == '__main__':
    # print(cell_to_num(cell="AZ100", length=200))
    alpha2num = generate_alpha2num(length=30)
    print(alpha2num)
    print(len(alpha2num))