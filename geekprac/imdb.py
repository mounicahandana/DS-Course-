# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:10:32 2022

@author: DELL
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
responce=requests.get('https://www.imdb.com/chart/top/')
soup=BeautifulSoup(responce.content,'html.parser')
#print(responce)
name=soup.find_all('table',class_='titleColumn')
title=[]
for i in range(0,len(name)):
    title.append(name[i].get_text())
images=soup.find_all('img')
img=[]
for i in range(0,len(images)):
    img.append(images[i].get('src'))

#year=soup.find_all('span',class_='secondaryInfo')
spans=soup.find_all('span',class_="secondaryInfo")
yr=[]
for span in spans:
  yr.append(span.text)
    
ratings=soup.find_all('td',class_='ratingColumn imdbRating')
rating=[]
for i in range(0,len(ratings)):
    rating.append(ratings[i].get_text())
    
df=pd.DataFrame()
df['Movie Name']=title
df['image']=img
df['year']=yr
df['Rating']=rating
df.to_csv('top_movies.csv')