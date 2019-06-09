# -*- coding: utf-8 -*-
# -*- author: GXR -*-
import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='1111',
    port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE spiders CHARSET=utf8")
db.close()
