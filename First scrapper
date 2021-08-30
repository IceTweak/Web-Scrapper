# This script scraping the information about house pricing and addresses from the web site
from bs4 import BeautifulSoup
from requests import get
import time
import random
url = 'https://www.avito.ru/omsk/kvartiry/prodam-ASgBAgICAUSSA8YQ?p='  # the web page url
houses = []  # array of getting information, in this case info about houses
count = 1
while count <= 100:
    url = 'https://www.avito.ru/omsk/kvartiry/prodam-ASgBAgICAUSSA8YQ?p=' + str(count)  # pages turning
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    house_data = html_soup.find_all('div', class_='iva-item-content-3rB8a')  # block that contains necessary info
    if house_data:
        houses.extend(house_data)
        value = random.random()               # the rest of the part before the else block is
        scaled_value = 1 + (value * (9 - 5))  # responsible for ensuring that requests are sent
        time.sleep(scaled_value)              # at a certain interval in order not to overload the web page
    else:
        print('Empty page - scraping stopped')
        break
    count += 1
print(len(houses))
print()
n = int(len(houses) - 1)
count = 0
while count <= 10:  # we can show the n blocks
    info = houses[int(count)]
    price = info.find('span', {"class": "price-text-2gwnC"}).text  # in this loop we printing the text from the blocks
    tittle = info.find('a', {"class": "link-link-1PlH1"}).text     # that contains necessary information
    address = info.find('div', {"class": "geo-root-3714B"}).text   # in this case there are price, tittle and address
    print(tittle, price, address, sep=' ')
    count += 1
