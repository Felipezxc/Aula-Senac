'''
import math

numero = 16
raiz_quadrada = math.sqrt(numero)
print("a raiz quadrada de", numero, "é: ", raiz_quadrada)
'''

'''
import random

numero_aleatorio = random.randint(1,100)
print("O numero aleatorio é: ", numero_aleatorio)

lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print("A lista embaralhada é: ", lista)
'''

import random

def jogo_adivinhaçao():
    numero_aleatorio = random.randint(1,100)
    tentativas = 0

    while True:
        palpite = int(input("tente adivinhar o numero entre 1 e 100!"))
        #tentativas += 1

        if palpite < numero_aleatorio:
            print("numero baixo. tente novamente.")
        elif palpite > numero_aleatorio:
            print("numero alto. tente novamente")
        else:
            print(f"parabens!! voce acertou o numero {numero_aleatorio}")
            break