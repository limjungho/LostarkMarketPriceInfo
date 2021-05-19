import os
import json
import requests
import sqlite3
from csv import reader
from bs4 import BeautifulSoup
import time

conn = sqlite3.connect("LostArkMarketPrice.db")
cur = conn.cursor()

for ID in range(201,347):
    sql = 'SELECT * FROM LostArkMarketPrice WHERE ID=?;'
    cur.execute(sql,(ID,))
    row = cur.fetchone()
    ManuPrice=0.0
    if row[3] is not '':
        ManuPrice = float(row[3])
    if int(row[17]) == 0:
        continue

    for i in range(5,15,2):
        sql = 'SELECT LowestPrice, BundleCount FROM LostArkMarketPrice WHERE ItemName=?;'
        cur.execute(sql,(row[i],))
        mtpr = cur.fetchone()
        if mtpr is None:
            break
        if int(mtpr[0])==0:
            break
        if ID == 203:
            print(int(mtpr[0])*int(row[i+1])/mtpr[1])
        ManuPrice += int(mtpr[0])*int(row[i+1])/mtpr[1]

    ManuPrice = round(ManuPrice/int(row[4]),2)
    SellPrice = round(float(row[17])*0.95,2)
    Margin = str(round(SellPrice - ManuPrice,2))

    sql = 'UPDATE LostArkMarketPrice SET Margin=? WHERE ID=?;'
    cur.execute(sql,(Margin,ID))
    conn.commit()

conn.close()

'''

'''

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
