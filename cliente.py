from historico import Historico

class Cliente():
    def __init__(self, pessoa):
        self._nome = pessoa.nome
        self._sobrenome = pessoa.sobrenome
        self._cpf = pessoa.cpf
        self._historico = Historico()
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    @property
    def sobrenome(self):
        return self._sobrenome
    
    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome
        
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
