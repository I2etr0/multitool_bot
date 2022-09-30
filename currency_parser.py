# import requests
# from bs4 import BeautifulSoup as bs
#
#
# url = ''
# response = requests.get(url)
#
# soup = bs(response.text, 'html.parser')
# date = soup.find('h2', class_='h2 blue').text.strip()
# site = soup.find_all('tr')
#
# mass = []
# current = []
#
# for i in site:
#     itemName = i.find_next('td', {'class': 't-left'}).text.strip()
#     itemCode = i.find_next('span', {'class': 'col-50 t-right mr5 m-mr2'}).text.strip()
#     itemLCode = i.find_next('span', {'class': 'gray col-50 t-left ml5 m-ml2'}).text.strip()
#     itemPrice = i.find_next('span', {'class': 'mr10 m-mr0'}).text.strip()
#     itemDescription = i.find_next('td', {'class': 't-left'}).text.replace('''
#                                     ''', ' ').strip()
#     res = f'''Буквенное обозначение валюты: {itemLCode} Цифровое обозначение валюты: {itemCode} Наименование валюты: {itemDescription} Стоимость: {itemPrice}\n\n'''
#     mass.extend(res)
#
# result = ''.join(mass) + '\n' + url
#
#
#
# currency = []
# currency.extend(list(result.split('\n\n')))
#
# r = [currency[0]]
# i = 1
# j = 0
#
# while i < len(currency):
#     if r[j] != currency[i]:
#         r.append(currency[i])
#         j += 1
#     i += 1
#
# # print('\n'.join(r))