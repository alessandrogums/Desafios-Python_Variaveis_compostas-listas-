 
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente. 
  
  lista=[[],[]]
for c in range(1,8):
    num=int(input(f'digite o número {c}:'))
    if num % 2==0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'os números pares da lista são:{lista[0]}')
print(f'os números ímpares da lista são:{lista[1]}')
