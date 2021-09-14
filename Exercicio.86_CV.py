# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.

matriz=[[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        num=int(input('digite um número:'))
        matriz[c].append(num)
print('='*15)
for c in range(0,3):
    cont=0
    while not cont ==3:
        print(f'[{matriz[c][cont]}]',end=' ')
        cont+=1
    print()
print('='*15)

