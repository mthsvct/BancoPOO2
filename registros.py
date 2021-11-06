import mysql.connector as mysql
from pessoa import Pessoa
from cliente import Cliente
from conta import Conta
from conexaoBD import ConexaoBD

class Registros:
	__slots__ = ['_clientes','_contas', '_bd']
	
	def __init__(self):
		self._clientes = []
		self._contas = []
		self._bd = ConexaoBD()

	@property
	def clientes(self):
		return self._clientes

	@property
	def contas(self):
		return self._contas

	@property
	def bd(self):
		return self._bd

	# -----------------------BUSCAS-------------------------- #

	# Função que inicializa a classe cliente;
	def montaCLIENTE(self, aux):
		encontrado = None
		if( len(aux) > 0 ):
			# nome, sobrenome, cpf, email, telefone
			print(aux)
			encontrado = Cliente(Pessoa(aux[0][1], aux[0][2], aux[0][0], aux[0][3], aux[0][4]), aux[0][5])
			print(f"encontrado = {encontrado}")
		return encontrado

	# Função que busca um cliente pelo o cpf
	def buscaCLIENTE(self, cpf):
		sql = (f"SELECT * FROM cliente WHERE cpf = {cpf}")
		aux = self.bd.executaSELECT(sql)
		encontrado = self.montaCLIENTE(aux)
		return encontrado

	# Função que inicializa a classe conta;
	def montaCONTA(self, aux):
		encontrado = None
		if( len(aux) > 0 ):
			# nome, sobrenome, cpf, email, telefone
			print(f"montaCONTA aux[0][1] = {aux[0][1]}")
			cliente = self.buscaCLIENTE(aux[0][1])

			print('-' * 50)
			j = 0
			for i in aux[0]:
				print(f'aux[0][{j}] = {i}')
				j += 1

			print('-' * 50)
			encontrado = Conta(aux[0][0], cliente, aux[0][2], aux[0][3], aux[0][4])
			print(f"encontrado em conta = {encontrado}")
		return encontrado

	# Verifica se já possui uma conta com o número buscado
	def buscaCONTA(self, num):
		sql = (f"SELECT * FROM conta WHERE numero = {num}")
		aux = self.bd.executaSELECT(sql)
		encontrado = self.montaCONTA(aux)
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
			print(f"conta login = {conta}")

			if(conta != None):
                # Funcionário existe!
				print(f"Senha = {senha} and conta.senha = {conta.senha}")
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
				sql = (f"INSERT INTO cliente VALUES ('{cpf}', '{nome}', '{sobrenome}', '{email}', '{tel}', 'nao')")
				self.bd.executaALTERACOES(sql)
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
		print("cadastrarCONTA")
		if '' in [numero, cpf, limite, senha, confirmSENHA]:
			# Algum dos valores não foi preenchido.
			mensagem = "Todos os valores devem ser preenchidos!"
		else:
			c = self.buscaCLIENTE(cpf)
			if c.possuiCONTA != 'nao':
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
						print('chegou aqui no cadastro de conta')
						conta_nova = Conta(numero, c, limite, senha)
						#self.contas.append(conta_nova)
						sql = (f"INSERT INTO conta VALUES ({numero}, {c.cpf}, {conta_nova.saldo}, {limite}, {senha})")
						self.bd.executaALTERACOES(sql)
						c.possuiCONTA = 'sim'
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




