import os
import json
import requests
import sqlite3
from csv import reader

InitialMaterialList=[]

with open('InitialMaterial.csv', 'r', encoding='utf-8') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Check file as empty
    if header != None:
        # Iterate over each row after the header in the csv
        for row in csv_reader:
            InitialMaterialList=InitialMaterialList+row

conn = sqlite3.connect("LostArkMarketPrice.db")
cur = conn.cursor()
idcnt = 101
for name in InitialMaterialList:
    if len(name) < 1 :
        continue
    sql = 'INSERT INTO LostArkMarketPrice(ID, ItemName, BundleCount, ManuPrice, ManuCount) VALUES(?,?,0,0,0);'
    cur.execute(sql, (idcnt, name))
    idcnt+=1
conn.commit()
conn.close()

'''
# DB 생성 (오토 커밋)
conn = sqlite3.connect("test.db")
# 커서 획득
cur = conn.cursor()
# 테이블 생성 (데이터 타입은 TEST, NUMERIC, INTEGER, REAL, BLOB 등)

param1 = '1'
cur.execute('SELECT * FROM table1 WHERE id='+param1)
print('param1', cur.fetchall())

conn.commit()
'''
