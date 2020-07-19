#Criando uma calculadora com o python
import os
def limpar():
    return os.system("cls")
sair = "n"
def decidir(decidir):
    if(decidir == 1):
        limpar()
        print("Digite os 2 valores em sequência: ")
        x1 = input ('')
        limpar()
        print (x1, '+', end = '')
        x2 = input (' ')
        limpar()
        print (x1, '+', x2)
        somar(float(x1), float(x2))
    elif(decidir == 2):
        limpar()
        print("Digite os 2 valores em sequência: ")
        x1 = input ('')
        limpar()
        print (x1, '-', end = '')
        x2 = input (' ')
        limpar()
        print (x1, '-', x2)
        subtrair(float(x1),float(x2))
    elif(decidir == 3):
        limpar()
        print("Digite os 2 valores em sequência: ")
        x1 = input ('')
        limpar()
        print (x1, '÷', end = '')
        x2 = input (' ')
        limpar()
        print (x1, '÷', x2)
        dividir(float(x1), float(x2))
    elif(decidir == 4):
        limpar()
        print("Digite os 2 valores em sequência: ")
        x1 = input ('')
        limpar()
        print (x1, '*', end = '')
        x2 = input (' ')
        limpar()
        print (x1, '*', x2)
        multiplicar(float(x1), float(x2))
    elif(decidir == 5):
        limpar()
        print("Digite os 2 valores em sequência: ")
        x1 = input ('')
        limpar()
        print (x1, '^', end = '')
        x2 = input (' ')
        limpar()
        print (x1, '^', x2)
        potencia(float(x1), float(x2))
    elif(decidir == 6):
        limpar()
        print('Digite 2 - raiz quadrada, 3 - cubica, 4...')
        x2 = input('\n')
        x1 = input('Digite o numero para fazer a raiz:')
        raiz(float(x1),float(x2))
def somar(x1, x2):
    limpar()
    total = x1 + x2
    return print(x1, '+', x2, '=', total)
def subtrair(x1, x2):
    total = x1 - x2
    return print (x1, '-', x2, '=', total)
def dividir(x1, x2):
    total = x1 / x2
    print (x1, '÷', x2, '=', total)
    print ('Deseja arredondar?(s/n)')
    deci = input ('')
    if deci == 's':
        limpar()
        arredondar = input('Para quantas casas?\n')
        int(arredondar)
        print ()
        return print (x1,'÷',x2,'=', round(total, int(arredondar)))
    else:
        return 0
def multiplicar(x1, x2):
    total = x1 * x2
    return print(x1, '*', x2, '=', total)
def potencia(x1,x2):
    total = x1 ** x2
    return print(x1, '^', x2, '=', total)
def raiz(x1, x2):
    x2 = 1/x2
    total = x1 ** x2
    print('A raiz é =', total)
    deci = input('Deseja arredondar(s/n)')
    if deci == 's':
        arredondar = input('Quantas casas:')
        return print('A raiz é =', round(total, int(arredondar)))
while sair == "N" or sair == "n":
    limpar()
    print ("Digite o numero da operação:\n"
      "1 - Somar\n"
      "2 - Subtrair\n"
      "3 - Dividir\n"
      "4 - Multiplicar\n"
      "5 - Potencia\n"
      "6 - Raiz\n")
    decisao = input ('')
    decidir(int(decisao))
    print(flush = True)
    sair = input('Deseja sair?(s/n)\n')