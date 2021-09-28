import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []
    
    def imprime(self):
        print("-" * 60)
        print(f"data de abertura: {self.data_abertura}")
        print("transacoes: ")
        for i in self.transacoes:
            print(f"- {i}")
        print("-" * 60)