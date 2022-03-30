#valor do euro em relação ao real

import requests
from bs4 import BeautifulSoup


headers = {'user-agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                         'like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
page = requests.get('https://www.google.com/search?q=cota%C3%A7%C3%A3o+euro&oq=cota%C3%A7%C3%A3o+euro&aqs=chrome'
                    '..69i57j0i131i433i512l3j0i512l2j0i131i433i512j0i512l3.2047j1j9&sourceid=chrome&ie=UTF-8', headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
atributos = {'class': 'g'}

#class="DFlfde SwHCTb"
valor_euro = soup.find_all('span', class_ = 'DFlfde SwHCTb')[0]
cotacao_euro = float(valor_euro['data-value'])

#print(cotacao_euro)



