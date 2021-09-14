# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

lista_numeros=[]
lista_pares=[]
lista_impares=[]
while True:
    num=int(input('digite um número:'))
    lista_numeros.append(num)
    if num % 2 ==0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
    escolha=str(input('Quer continuar?[S] ou [N]')).strip().upper()
    if escolha in 'Nn':
        break
print(f'a lista de todos os números é:{lista_numeros}'
      f'\no conjunto de números pares desta lista:{lista_pares}'
      f'\no conjunto de números ímpares desta lista:{lista_impares}')
