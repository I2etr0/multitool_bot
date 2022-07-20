from bs4 import BeautifulSoup as bs
import requests

url = 'https://world-weather.ru/pogoda/georgia/tbilisi/'
response = requests.get(url)

soup = bs(response.text, 'html.parser')


# Parser "today"
class Parser:
    def parser(self, site, current_day, mass, current, day_wk, nmbrDay, month, wtDay, wtNight, res, result, currency):
        self.current_day = current_day
        self.site = site

        self.mass = mass
        self.current = current

        for i in current_day:
            self.day_wk = day_wk
            self.nmbrDay = nmbrDay
            self.month = month
            self.wtDay = wtDay
            self.wtNight = wtNight

            self.res = res
            self.mass.extend(self.res)

        self.result = result

        self.currency = currency
        self.currency.extend(list(self.result.split('\n\n')))

        self.r = [self.currency[0]]
        self.i = 1
        self.j = 0

        while self.i < len(self.currency):
            if self.r[self.j] != self.currency[self.i]:
                self.r.append(self.currency[self.i])
                self.j += 1
            self.i += 1
        # End "today's" parser


class Today(Parser):
    today = Parser()

    today.current_day = soup.find_all('li', {'class': 'tab-w current'})

    today.mass = []
    today.current = []

    today.current_day = soup.find_all('li', {'class': 'tab-w current'})
    for i in today.current_day:
        today.day_wk = i.find_next('div', {'class': 'day-week'}).text.strip()
        today.nmbrDay = i.find_next('div', {'class': 'numbers-month'}).text.strip()
        today.month = i.find_next('div', {'class': 'month'}).text.strip()
        today.wtDay = i.find_next('div', {'class': 'day-temperature'}).text.strip()
        today.wtNight = i.find_next('div', {'class': 'night-temperature'}).text.strip()

        today.res = f'''{today.day_wk} {today.nmbrDay} {today.month}\nПогода днем: {today.wtDay}\nПогода вечером: {today.wtNight}\n\n'''
        today.mass.extend(today.res)

    today.result = ''.join(today.mass) + '\n' + url

    today.currency = []
    today.currency.extend(list(today.result.split('\n\n')))

    today.r = [today.currency[0]]
    today.i = 1
    today.j = 0

    while today.i < len(today.currency):
        if today.r[today.j] != today.currency[today.i]:
            today.r.append(today.currency[today.i])
            today.j += 1
        today.i += 1

    # print('\n'.join(today.r))


class Other_days(Parser):
    other = Parser()

    other.current_day = soup.find_all('li', {'class': 'tab-w'})

    other.mass = []
    other.current = []

    for i in other.current_day:
        other.day_wk = i.find_next('div', {'class': 'day-week'}).text.strip()
        other.nmbrDay = i.find_next('div', {'class': 'numbers-month'}).text.strip()
        other.month = i.find_next('div', {'class': 'month'}).text.strip()
        other.wtDay = i.find_next('div', {'class': 'day-temperature'}).text.strip()
        other.wtNight = i.find_next('div', {'class': 'night-temperature'}).text.strip()

        other.res = f'''{other.day_wk} {other.nmbrDay} {other.month}\nПогода днем: {other.wtDay}\nПогода вечером: {other.wtNight}\n\n'''
        other.mass.extend(other.res)

    other.result = ''.join(other.mass) + '\n' + url

    other.currency = []
    other.currency.extend(list(other.result.split('\n\n')))

    other.r = [other.currency[0]]
    other.i = 1
    other.j = 0

    while other.i < len(other.currency):
        if other.r[other.j] != other.currency[other.i]:
            other.r.append(other.currency[other.i])
            other.j += 1
        other.i += 1

    # print('\n'.join(other.r[0]))
