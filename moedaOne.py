import os

import funcao_cotacao.cot_dollar
import funcao_cotacao.cot_euro

while 1:
   os.system('cls' if os.name == 'nt' else 'clear')
   print('''CONVERSOR DE MOEDAS
   Digite o número da opção desejada:
      1- Dólar --> Real
      2- Real  --> Dólar
      3- Real --> Euro
      4- Euro --> Real
      5- Real --> Libra
      6- Libra --> Real
      7- Sair''')
   op = int(input('Digite aqui: '))

   if op == 1:

      valor = float(input('Valor em dólar: '))
      total = valor * funcao_cotacao.cot_dollar.cotacao_dollar
      print ('Seu valor em reais fica: R$ %.2f.' %total)
      input('Pressione qualquer tecla para continuar')
      





