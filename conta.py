from historico import Historico
from cliente import Cliente

class Conta():
    
    _total_contas = 0
    
    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_id_historico', '_historico', '_senha']
    
    def __init__(self, numero=None, cliente=None, saldo=0, limite=None, senha=None):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._senha = senha
        self._historico = Historico()
        Conta._total_contas += 1
        
    # -------------------- #
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, numero):
        self._numero = numero
    
    # -------------------- #
    
    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, titular):
        self._titular = titular
    
    # -------------------- #

    @property
    def saldo(self):
        return self._saldo

    # -------------------- #
    
    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, limite):
        self._limite = limite
        
    # -------------------- #    
    
    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha):
        self._senha = senha
    
    # -------------------- #   

    @property
    def historico(self):
        return self._historico
    
    @historico.setter
    def historico(self, historico):
        self._historico = historico


    # -------------------- # 
    
    @staticmethod
    def get_total_contas():
        return Conta._total_contas
    
    # -------------------- # 
    
    def deposita(self, valor):
        if valor < 1:
            aux = False
        else:
            aux = True
            self._saldo += valor
            self.historico.transacoes.append(f"Deposito de {round(valor, 2)}R$")
        return aux
    
    def saca(self, valor):
        if valor > self._saldo or valor < 1:
            resultado = False
        else:
            resultado = True
            self._saldo -= valor
            self.historico.transacoes.append(f"Saque de {round(valor, 2)}R$")
        return resultado
        
    def extrato(self):
        self.historico.transacoes.append(f"Tirou o extrato. Saldo de {round(self._saldo, 2)}R$")
        print('-' * 50)
        print("EXTRATO:")
        print('-' * 50)
        print(f"Numero:..................{self.numero}")
        print(f"Titular:.................{self.titular.nome} {self.titular.sobrenome}")
        print(f"Saldo:...................{self._saldo:.2f} R$")
        print(f"Limite:..................{self.limite:.2f} R$")
        print('-' * 50)
        
    def transfere(self, conta2, valor):
        resultado = self.saca(valor)
        aux = False
        if resultado == False:
            aux = False
        else:
            conta2.deposita(valor)
            self.historico.transacoes.append(f"Transferencia de {valor} para a conta {conta2.numero}")
            aux = True
        return aux


    # --------------------------------------------------------- #

    def efetuarSAQUE(self, valor):
        if valor == '':
            mensagem = "Todos os valores devem ser preenchidos"
        else:
            valor1 = float(valor)
            if self.saca(valor1):
                mensagem = "Saque realizado com sucesso!"
            else:
                mensagem = "Não foi possivel realizar o saque!"
        return mensagem

    
    def efetuarDEPOSITO(self, valor):
        if valor == '':
            mensagem = "Todos os valores devem ser preenchidos"
        else:
            valor1 = float(valor)
            if self.deposita(valor1):
                mensagem = "Saque realizado com sucesso!"
            else:
                mensagem = "Não foi possivel realizar o saque!"
        return mensagem


    
