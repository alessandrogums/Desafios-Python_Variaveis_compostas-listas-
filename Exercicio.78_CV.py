
#  Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
#  No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista_numeros=list()
for c in range(1,6):
    num=int(input(f'digite o número {c}º:'))
    lista_numeros.append(num)
print(f'o número de maior valor  é o {max(lista_numeros)}')
print(f'enquanto o número de menor valor é o {min(lista_numeros)}')

if lista_numeros.count(max(lista_numeros))==1:
    print(f'o {max(lista_numeros)} está na posição {lista_numeros.index(max(lista_numeros))} da lista')
else:
    print(f'o {max(lista_numeros)} está nas posições:',end=' ')
    for c,v in enumerate(lista_numeros):
        if max(lista_numeros)==lista_numeros[c]:
            print(c,end=' ')
if lista_numeros.count(min(lista_numeros))==1:
    print(f'\no {min(lista_numeros)} está na posição {lista_numeros.index(min(lista_numeros))} da lista')
else:
    print(f'\no {min(lista_numeros)} está nas posições:',end=' ')
    for c,v in enumerate(lista_numeros):
        if min(lista_numeros)==lista_numeros[c]:
            print(c,end=' ')
