
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
lista=[]
lista_mutavel=[]
jogos=int(input('digite quantos jogos você quer que sorteie:'))
print('='*15,'JOGO DA MEGA-SENA','='*15)
for c in range(1,jogos+1):
    print(f'Jogo {c}:',end='')
    for cont in range(0,6):
        lista_mutavel.append(randint(1, 60))
        while lista_mutavel in lista:
            lista_mutavel.clear()
            lista_mutavel.append(randint(1, 60))
        lista.append(lista_mutavel[:])
        lista_mutavel.clear()
    lista.sort()
    sleep(0.8)
    print(lista)
    lista.clear()
print('='*49)
