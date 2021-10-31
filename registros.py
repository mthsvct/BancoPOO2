from pessoa import Pessoa
from cliente import Cliente
from conta import Conta

class Registros:
	__slots__ = ['_clientes','_contas']
	
	def __init__(self):
		self._clientes = []
		self._contas = []
	
	@property
	def clientes(self):
		return self._clientes

	@property
	def contas(self):
		return self._contas

	# -----------------------BUSCAS-------------------------- #

	# Função que busca um cliente pelo o cpf
	def buscaCLIENTE(self, cpf):
		encontrado = None
		for i in self.clientes:
			if i.cpf == cpf:
				encontrado = i
		return encontrado

	# Verifica se já possui uma conta com o número buscado
	def buscaCONTA(self, num):
		encontrado = None
		for i in self.contas:
			if num == i.numero:
				encontrado = i
		return encontrado

	# Busca um conta pelo o CPF:
	def buscaCONTA_cpf(self, cpf):
		encontrado = None
		for i in self.contas:
			if cpf == i.titular.cpf:
				encontrado = i
		return encontrado

	# --------------------------------------------------------------------- #

	# Retorna uma lista contendo:
		# Retorna o usuário caso seja digitado os dados corretamente, caso contrário retorna retorna None;
		# Junto com o usuário ou None é retornado uma mensagem.
	def fazerLOGIN(self, num, senha):

		logado = []

		if num != '' and senha != '':
			# todos os campos foram preenchidos
			conta = self.buscaCONTA(num) # busca o usuário na lista de funcionarios cadastrados.

			if(conta != None):
                # Funcionário existe!
				if(senha == conta.senha):
					mensagem = ("Bem vindo, "+conta.titular.nome+"!")
					logado.append(conta)
                	# logado.append(mensagem)
				else:
					# A senha não existe.
					mensagem = "Senha incorreta!"
			else:
				# O funcionário não existe.
				mensagem = "Conta nao encontrada. \nPor favor, efetue o cadastro antes do login."
		else:
			mensagem = "Todos os valores devem ser preenchidos!"

		if( len(logado) == 0 ):
			logado.append(None)
        	
		logado.append(mensagem)

		return logado


	# Função que verifica se não há cpfs repetidos e cria um objeto pessoa:
	def cadastrarCLIENTE(self, nome, sobrenome, cpf, email, tel):
		retorno = []
		
		if '' in [nome, sobrenome, cpf, email, tel]:
			# Algum dos valores não foi preenchido.
			mensagem = "Todos os valores devem ser preenchidos!"
		else:
			if self.buscaCLIENTE(cpf) != None:
				# Existe um produto já cadastrado com o mesmo código
				mensagem = "O cpf informado já foi cadastrado!"
			else:
				p = Pessoa(nome, sobrenome, cpf, email, tel)
				c = Cliente(p)
				self.clientes.append(c)
				mensagem = "Cadastro do cliente realizado com sucesso!"
				retorno.append(c)

		if len(retorno) == 0:
			retorno.append(None) # Houve um erro e o cliente não pôde ser cadastrado.
		
		retorno.append(mensagem)
		
		return retorno

	# ---------------------------------------------------- #

	# Cadastra uma nova conta;
	def cadastrarCONTA(self, numero, cpf, limite, senha, confirmSENHA):
		if '' in [numero, cpf, limite, senha, confirmSENHA]:
			# Algum dos valores não foi preenchido.
			mensagem = "Todos os valores devem ser preenchidos!"
		else:
			c = self.buscaCLIENTE(cpf)
			if c.possuiCONTA != False:
				# O cliente selecionado já possui uma conta.
				mensagem = "Este CPF já possui uma conta"
			else:
				if senha != confirmSENHA:
					# A senha e confirmSENHA não foram digitadas corretamente.
					mensagem = "Senha e confirmação da senha digitadas INCORRETAMENTE!"
				else:
					if limite < 20.00 or limite > 200.00:
						# Limite não aceito. Não vamos aceitar um valor maior que 200 pois não confiamos. kkkk
						mensagem = "Limite com valor não aceito."
					else:
						# Sem problemas, pode cadastrar normalmente.
						self.contas.append(Conta(numero, c, limite, senha))
						c.possuiCONTA = True
						mensagem = "Cadastro realizado com sucesso!"
		return mensagem


	# -------------------------------------------------------------- #

	def efetuarTRANSFERENCIA(self, conta1, cpf2, valor):
		if '' in [cpf2, valor]:
			mensagem = "Todos os valores devem ser preenchidos!"
		else:
			valor1 = float(valor)
			conta2 = self.buscaCONTA_cpf(cpf2)
			if conta2 == None:
				mensagem = "A conta destino não foi encontrada!"
			else:
				if conta1.transfere(conta2, valor1):
					mensagem = "Transferencia realizada com sucesso!"
				else:
					mensagem = "Ocorreu um erro na transferencia"
		return mensagem




