'''
Packages you might need to install via pip:
1. pandas
2. requests
3. bs4
4. csv
5. io
6. lxml
'''

import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
import io

url = 'https://www.worldometers.info/coronavirus/'
html_content = requests.get(url).text

soup = BeautifulSoup(html_content, 'lxml')

table_content = soup.table
head = table_content.thead.find_all('tr')

headings = []
for i in head[0].find_all('th'):
    headings.append(i.text.replace('\n', '').strip())

data = []
body = table_content.tbody.find_all('tr')
for i in range(1, len(body)):
    row = []
    for tr in body[i].find_all('td'):
        row.append(tr.text.replace('\n', '').strip())
    data.append(row)

with io.open('covid19_cases.csv', 'w', encoding='UTF-8') as f:
    x = csv.writer(f)
    x.writerow(headings)
    for i in range(6, len(data)):
        x.writerow(data[i])

df = pd.read_csv('covid19_cases.csv', index_col=0)
print(df)
