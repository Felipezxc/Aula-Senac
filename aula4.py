def fatorial(a):
    if a ==0:
        return 1
    else:
        fat = 1
        for i in range (1, a+1):
            fat *= i
            return fat
        
x = int(input("digite um numero inteiro: "))
print("O fatorial de", x, " é: ", fatorial(x))

# nome, idade, altura, tem_carro

nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
alutura = float(input("digite sua altura: "))
tem_carro = input("voce possui algum carro? (sim/não:) ")

tem_carro.lower() == "não"

print("informacoes digitadas: ")
print("nome: ", nome)
print("idade: ", idade)
print("altura: ", alutura)
print("tem carro? ", "sim" if tem_carro else "não")

def contagem_regressiva():
    numero = int(input("digite um numero inteiro positivo: "))

    if numero <= 0:
        print("por favor, digite um numero inteiro positivo.")
        contagem_regressiva

    else:
        while numero >= 0:
            print(numero)   
            numero -= 1

contagem_regressiva() 

def soma (a, b):
    return a + b
def subtraçao(a, b):
    return a - b
def multiplicaçao(a, b):
    return a * b 
def divisao(a, b):
    if b != 0: 
        return a / b
    else:
        return "divisao invalida"
    
def calculadora():
    print("bem vindo a calculadora em python!")
    print("selecione a opçao desejada: ")
    print("1: adição")
    print("2: subtração")
    print("3: multiplicação")
    print("4: divisao")

    escolha = input("digite sua escolha 1/2/3/4: ")
    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("digite o primeiro numero: "))
        num2 = float(input("digite o segundo numero: "))

        if escolha == '1':
            print("resuldado", soma(num1, num2))
        elif escolha == '2':
            print("resuldado", subtraçao(num1, num2))   
        elif escolha == '3':
            print("resuldado", multiplicaçao(num1, num2))
        elif escolha == '4':
            print("resultado", divisao(num1, num2)) 