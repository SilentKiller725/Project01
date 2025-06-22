import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import os

def scraping():
    url='https://merolagani.com/latestmarket.aspx'
    req=requests.get(url)
    soup=BeautifulSoup(req.text,'html.parser')

    table=soup.find('table')
    rows=table.find_all('tr')[1:]
    
    datae=[]
    for row in rows:
        data=row.find_all('td')
        if len(data)>5:
           symbol=data[0].text.strip()
           ltp=data[1].text.strip()
           open=data[5].text.strip()
           datae.append((symbol,ltp,open))
    return pd.DataFrame(datae,columns=["Symbol","LTP","Open Price"])

def wr_to_excel(data,filename):
    
    with pd.ExcelWriter(filename,engine="openpyxl",mode='w') as writer:
        data.to_excel(writer,index=False,header=False)

def job():
    print("Begin Scraping.........")
    data=scraping()
    wr_to_excel(data,"data1.xlsx")
    print("Scraping Done:")

job()

schedule.every(10).minutes.do(job)

if __name__=="__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)






