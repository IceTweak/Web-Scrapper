import requests
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent


options = webdriver.ChromeOptions()
options.add_argument('headless')
# change useragent
useragent = UserAgent()
options.add_argument(f'user-agent={useragent.random}')

url = 'https://coinmarketcap.com/'
driver = webdriver.Chrome(executable_path='F:\\PythonForGit\\CoinMarketCap_Scrapper_Selenium\\chromedriver'
                                          '\\chromedriver.exe', options=options)

try:
    driver.get(url)
    # click the most growing coins for the 7 days period
    week_gainers_button = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[1]/div[2]/div/div[1]/div['
                                                       '2]/table/thead/tr/th[6]/div/div/div')
    week_gainers_button.click()
    # get the html source of the page
    html = driver.page_source
    # create soup object
    soup = BeautifulSoup(html, 'lxml')
    table = soup.findChildren('tbody')
    rows = table[0].findChildren('tr')
    count = 0
    # now we print the 10 coins that have the biggest increase on the week
    for row in rows:
        coin_name = row.find_all('td')[2].find('p').text
        symbol = row.find_all('td')[2].find('div', class_='fZIJcI').find('p').text
        weekly_percents = row.find_all('td')[5].text
        price = row.find_all('td')[3].text
        if count < 10:
            print(f'{coin_name} ({symbol}): {price}')
            print(f'The weekly increase is {weekly_percents}')
            print()
            count += 1
        else:
            break
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
