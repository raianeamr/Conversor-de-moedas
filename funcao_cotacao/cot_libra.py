#valor da libra esterlina em relação ao real

import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                         'like Gecko) Chrome/99.0.4844.82 Safari/537.36 '}

page = requests.get('https://www.google.com/search?q=cota%C3%A7%C3%A3o+libra&ei=JIJDYu7oLO_Y5OUP9eaX4AU&ved'
                    '=0ahUKEwjuitTEqez2AhVvLLkGHXXzBVwQ4dUDCA4&uact=5&oq=cota%C3%A7%C3%A3o+libra&gs_lcp'
                    '=Cgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQggIyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQM'
                    'QgwEyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6BAgA'
                    'EEM6EQguEIAEELEDEIMBEMcBEKMCOgoIABCxAxCDARBDOg8IABCxAxCDARBDEEYQggJKBAhBGABKBAhGGABQugVYpxh'
                    'gwxloA3ABeACAAaIBiAHaDJIBBDAuMTOYAQCgAQHIAQrAAQE&sclient=gws-wiz', headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
atributos = {'class': 'g'}

valor_libra = soup.find_all('span', class_ = 'DFlfde SwHCTb')[0]
cotacao_libra = float(valor_libra['data-value'])

#print(cotacao_libra)
