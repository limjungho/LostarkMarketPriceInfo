import os
import json
import requests
import sqlite3
from csv import reader
from bs4 import BeautifulSoup
import time

conn = sqlite3.connect("LostArkMarketPrice.db")
cur = conn.cursor()

sql = 'SELECT ItemName, Margin FROM LostArkMarketPrice;'
cur.execute(sql)
MarginList = cur.fetchall()
conn.close()
MarginFloatList=[]
for tup in MarginList:
    MarginFloatList.append((tup[0],float(tup[1])))
MarginFloatList.sort(key=lambda x:-x[1])

with open('MarginResult.txt', 'w') as fw:
    for i, tup in enumerate(MarginFloatList):
        fw.write("{}. {} {}\n".format(i+1,tup[0],tup[1]))


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
