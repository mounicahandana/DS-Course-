import pandas as pd
import requests
from bs4 import BeautifulSoup

dec=requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
con=BeautifulSoup(dec.content,'html.parser')

#names

namelist=con.find_all('td',class_='titleColumn')
# print(namelist)
names=[]
# for i in namelist:
#     i=i.text.replace('\n','')
#     i=i.strip(' ')
#     names.append(i)

# print(names)








#links

linklist=con.find_all('td',class_='titleColumn')
links=[]

print(linklist)
for i in linklist:
    l1=i.a
    l2=l1.get('href')
    l3='https://www.imdb.com/'+l2+'?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=EQB39P6H5C0Y6P05YNW7&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1'
    links.append(l3)

print(links)






# images

imglist=con.find_all('img')
img=[]
for i in range(0,len(imglist)):
    img.append(imglist[i]['src'])
# print(img)

#years

yearlist=con.find_all('span',class_='secondaryInfo')
years=[]
for i in range(len(yearlist)):
    years.append(yearlist[i].text)
# print(years)

df=pd.DataFrame()
df['name']=names
df['links']=links
df['images']=img
df['years']=years

df.to_csv('imdbtop_250.csv')