#Questão 6
'''
def fatorial(n):
    resultado = 1
    for i in range(2, n+1):
        resultado *= i


numero = int(input("digite um numero inteiro: "))
print(f"fatorial de {numero} é de {fatorial(numero)}")
'''

# Questão 7
'''
import re

def validar_senha(senha):
    if (len(senha) >= 8 and
        re.search(r"[A-Z]", senha) and
        re.search(r"[a-z]", senha) and    
        re.search(r"\d", senha) and
        re.search(r"[!@#$%''*()[]{}]")):
        return True
    else:
        return False
'''

#Questão 5

def lista_de_compras():
    compras = []

    while True:
        print("menu da lista de compras!")
        print("1. adicionar item")
        print("2. remover item")
        print("3. visualizar item")
        print("4. sair")
        escolha = input("digite o numero da opçao desejada")

        if escolha =="1":
            item = input("digite o item que deva ser adicionado")
            compras.append(item)
        elif escolha == "2":
            item = input("digite o item que quer romover")
            if item in compras:
                compras.remove(item)   
            else:
                print("estar tentando remover algo que nunca existiu!")
        elif escolha == "3":
            print("itens da lista de compras ate agora: ")
            for item in compras:
                print(item)
        elif escolha == "4":
            print("saindo...")
            break
        else:
            print("opcão inválida. tente novamente!")                