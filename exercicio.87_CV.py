# Aprimore o desafio anterior, mostrando no final:                                                    
#   A) A soma de todos os valores pares digitados.                                                                                                  
#   B) A soma dos valores da terceira coluna.                                                                                                                
#   C) O maior valor da segunda linha.

 matriz=[[],[],[]]
soma_pares=0
soma_colunas=0
max=0
for l in range(0,3):
    for col in range(0,3):
        num=int(input(f'digite o número{[l]}{[col]}:'))
        matriz[col].append(num)
        if num % 2==0:
            soma_pares+=num
print('\na matriz 3x3 é:')
print('='*20)
for col in range(0,3):
    for l in range(0,3):
        print(f'[ {matriz[col][l]} ]',end=' ')
        if l == 2:
            print('')
print('='*20)
print(f'a soma dos números pares de toda matriz é:{soma_pares}')
for l in range(0,3):
    soma_colunas+=matriz[l][2]
    if c==0:
        max=matriz[1][0]
    else:
        if max <= matriz[1][c]:
            max=matriz[1][c]
print(f'a soma dos valores da terceira coluna dá {soma_colunas}')
print(f'o maior valor da segunda linha é: {max}')
