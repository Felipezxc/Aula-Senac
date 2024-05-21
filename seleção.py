
def eprimo(n):
    # numeros iguais ou menores que 1 nao sao primos
    if n <= 1:
        return 'numero nao e primo.'
    
 # verificar de 2 a n/2
    for i in range(2, n//2 ):
        if n % i == 0:
            return 'numero nao e primo.'
    return 'numero e primo.'

num = int(input("entre com o numero:"))
res = eprimo(num)
print(f' {num} é primo? {res}')



# para sequinte entrada:
    #arara

# a funçao deverá retorna:
    #true

def verifica_polindromo(string):
    flag = False

    string_invvertida = string[::-1]

    if(string == string_invvertida):
        flag = True

    return flag    

# Main

input(input("Digite uma palavra ou frase: "))
     
teste1 = input("Digite uma palavra ou frase: ")
print(verifica_polindromo(teste1))

teste2 = input("Digite uma palavra ou frase: ")
print(verifica_polindromo(teste2))

teste3 = input("Digite uma palavra ou frase: ")
print(verifica_polindromo(teste3))