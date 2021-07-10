from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com/'
response = requests.get(url).text
soup = BeautifulSoup(response,'html.parser')

news_title = soup.find_all('h3', class_='css-xxaj7r e1lsht870')
title = news_title[0].text

points = soup.find('ul', class_='css-ipcj49').find_all('li')
summary = []

for i in points:
    summary.append(i.text)

news = {head:summary,}