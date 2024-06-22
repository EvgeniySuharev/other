import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
url = 'https://funpay.com/chips/8/'

response = requests.get(url, headers=headers)
src = response.text

soup = BeautifulSoup(src, 'lxml')
users = soup.find_all('a', class_="tc-item")
for i in users:
    name = i.find('div', class_="media-user-name")
    price = i.find('div', class_="tc-price")
    name = name.contents
    price_num = price.find('div')
    price_rub = price.find('span')

    print(*name)
    print(*price_num, *price_rub)

