import pymysql



sql = '''CREATE TABLE `code_sql` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `need` VARCHAR(100) NOT NULL,
  `code` VARCHAR(1000) NOT NULL,
  `des` VARCHAR(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

sql2 = '''CREATE TABLE `understand_sql` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `obj` VARCHAR(100) NOT NULL,
  `understand` VARCHAR(3000) NOT NULL,
  `des` VARCHAR(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

conn = pymysql.connect(host='localhost', user='root', password='131452', database='python_db001',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
with conn:
    with conn.cursor() as cursor:
        cursor.execute(sql2)
    conn.commit()

    with conn.cursor() as cursor:
        sql = "SELECT `id`, `obj`, `understand`, `des` FROM `understand_sql`"
        cursor.execute(sql2)
        result = cursor.fetchall()
        for i in result:
            print(i)