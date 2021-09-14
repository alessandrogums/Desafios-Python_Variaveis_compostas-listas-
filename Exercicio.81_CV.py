# Crie um programa que vai ler vários números e colocar em uma lista.                  
# Depois disso, mostre:                                                                                                                                                
#   A) Quantos números foram digitados.                                                                                                                   
#   B) A lista de valores, ordenada de forma decrescente.        
#   C) Se o valor 5 foi digitado e está ou não na lista.

 lista_numeros=list()
while True:
    num=int(input('digite um número:'))
    lista_numeros.append(num)
    escolha=str(input('Quer continuar?Digite sim ou não:')).strip().lower()[0]
    if escolha=='n':
        break
print('='*40)
print(f'foram digitados {len(lista_numeros)} números')
lista_numeros.sort(reverse=True)
print(f'a lista na ordem decrescente é:{lista_numeros}')
if 5 in lista_numeros:
    print('o número 5  está na lista')
else:
    print('o número 5  não está na lista')
print('='*40)
