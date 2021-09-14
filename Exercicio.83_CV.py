# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

lista=[]
exp=str(input('digite sua expressão numérica:'))
for c in range(len(exp)):
    if '(' in exp[c]:
        lista.append('(')
    elif ')' in exp[c]:
        lista.append(')')
#para avaliar a ordem dos parênteses
cont=0
k=1
while not k>=len(lista):
    if lista[cont] in "(" and lista[k] in ")":
        lista.pop(k)
        lista.pop(cont)
        cont=-1
        k=0
    cont += 1
    k = cont + 1
if len(lista)==0:
    print('voce digitou corretamente a ordem dos parênteses')
else:
    print('você digitou errado os parenteses!')
#para avaliar se existe algum conteúdo dentro dos parênteses
for c in range(len(exp)-1):
    if exp[c] in '(' and exp[c+1]==')':
        print('porém você deixou de digitar algo entre algum dos parenteses')
