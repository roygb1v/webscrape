import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

r = requests.get('https://www.bloomberg.com/asia')

soup = BeautifulSoup(r.text, 'html.parser')

#results_1 = soup.find_all('section', attrs={'class':'single-story-module__eyebrow'})
results_2 = soup.find_all('article', attrs={'data-type':'article'})

records = []

#Concat bloomberg since headline is missing
for result in results_2:
    date = result.find('time')['datetime'][0:-8]
    url = 'www.bloomberg.com' + result.find('a')['href']
    records.append((date, url))


df = pd.DataFrame(records, columns=['Date','Url'])
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values(by='Date', ascending=False)

df.to_csv('Bloomberg.csv', index = False, encoding = 'utf-8')

