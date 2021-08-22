# This script scraping the information about house pricing and addresses from the web site
from bs4 import BeautifulSoup
from requests import get
import time
import random
url = 'https://www.avito.ru/omsk/kvartiry/prodam-ASgBAgICAUSSA8YQ?p='
houses = []
count = 1
while count <= 100:
    url = 'https://www.avito.ru/omsk/kvartiry/prodam-ASgBAgICAUSSA8YQ?p=' + str(count)
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    house_data = html_soup.find_all('div', class_='iva-item-content-3rB8a')
    if house_data:
        houses.extend(house_data)
        value = random.random()
        scaled_value = 1 + (value * (9 - 5))
        time.sleep(scaled_value)
    else:
        print('Empty page - scraping stopped')
        break
    count += 1
print(len(houses))
print()
n = int(len(houses) - 1)
count = 0
while count <= 10:
    info = houses[int(count)]
    price = info.find('span', {"class": "price-text-2gwnC"}).text
    tittle = info.find('a', {"class": "link-link-1PlH1"}).text
    address = info.find('div', {"class": "geo-root-3714B"}).text
    print(tittle, price, address, sep=' ')
    count += 1
