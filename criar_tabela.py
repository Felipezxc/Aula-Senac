#Realizamos a importacao da biblioteca SQLITE3
import sqlite3

#abrimos a coneção e atribuimos ela a uma variavel
conexao = sqlite3.connect('exemplo.db')
#utilizamos as opções presente na conexão
cursor = conexao.cursor()

#Executamos uma tarefa: criamos uma tabela caso ela não exista, especificamos os campos
# que precisam ser preenchidos com nome do campo, tipo do campo e ,caso precise,
# chave primária.
cursor.execute('''
    CREATE TABLE IF NOR EXISTS usuarios(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER            
        )   
    ''')

#fechamos a conexão com o banco
conexao.close()