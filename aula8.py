'''
def soma_impares(lista):
    impares = [num for num in lista if num % 2 != 0]
    return sum(impares)

numeros = input("digite uma lista de numeros separados por espaço: ").split()
numeros = [int(num) for num in numeros]

soma = soma_impares(numeros)
print(" A soma dos numeros impares da lista e: ", soma)
'''

'''
def maior_elemento(lista):
    return max(lista)

numeros = input("digite os numeros da lista separados por espaço").split()
numeros = [int(num) for num in numeros]

maior = maior_elemento(numeros)
print("O maior elemento da lista é ", maior)
'''

num_alunos = int(input("quantos alunos deseja registrar?"))

media_alunos = []
media_turma = []

for i in range(1, num_alunos=1):
    print(f"alunos {i}: ")
    notas_aluno = []

    for j in range(1 ,4):
        nota = float(input(f"insira a nota {j}: "))
        notas_aluno.append(nota)
        media_turma.append(nota)

media_aluno = sum(notas_aluno) / len(notas_aluno)     
media_aluno.append(media_aluno)
print("A media do aluno é: ", media_aluno) 