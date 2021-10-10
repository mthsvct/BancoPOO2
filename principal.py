from cliente import Cliente
from conta import Conta

class DadosCadastros:
	__slots__ = ['_ListaDeClientes','_ListaDeContas']
	
	def __init__(self):
		self._ListaDeClientes = []
		self._ListaDeContas = []
		
	# Função para cadastrar um cliente.
	def CadastrarCliente(self,Cliente):
		Existe = self.BuscarCPF(Cliente.cpf)
		if Existe == None:
			self._ListaDeClientes.append(Cliente)
			return True	
		else:
			return False
		
	# Função para adicionar uma conta.
	def AdicionarConta(self,Conta):
		Existe1 = self.BuscarCPF(Conta._titular.cpf)
		Existe2 = self.BuscarConta(Conta.numero)
		Existe3 = self.BuscarPessoa(Conta._titular.cpf)
		if Existe1 != None and Existe2 == None and Existe3 == None:
			self._ListaDeContas.append(Conta)
			return True
		else:
			return False
	
	# Função para procurar na lista se alguma pessoa tem o mesmo CPF.
	def BuscarCPF(self,Procurado):
		for C in self._ListaDeClientes:
			if C.cpf == Procurado:
				return C
		return None
	
	# Função para procurar se o número da conta já está na lista de contas.
	def BuscarConta(self,Procurado):
		for C in self._ListaDeContas:
			if C.numero == Procurado:
				return C
		return None
	
	# Função para verificar se aquele cliente possui uma conta na lista de contas.
	def BuscarPessoa(self,Procurado):
		for C in self._ListaDeContas:
			if C.titular.cpf == Procurado:
				return C
		return None

	def verEXTRATO(self, conta):
		
		pass
