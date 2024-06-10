# Relizamos a importação da biblioteca SQLITE3
import sqlite3

#Abrimos a coneção e atribuimos ela a uma variável
conexao = sqlite3.connect('exemplo.db')
#Utilizamos as opções pressentes na coneção
cursor = conexao.cursor()

#Realizamos a operaçao de inserir dados nos campos informados e colocamos placeholders
# em seguida nós informamos os dados
cursor.execute('INSERT INTO usuarios (nome, idade) VALUES (?, ?)', ('Alice', 30)) 
cursor.execute('INSERT INTO usuarios (nome, idade) VALUES (?, ?)', ('Marcos', 25))

#comprometemos nossa alteração para o banco
conexao.commit()

#fechamos a conexão com o banco
conexao.close()