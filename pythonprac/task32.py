import pandas as pd
import requests
from bs4 import BeautifulSoup


dec=requests.get('https://www.bikedekho.com/new-bikes')
print(dec)

'''

output 

403

refuses to authorize the info

'''