import sqlite3

class ItemEstoque:
    def __init__ (self, nome, marca, modelo, preço, quantidade):
       self.nome = nome
       self.marca = marca
       self.modelo = modelo
       self.preço = preço
       self.quantidade = quantidade

    def exibir_informaçoes(self):
      print(f"nome: {self.nome}, Marca: {self.marca}, Modelo: {self.modelo}, preço: {self.preço}, Quantidade: {self.quantidade}")
 
class Estoque:
   def _init_(self,db_name="estoque.db"):
    self.conn = sqlite3.connec(db_name)
    self.criar_tabela()

   def criar_tabela(self):
     with self.conn:
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS itens(
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                marca TEXT NOT NULL,
                modelo TEXT NOT NULL,
                preço REAL NOT NULL,
                quantidadade INTEGER NOT NULL
            )
        """)

   def adicionar_item(self, item):
      with self.conn:
        self.conn.execute("""
            INSERT INTO itens (nome, marca, modelo, preço, quantidade)
            VALUES (?, ?, ?, ?, ?)""", (item.nome, item.marca, item.modelo, item.preço, item.quantidade))
      print("Item adicionado ao estoque com sucesso!")
 
   def remover_item(self, nome_item):
     with self.conn:
       cursor = self.conn.execute("DELETE FROM itens WHERE nome = ?", (nome_item,))
     if cursor.rowcount > 0:
       print("Item removido com sucesso!")
     else:
       print("Item não encontrado no estoque.")