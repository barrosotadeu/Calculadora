from sys import exit
from math import sqrt




def pegaNum():
    x = int(input("Informe o primeiro numero: "))
    y = int(input("Informe o segundo numero: "))
    return x, y
    pass

def pegaNumPoteRaiz():
    x = int(input("Informe o número: "))
    return x
    pass

def soma():
    x, y = pegaNum()
    return "O resultado é " + str(x + y)
    pass

def subtracao():
    x, y = pegaNum()
    return "O resultado é " + str(x - y)
    pass

def multi():
    x, y = pegaNum()
    return "O resultado é " + str(x * y)
    pass

def div():
    x, y = pegaNum()
    return "O resultado é " + str(x / y)
    pass


def erro():
    return "Opção inválida"
    pass

def pot():
    x = pegaNumPoteRaiz()
    return x*x
    pass

def raizQuadrada():
    x = pegaNumPoteRaiz()
    x = float(sqrt(x))
    return x
    pass


def sai():
    print("Saindo")
    return  exit()
    pass

    

def calculadora_switcher(escolha):
    switcher = {
        1: soma,
        2: subtracao,
        3: multi,
        4: div,
        5: pot,
        6: raizQuadrada,
        7: sai
    }

    resultado = switcher.get(escolha, erro)()
    print(resultado)    
    


while True:
    print("*****Calculadora*****")

    escolha = int(input('''Qual operação você quer fazer?
    1.Soma
    2.Subtração
    3.Multiplicação
    4.Divisão
    5.Potenciação
    6.Raiz quadrada
    7.Sai
    \n'''))


    

    calculadora_switcher(escolha)
