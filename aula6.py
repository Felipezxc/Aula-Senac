numeros = input("digite numeros separados por espaço: ").split()

numeros = [int(numero) for numero in numeros]

contador = 0

for numero in numeros:
    if numero % 2 != 0:
        contador = contador + 1 
         
print(contador)