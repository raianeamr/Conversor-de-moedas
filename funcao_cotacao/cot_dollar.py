# valor do dolar em relação ao real

import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                         'like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
page = requests.get(
    'https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar&oq=cot&aqs=chrome.0'
    '.69i59j0i131i433i512j69i57j69i59j69i65j69i60l2j69i61.1077j0j7&sourceid=chrome&ie=UTF-8', headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
atributos = {'class': 'g'}

#class="DFlfde SwHCTb"

valor_dolar = soup.find_all('span', class_ = 'DFlfde SwHCTb')[0]

cotacao_dollar = float(valor_dolar['data-value'])

#print(cotacao_dollar)

