import datetime
from conexaoBD import ConexaoBD

class Historico:
    def __init__(self, num=0, descricao=''):
        self.num = num # Número da conta.
        self.descricao = descricao
        self.data = datetime.date.today()
        '''self.id = ConexaoBD().gerarID_historico()
        self.data_abertura = datetime.date.today()
        self.transacoes = Transacoes()
        self.id_transacoes = self.transacoes.id'''
    
    def imprime(self, num):
        #print("-" * 60)
        #print(f"data de abertura: {self.data_abertura}")
        #print("transacoes: ")
        for i in ConexaoBD().executaSELECT(f"SELECT * from historico where conta_num = {num}"):
            for j in i:
                print(f"- {j}")
        print("-" * 60)
