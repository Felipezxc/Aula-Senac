'''
def operaçoes_basicas (a, b):
    soma = a + b
    subtraçao = a - b
    multiplicaçao = a * b
    if b != 0:
        divisao = a / b
    else:
        print("divisão não permitida!")

    return soma, subtraçao, multiplicaçao, divisao

num1 = 10
num2 = 5
resultado = operaçoes_basicas(num1, num2)
print("soma: ", resultado [0])
print("subtraçao: ", resultado [1])
print("multiplicaçao: ", resultado [2])
print("divisão: ", resultado [3])
'''

'''
def fatorial(a):
    if a == 0:
        return 1
    else:
        fat = 1
        for i in range (1, a+1):
            fat *= i
        return fat
    
x = 10
print("O fatorial de", x, "é: ", fatorial (x))
'''

a = input("digite seu nome: ")
b = int(input("digite um numero inteiro: "))
c = float(input("digite seu ponto flutuante: "))

soma = c + b

subtraçao = c - b 

def soma (b , c):
    adiçao = a + b
    return adiçao 

print("soma: ", soma(b,c))