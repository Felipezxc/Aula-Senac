import sqlite3

class BancoDeDadosSQLite:
    def _init_(self, nome_banco):
      self.conexao = sqlite3.connect(nome_banco)
      self.cursor = self.conexao.cursor()
      self.criar_tabela()

    def criar_tabela(self):
      self.cursor.execute('''
    CREATE TABLE IF NOR EXISTS usuarios tarefas(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        concluida BOOLEAN       
        )   
    ''') 

    def adicionar_tarefa(self):
      self.cursor.execute('INSERT INTO tarefas (descriçao, concluida) VALUES (?, ?)', (descriçao, False))
      self.conexao.commit()

    def obter_tarefas(self):
       self.cursor.execute('SELECT * FROM tarefas')
       return self.cursor.fetchall()
    
    def marcar_tarefa_como_concluida(self, id_tarefa):
       self.cursor('UPDATE tarefas SET concluida = ? where id= ?', (True, id_tarefa))

class ListarDeTarefas:
   def __init__(self,db):
      self.db = db

   def adicionar_tarefa(self, descricao):
      self.db.adicionar_tarefa(descricao)

   def lista_tarefas(self):
     tarefas = self.db.obter_tarefas()
     for tarefa in tarefas:
        print(f'{tarefa[0]}. {tarefa[1]} - {Concluída if tarefa[2] else "pendente"}')
         