# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente

lista_numeros=[]
while True:
    num=float(input('digite um número:'))
    while  num in lista_numeros:
        print('este número já foi adicionado na lista!')
        num=float(input('digite outro número novamente:'))
    lista_numeros.append(num)
    escolha=str(input('quer continuar?digite sim ou não:')).strip().upper()[0]
    if escolha =='N':
        break
lista_numeros.sort()
print(f'os valores adicionados em ordem crescente foram:{lista_numeros}')
