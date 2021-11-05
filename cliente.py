from historico import Historico

class Cliente():

    __slots__ = ['_nome', '_sobrenome', '_cpf', '_possuiCONTA', '_historico']

    def __init__(self, pessoa, possuiCONTA='nao'):
        self._nome = pessoa.nome
        self._sobrenome = pessoa.sobrenome
        self._cpf = pessoa.cpf
        self._possuiCONTA = possuiCONTA
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

    @property
    def possuiCONTA(self):
        return self._possuiCONTA

    @possuiCONTA.setter
    def possuiCONTA(self, possuiCONTA):
        self._possuiCONTA = possuiCONTA