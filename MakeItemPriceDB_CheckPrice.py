import os
import json
import requests
import sqlite3
from csv import reader
from bs4 import BeautifulSoup
import time

conn = sqlite3.connect("LostArkMarketPrice.db")
cur = conn.cursor()

CategoryList=['50000', '60000']
for cate in CategoryList:
    for pageno in range(1,7):
        url="https://lostark.game.onstove.com/Market/List_v2?firstCategory="+cate+"&pageNo="+str(pageno)+"&isInit=false"
        response = requests.get(url)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            for i in range(1,11):
                prlist=[]
                for j in range(2,5):
                    price = soup.select_one('#tbodyItemList > tr:nth-child({}) > td:nth-child({}) > div > em'.format(i,j))
                    if price is None:
                        break
                    prlist.append(price.get_text())
                if price is None:
                    break
                itemname=soup.select_one('#tbodyItemList > tr:nth-child({}) > td:nth-child(1) > div > span.name'.format(i)).get_text()
                if itemname.find('[') > 0:
                    itemname=itemname[:itemname.find('[')-1]
                sql = 'UPDATE LostArkMarketPrice SET PrevAvgPrice=?, RecentPrice=?, LowestPrice=? WHERE ItemName=?;'
                cur.execute(sql,(prlist[0],prlist[1],prlist[2],itemname))
            conn.commit()
        else :
            print(response.status_code)
        time.sleep(3)
        print("Loading..."+str(pageno)+" "+cate)

for pageno in range(1,11):
    url="https://lostark.game.onstove.com/Market/List_v2?firstCategory=70000&pageNo="+str(pageno)+"&isInit=false"
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        for i in range(1,11):
            prlist=[]
            for j in range(2,5):
                price = soup.select_one('#tbodyItemList > tr:nth-child({}) > td:nth-child({}) > div > em'.format(i,j))
                if price is None:
                    break
                prlist.append(price.get_text())
            if price is None:
                break
            itemname=soup.select_one('#tbodyItemList > tr:nth-child({}) > td:nth-child(1) > div > span.name'.format(i)).get_text()
            if itemname.find(']') > 0:
                itemname=itemname[itemname.find(']')+2:]
            sql = 'UPDATE LostArkMarketPrice SET PrevAvgPrice=?, RecentPrice=?, LowestPrice=? WHERE ItemName=?;'
            cur.execute(sql,(prlist[0],prlist[1],prlist[2],itemname))
        conn.commit()
    else :
        print(response.status_code)
    time.sleep(3)
    print("Loading..."+str(pageno)+" 70000")

for pageno in range(1,10):
    url="https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&pageNo="+str(pageno)+"&isInit=false"
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        for i in range(1,11):
            prlist=[]
            for j in range(2,5):
                price = soup.select_one('#tbodyItemList > tr:nth-child({}) > td:nth-child({}) > div > em'.format(i,j))
                if price is None:
                    break
                prlist.append(price.get_text())
            if price is None:
                break
            itemname=soup.select_one('#tbodyItemList > tr:nth-child({}) > td:nth-child(1) > div > span.name'.format(i)).get_text()
            if itemname.find('[') > 0:
                itemname=itemname[:itemname.find('[')-1]
            sql = 'UPDATE LostArkMarketPrice SET PrevAvgPrice=?, RecentPrice=?, LowestPrice=? WHERE ItemName=?;'
            cur.execute(sql,(prlist[0],prlist[1],prlist[2],itemname))
        conn.commit()
    else :
        print(response.status_code)
    time.sleep(3)
    print("Loading..."+str(pageno)+" 90000")

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
