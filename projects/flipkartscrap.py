import pandas as pd
import requests
from bs4 import BeautifulSoup

resp=requests.get('https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&param=7564&otracker=clp_metro_expandable_1_3.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_Q1PDG4YW86MF_wp3&fm=neo%2Fmerchandising&iid=M_f08f16c6-c1f2-4c94-8824-d8c5b9e8c7f4_3.Q1PDG4YW86MF&ssid=qm2v7bk6o00000001645105663320')
# print(resp)
s=BeautifulSoup(resp.content,'html.parser')
# print(s.prettify())

#RATINGS

ratings=s.find_all('div',class_='_3LWZlK')  #u get list of all div tags
ratingsl=[]

for i in ratings:
    ratingsl.append(i.get_text())

# print(ratingsl)

#NAMES

names=s.find_all('div',class_='_4rR01T')  #u get list of all div tags
# print(len(names))
namesl=[]

for i in names:
    namesl.append(i.get_text())   #TAKE ONLY get_text() avoid using text

# print(namesl)

#REVIEWS 


reviews=s.find_all('span',class_='_2_R_DZ')
reviewsl=[]

for i in reviews:
    reviewsl.append(i.get_text())

# print(reviewsl)


#PRICES

prices=s.find_all('div',class_='_30jeq3 _1_WHN1')
pricesl=[]

for i in prices:
    pricesl.append(i.get_text()) 

# print(len(pricesl))



df=pd.DataFrame()

df['RATINGS']=ratingsl
df['names']=namesl
df['REVIEWS']=reviewsl
df['PRICEX']=pricesl

print(df)



