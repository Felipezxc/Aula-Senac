class ContaBancaria:
    def __init__(self, nome_titular, nome_conta, saldo_inicial=0):
        self.nome_titular = nome_titular
        self.numero_conta = nome_conta
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor < 0:
            print("valor de deposito invalido!")
        else:
            self.saldo += valor

def sacar(self, valor):
    if valor > 0:
     if self.saldo >= valor:
        self.saldo -= valor
     else:
        print("saldo insuficiente!")
    else:
       print("valor de saque invalido!")

def consulta_saldo(self):
    return self.saldo

def transferir(self, valor , outra_conta)
   if valor > 0:
      if self.saldo >= valor:
         self.saldo -= valor
         outra_conta.deposito(valor)
         print("transferencia feita com sucesso")
      else:
         print("voce nao possui saldo necessario para transferir! deixe de ser liso!")
    else:
        print("valor da transferencia deve ser maior do que 0, deixe de ser doido")
