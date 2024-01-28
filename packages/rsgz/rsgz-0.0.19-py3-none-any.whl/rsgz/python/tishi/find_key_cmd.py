import pymysql

def find_code(find, the_range, code_style):
    conn = pymysql.connect(host='localhost', user='root', password='131452', database='python_db001',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    print('*'*25,'查询结果','*'*25)
    with conn:
        with conn.cursor() as cursor:
            if code_style=='code':
                if the_range!='':
                    sql = r'''select `range`, `need`, `code` from code_sql where `des` like "%{}%" and `range` like "%{}%";'''.format(find, the_range)
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    for i in result:
                        print("功能:", i['need']+'---[范围:{}]'.format(the_range), "\n代码:")
                        print(i['code'])
                        print('-'*35)
                else:
                    sql = r'''select `range`, `need`, `code` from code_sql where `des` like "%{}%";'''.format(find)
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    for i in result:
                        print("功能:", i['need'] + '---[范围:{}]'.format(i['range']), "\n代码:")
                        print(i['code'])
                        print('-' * 35)

            elif code_style=='concept':
                if the_range!='':
                    sql = r'''select `range`, `obj`, `understand` from understand_sql where `des` like "%{}%" and `range` like "%{}%";'''.format(find, the_range)
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    for i in result:
                        print("功能:", i['need']+'---[范围:{}]'.format(the_range), "\n代码:")
                        print(i['code'])
                        print('-'*35)
                else:
                    sql = r'''select `range`, `obj`, `understand` from understand_sql where `des` like "%{}%";'''.format(find)
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    for i in result:
                        print("功能:", i['obj'] + '---[范围:{}]'.format(i['range']), "\n代码:")
                        print(i['understand'])
                        print('-' * 35)

code_style='code'  # 代码
# code_style='concept'  # 概念
the_range=''  #范围
find=str(input('查询内容:'))
find_code(find, the_range, code_style)