#Programa de teste python
import random #Biblioteca para numeros randomicos
import os #Biblioteca para usar comando do tipo (system("PAUSE, CLS..."))
import array
os.system("CLS")
l = []
i = 0
x = 5
y = 3
print('x: ', x, 'y: ', y)
soma = x + y
divisao = x / y
multiplicar = x * y
elevado = x ** y
print('A soma é: ', soma, '\nA divisao é: ', divisao, '\nA multiplicação é: ', multiplicar, '\nElevado é: ', elevado)

os.system("PAUSE")
os.system("CLS")

print("Agora vou fazer um for")
for i in range(5):
    print(i, end=' ', flush=True)
    l.append (i*i)#Adicionando i para um novo espaço da array

print('\nAgora array')
for i in range(len(l)):#len é para ser o limite (tamanho da array) representa o (vet[5] "no caso o 5")
     print('Array recebe ', i, ' * ', i)
     print ('Array = ', l[i])#Exibir os valores de l

print()
os.system("PAUSE")
os.system("CLS")

a = input ("Agora adicione um novo valor para a array: ")#a = input ou seja usuario digita, nessa linha no caso aparece a mensagem depois para digitar
l.append(int (a))

print ("Mostrando o novo valor")
for i in range(len(l)):
    print (i, ' - ', l[i])
rdm = random.randrange(0,len(l))
rdm2 = random.randrange(0,len(l))
print ('Somando os valores da', rdm, 'º + ', rdm2, 'º casa')
soma2 = l[rdm] + l[rdm2]
print (soma2)

os.system("PAUSE")
os.system("CLS")

remove = random.randrange(1,len(l))#Removendo um valor aleatorio do array
print ("Irei remover um numero aleatório de l")
l1 = l.copy()
removido = l[remove]
l.remove(removido)
print ('Numero removido foi o: ', removido)

for i in range(len(l1)):
    print (l1[i], end = " ", flush = True)
print('\nNova array')
for i in range(len(l)):
    print (l[i], end = " ", flush = True)

print('')#Pulando linha
os.system("PAUSE")
os.system("CLS")

print("Matriz em python")
T = [[11, 12, 5, 2], [15, 'pode',10], [10, 8, 12, 'ter letras'], [12,'ou',8,'numeros']]
for r in T:
    for c in r:
        print(c,end = " ")
    print()
