# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista_numeros=[]
for c in range(0,5):
    num=int(input(f'digite o valor do nº{c}:'))
    if c==0:
        lista_numeros.append(num)
        print('o número foi colocado na última posição!')
    else:
        if num>=lista_numeros[c-1]:
            lista_numeros.insert(c,num)
            print(f'o número foi colocado na posição {c}')
        else:
            cont=c
            while num<lista_numeros[cont-1]:
                cont-=1
                if cont==0:
                    break
            lista_numeros.insert(cont,num)
            print(f'o número foi colocado na posição {cont}')
print(lista_numeros)
