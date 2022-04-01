'''
Web Scrapping extracts the data from websites in the unstructured format. 
It helps to collect these unstructured data and convert it in a structured form.
'''
#installations
# pip install pandas
# pip install requests
# pip install beautifulsoup4

import pandas as pd
import requests
from bs4 import BeautifulSoup

responce=requests.get('https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&param=7564&otracker=clp_metro_expandable_1_3.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_Q1PDG4YW86MF_wp3&fm=neo%2Fmerchandising&iid=M_f08f16c6-c1f2-4c94-8824-d8c5b9e8c7f4_3.Q1PDG4YW86MF&ssid=qm2v7bk6o00000001645105663320')
soup=BeautifulSoup(responce.content,'html.parser')

# print(soup.prettify())
# print(responce)

names=soup.find_all('div',class_="_4rR01T")
# print(names)

name=[]
# for i in range(0,len(names)):
#     name.append(names[i].get_text())

# print(name)

for i in names:
    name.append(i.text)

# print(name)



cost=soup.find_all('div',class_="_30jeq3 _1_WHN1")

price=[]
for i in range(0,len(cost)):
    price.append(cost[i].get_text())



ratings=soup.find_all('div',class_="_3LWZlK")

rating=[]
for i in range(0,len(ratings)):
    rating.append(ratings[i].get_text())


images=soup.find_all('img',class_="_396cs4 _3exPp9")
# print(images)

img=[]
# for i in range(0,len(images)):
#     img.append(images[i]['src'])

for i in images:
    img.append(i['src'])

print(img)



links=soup.find_all('a',class_="_1fQZEK")
print(links)
link=[]
for i in range(0,len(links)):
    s='https://www.flipkart.com'+links[i]['href']
    link.append(s)

df=pd.DataFrame()
df['Name']=name
df['Price']=price
df['rating']=rating
df['Images']=img
df['Links']=link

print(len(name),len(price),len(rating),len(images),len(link))

# df.to_csv('flipkart_mobile_data.csv')




# task 32

# https://www.bikedekho.com/new-bikes

# bike images
# bike links
# bike print
# bike ratings or reviews

# task 33

# https://www.imdb.com/chart/top/?ref_=nv_mv_250

# movie name
# movie links
# movie images
# movie years


# task 34
'''
kabadi
corona
stocks
IT companys
'''



'''

bs4 docuemntatuion : https://www.crummy.com/software/BeautifulSoup/bs4/doc/

'''



