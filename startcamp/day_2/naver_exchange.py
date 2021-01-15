import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'

response = requests.get(url).text
# print(response)

data = BeautifulSoup(response, 'html.parser')

result = data.select_one(
    '#exchangeList > li:nth-child(1) > a.head.usd > div > span.value').text
print(result)
