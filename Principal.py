from Cliente import Cliente
from Conta import Conta

class DadosCadastros:
	__slots__ = ['_ListaDeClientes','_ListaDeContas']
	
	def __init__(self):
		self._ListaDeClientes = []
		self._ListaDeContas = []
		
	# Função para cadastrar um cliente.
	def CadastrarCliente(self,Cliente):
		Existe = BuscarCPF(Cliente.CPF)
		if Existe == None:
			self._ListaDeClientes.append(Cliente)
			return True	
		else:
			return False
		
	# Função para adicionar uma conta.
	def AdicionarConta(self,Conta):
		Existe1 = BuscarCPF(Conta._titular.CPF)
		Existe2 = BuscaConta(Conta.numero)
		if Existe1 == None and Existe2 == None:
			self._ListaDeContas.append(Conta)
			return True
		else:
			return False
	
	# Função para procurar na lista se alguma pessoa tem o mesmo CPF.
	def BuscaCPF(self,Procurado):
		for C in self._ListaDeClientes:
			if C.CPF == Procurado:
				return C
		return None
	
	# Função para procurar se o número da conta já está na lista de contas.
	def BuscaConta(self,Procurado):
		for C in self._ListaDeContas:
			if C.numero == Procurado:
				return C
		return None
	
	# Função para verificar se aquele cliente possui uma conta na lista de contas.
	def BuscaPessoa(self,Procurado):
		for C in self._ListaDeContas:
			if C.titular.CPF == Procurado:
				return C
		return None