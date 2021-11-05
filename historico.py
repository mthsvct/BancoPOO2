import datetime
from conexaoBD import ConexaoBD

class Historico:
    def __init__(self):
        self.id = ConexaoBD().gerarID_historico()
        self.data_abertura = datetime.datetime.today()
        self.id_transacoes = 0
        self.transacoes = []
    
    def imprime(self):
        print("-" * 60)
        print(f"data de abertura: {self.data_abertura}")
        print("transacoes: ")
        for i in ConexaoBD().executaSELECT(f"SELECT * from transacoes where id = {self.id_transacoes}"):
            for j in i:
                print(f"- {j}")
        print("-" * 60)
