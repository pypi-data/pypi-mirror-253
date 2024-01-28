import os
import pymysql


def add_record(need, code, des, the_range, tishi, sql_style):
    conn = pymysql.connect(host='localhost', user='root', password='131452', database='python_db001',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    print('*'*25,'添加记录','*'*25)
    with conn:
        with conn.cursor() as cursor:
            if sql_style=='code':
                sql = "INSERT INTO `code_sql` (`need`, `code`, `des`, `range`) VALUES (%s, %s, %s, %s);"
                cursor.execute(sql, (need,code,des,the_range))
            elif sql_style=='concept':
                sql = "INSERT INTO `understand_sql` (`obj`, `understand`, `des`, `range`) VALUES (%s, %s, %s, %s);"
                cursor.execute(sql, (need, code, des, the_range))
        conn.commit()
        print("{} add Success!!!".format(need))

def return_file_str(v1):
    r'''
    返回py文件内容
    '''
    v1 = os.path.join(os.getcwd(), v1)
    v2 = v1.replace('.py', '.txt')
    try:
        os.rename(v1,v2)
    except:
        pass

    r"获取文件内容"
    line_all=''
    with open(v2, 'r', encoding="utf-8") as f1:
        lines = f1.readlines()

    os.rename(v2, v1)
    return ''.join(lines[:])

# ************************* 添加记录 *************************
sql_style='code'  # 1 代码
# sql_style='concept'  # 2 概念
the_range = 'js'  # 领域
# the_range = 'dos'  # 领域
v1 = r'code.py'
code = return_file_str(v1)
des = 'fetch;随机索引;随机数;'
need = des.split(';')[0]
add_record(need, code, des, the_range, tishi=0, sql_style=sql_style)
print(code)