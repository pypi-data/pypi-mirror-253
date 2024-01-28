import pymysql

r"""
https://mariadb.com/kb/en/mariadb-server-10-11-2/
pip install pymysql
pip install pymysql[rsa]
install:  D:\69-MariaDB\install
root 131452
show databases;
"""

conn = pymysql.connect(host='localhost', user='root', password='131452', charset='utf8mb4')
cursor = conn.cursor()
sql = "CREATE DATABASE IF NOT EXISTS python_db001"
cursor.execute(sql)
conn.commit()
conn.close()
# 最后在你的安装目录里面会出现这个 新建立的数据库 D:\69-MariaDB\install\data
