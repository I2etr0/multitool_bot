import re
import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.cbr.ru/currency_base/daily/'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
date = soup.find('button', class_='datepicker-filter_button').text.strip() # готовое отображение даты в формате dd.mm.YYYY
site = soup.find_all('table')

mass = []
current = []

for i in site:
    tenge = str(re.findall(r'([0-9]{3})\D+(К[а-я]{12}\D[тенг]+)\D+(\d+.\d+)',  str(i.find_all('tr')))).replace('\', \'', ' ')[3:36].replace(',', '.')
    print(tenge)