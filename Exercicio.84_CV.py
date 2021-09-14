# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
# No final, mostre:                                                                                                    
#   A) Quantas pessoas foram cadastradas.                                                                                                                
#   B) Uma listagem com as pessoas mais pesadas.                                                                                                   
#   C) Uma listagem com as pessoas mais leves.

lista = list()
lista_composta = []
while True:
    pessoa = str(input('digite seu nome:'))
    lista.append(pessoa)
    peso = float(input('digite seu peso:'))
    lista.append(peso)
    lista_composta.append(lista[:])
    lista.clear()
    escolha = str(input('você quer continuar?[S] ou [N]:')).strip().upper()[0]
    while not escolha in 'SN':
        escolha = str(input('você quer continuar?[S] ou [N]:')).strip().upper()[0]
    if escolha == 'N':
        break
peso_maior = peso_menor = 0
p_menor = []
p_maior = []
for c, v in enumerate(lista_composta):
    if c == 0:
        peso_maior = peso_menor = v[1]
        p_maior.append(v[0][:])
        p_menor.append(v[0][:])
    else:
        if peso_maior == v[1]:
            p_maior.append(v[0])
        elif peso_maior < v[1]:
            peso_maior = v[1]
            p_maior.clear()
            p_maior.append(v[0])
        if peso_menor == v[1]:
            p_menor.append(v[0])
        elif peso_menor > v[1]:
            peso_menor = v[1]
            p_menor.clear()
            p_menor.append(v[0])
print('=-' * 50)
print(f'Foram cadastradas {len(lista_composta)} pessoas')
print(f'o maior peso  foi de {peso_maior}kg, sendo as pessoas: {p_maior}')
print(f'o menor peso foi de {peso_menor}kg, sendo as pessoas:{p_menor}')
print('=-' * 50)
