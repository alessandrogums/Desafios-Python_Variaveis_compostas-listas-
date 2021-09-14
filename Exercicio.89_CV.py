# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista_composta=[]
lista=[]
while True:
    lista.append(str(input('digite o nome do aluno:')))
    lista.append(float(input('digite sua primeira nota:')))
    lista.append(float(input('digite sua segunda nota:')))
    media=(lista[1]+lista[2])/2
    lista.append(media)
    lista_composta.append(lista[:])
    lista.clear()
    escolha=str(input('Quer continuar?Digite [S] ou [N]:')).strip().upper()[0]
    if escolha =='N':
        break
print(lista_composta)
print('='*30,'BOLETIM DOS ALUNOS','='*30)
print('NOME DO ALUNO',end='')
print(f'{"MÉDIA":>62}')
lista_nomes=[]
for c in range(len(lista_composta)):
    lista_nomes.append(len(lista_composta[c][0]))
for c in range(len(lista_composta)):
    print(f'nª{c}',lista_composta[c][0],end='')
    print(f'{lista_composta[c][3]:>{70-lista_nomes[c]}}')
print('='*80)
while True:
    escolha=int(input('Mostrar qual nota de qual aluno?Digite o nº dele.Para interromper digite 999:'))
    if escolha>=len(lista_composta):
        break
    print(f'As notas de {lista_composta[escolha][0]} são:{lista_composta[escolha][1:3]}')
