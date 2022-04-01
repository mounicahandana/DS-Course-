'''

TOP IT COMPANIES WEB SCRAPINg

NAMES AND LINKS

'''

import pandas as pd
import requests
from bs4 import BeautifulSoup

dec=requests.get('https://indiancompanies.in/top-10-it-company-in-india/')

con=BeautifulSoup(dec.content,'html.parser')

namelist=con.find_all('span',class_='lwptoc_item_label')

names=[]
for i in namelist:
    names.append(i.text)

names1=names[1:]
# print(names1)

#links

linklist=con.find_all('div',class_='lwptoc_item')
links=[]
for i in linklist:
    l1=i.a
    l2=l1.get('href')
    l3='https://indiancompanies.in/top-10-it-company-in-india/'+l2
    links.append(l3)
links2=links[1:]
# print(len(links2))

df=pd.DataFrame()
df['IT COMPANY NAME']=names1
df['LINKS']=links2


df.to_csv('Top_10_IT_COMPANIES.csv')




