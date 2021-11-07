import mysql.connector as mysql
import datetime
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
			# print(aux)
			encontrado = Cliente(Pessoa(aux[0][1], aux[0][2], aux[0][0], aux[0][3], aux[0][4]), aux[0][5])
			# print("encontrado = {encontrado}")
		return encontrado

	# Função que busca um cliente pelo o CPF.
	def buscaCLIENTE(self,cpf):
		sql = ("SELECT * FROM cliente WHERE cpf = '%s'" %(cpf))
		aux = self.bd.executaSELECT(sql)
		encontrado = self.montaCLIENTE(aux)
		return encontrado

	# Função que inicializa a classe conta;
	def montaCONTA(self,aux):
		encontrado = None
		# print(aux)
		if(len(aux) > 0 ):
			# nome, sobrenome, cpf, email, telefone
			# print(f"montaCONTA aux[0][1] = {aux[0][1]}")
			cliente = self.buscaCLIENTE(aux[0][1])
			
			"""
			print('-' * 50)
			j = 0
			for i in aux[0]:
				print(f'aux[0][{j}] = {i}')
				j += 1
			print('-' * 50)
			"""
			encontrado = Conta(aux[0][0],cliente,aux[0][2],aux[0][3],aux[0][4])
			# print(f"encontrado em conta = {encontrado}")
		return encontrado

	# Verifica se já possui uma conta com o número buscado...
	def buscaCONTA(self,cpf):
		sql = ("SELECT * FROM conta WHERE cpf_cliente = '%s'"%(cpf))
		aux = self.bd.executaSELECT(sql)
		encontrado = self.montaCONTA(aux)
		return encontrado



	# Busca um conta pelo o CPF:
	def buscaCONTA_num(self,num):
		sql = ("SELECT * FROM conta WHERE numero = '%s'"%(num))
		aux = self.bd.executaSELECT(sql)
		encontrado = self.montaCONTA(aux)
		return encontrado

	# --------------------------------------------------------------------- #
	# Retorna uma lista contendo:
	# Retorna o usuário caso seja digitado os dados corretamente, caso contrário retorna retorna None;
	# Junto com o usuário ou None é retornado uma mensagem.
	def fazerLOGIN(self, num, senha):

		logado = []

		if num != '' and senha != '':
			# todos os campos foram preenchidos
			
			conta = self.buscaCONTA_num(num) # busca o usuário na lista de funcionarios cadastrados.
			print(f"conta login = {conta}")

			sql = ("SELECT * FROM conta WHERE numero = '%s' AND senha = MD5('%s')" %(num,senha))
			Aqui = self.bd.executaSELECT(sql)
			conta = self.montaCONTA(Aqui)
			if(conta != None):
                # Funcionário existe!
				mensagem = ("Bem vindo, "+conta.titular.nome+"!")
				logado.append(conta)
              
			else:
				# O funcionário não existe.
				mensagem = "Conta não encontrada ou senha incorreta. \nPor favor, efetue o cadastro antes do login."
		else:
			mensagem = "Todos os valores devem ser preenchidos!"

		if( len(logado) == 0 ):
			logado.append(None)
        	
		logado.append(mensagem)

		return logado


	# Função que verifica se não há CPFs repetidos e cria um objeto pessoa:
	def cadastrarCLIENTE(self,nome,sobrenome,cpf,email,tel):
		retorno = []
		if '' in [nome,sobrenome,cpf,email,tel]:
			# Algum dos valores não foi preenchido.
			mensagem = "Todos os valores devem ser preenchidos!"
		else:
			if self.buscaCLIENTE(cpf) != None:
				# Existe um produto já cadastrado com o mesmo código
				mensagem = "O CPF informado já foi cadastrado!"
			else:
				p = Pessoa(nome,sobrenome,cpf,email,tel)
				s = "Não"
				sql = ("INSERT INTO cliente(cpf,nome,sobrenome,email,telefone,possui_conta) VALUES ('%s','%s','%s','%s','%s','%s')" %(cpf,nome,sobrenome,email,tel,s))
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
	def cadastrarCONTA(self,numero,cpf,limite,senha,confirmSENHA):
		# print("cadastrarCONTA")
		if '' in [numero, cpf, limite, senha, confirmSENHA]:
			# Algum dos valores não foi preenchido.
			mensagem = "Todos os valores devem ser preenchidos!"
		else:
			c = self.buscaCLIENTE(cpf)
			if c.possuiCONTA == 'Sim':
				# O cliente selecionado já possui uma conta.
				mensagem = "Este CPF já possui uma conta!"
			else:
				if senha != confirmSENHA:
					# A senha e confirmSENHA não foram digitadas corretamente.
					mensagem = "Senha e confirmação da senha digitadas INCORRETAMENTE!"
				else:
					if limite < 20.00 or limite > 1000.00:
						# Limite não aceito. Não vamos aceitar um valor maior que 200 pois não confiamos. (Banco pequeno.)
						mensagem = "Limite com valor não aceito."
					else:
						# Sem problemas, pode cadastrar normalmente.
						# print('Chegou aqui no cadastro de conta.')
						conta_nova = Conta(numero,c,0,limite,senha)
						#self.contas.append(conta_nova)
						sql = ("INSERT INTO conta(numero,cpf_cliente,saldo,limite,senha) VALUES ('%s','%s','%f','%f',MD5('%s'))" %(numero,c.cpf,conta_nova.saldo,limite,senha))
						self.bd.executaALTERACOES(sql)
						c.possuiCONTA = 'Sim'
						data = datetime.date.today()
						info= ("Criação da conta realizada.")
						sql = ("INSERT INTO historico(conta_num,data,descricao) VALUES ('%s','%s','%s')" %(numero,data,info))
						self.bd.executaALTERACOES(sql)
						sql = ("UPDATE cliente SET possui_conta = '%s' WHERE cpf = '%s'" %("Sim",c.cpf))
						self.bd.executaALTERACOES(sql)
						mensagem = "Cadastro realizado com sucesso!"
		return mensagem


	# -------------------------------------------------------------- #	
	"""
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
	"""
	
	def EfetuarDEPOSITAR(self,cpf,depos):
		if '' in [cpf,depos]:
			mensagem = "Todos os valores devem ser preenchidos!"
		else:
			valor = float(depos)
			Encontrado = self.buscaCONTA(cpf)
			sql = ("SELECT saldo FROM conta WHERE cpf_cliente = '%s'" %(Encontrado.titular.cpf))
			Aqui = self.bd.executaSELECT(sql)
			saldo = float(Aqui[0][0])
			if(saldo+valor <= Encontrado.limite):
				sql = ("UPDATE conta SET saldo = '%f' WHERE cpf_cliente = '%s'" %(saldo+valor,Encontrado.titular.cpf))	
				self.bd.executaALTERACOES(sql)
				mensagem = "Depósito realizado com sucesso!"
				data = datetime.date.today()
				info = ("Depósito realizado de %.2f R$." %valor)
				sql = ("INSERT INTO historico(conta_num,data,descricao) VALUES ('%s','%s','%s')" %(Encontrado.numero,data,info))
				self.bd.executaALTERACOES(sql)
			else:
				data = datetime.date.today()
				info = ("Tentativa de depósito de %.2f R$ recusada." %valor)
				sql = ("INSERT INTO historico(conta_num,data,descricao) VALUES ('%s','%s','%s')" %(Encontrado.numero,data,info))
				self.bd.executaALTERACOES(sql)
				mensagem = "Depósito realizado sem sucesso!"
		return mensagem
	
	def EfetuarSAQUE(self,cpf,saque):
		if '' in [cpf,saque]:
			mensagem = "Todos os valores devem ser preenchidos!"
		else:
			valor = float(saque)
			Encontrado = self.buscaCONTA(cpf)
			sql = ("SELECT saldo FROM conta WHERE cpf_cliente = '%s'" %(Encontrado.titular.cpf))
			Aqui = self.bd.executaSELECT(sql)
			saldo = float(Aqui[0][0])
			if(saldo >= valor ):
				sql = ("UPDATE conta SET saldo = '%f' WHERE cpf_cliente = '%s'" %(saldo-valor,Encontrado.titular.cpf))	
				self.bd.executaALTERACOES(sql)
				data = datetime.date.today()
				info= ("Saque realizado de %.2f R$." %valor)
				sql = ("INSERT INTO historico(conta_num,data,descricao) VALUES ('%s','%s','%s')" %(Encontrado.numero,data,info))
				self.bd.executaALTERACOES(sql)
				mensagem = "Saque realizado com sucesso!"
			else:
				data = datetime.date.today()
				info = ("Tentativa de saque de %.2f R$ recusada." %valor)
				sql = ("INSERT INTO historico(conta_num,data,descricao) VALUES ('%s','%s','%s')" %(Encontrado.numero,data,info))
				self.bd.executaALTERACOES(sql)
				mensagem = "Saque realizado sem sucesso!"
		return mensagem
	
	def EfetuarTRANSFERENCIA(self,cpf,destino,transf):
		if '' in [cpf,destino,transf]:
			mensagem = "Todos os valores devem ser preenchidos!"
		else:
			valor = float(transf)
			Encontrado = self.buscaCONTA(cpf)
			Encontrado2 = self.buscaCONTA(destino)
			sql = ("SELECT saldo FROM conta WHERE cpf_cliente = '%s'" %(Encontrado.titular.cpf))
			Aqui = self.bd.executaSELECT(sql)
			saldo = float(Aqui[0][0])
			if(saldo >= valor ):
				sql = ("SELECT saldo FROM conta WHERE cpf_cliente = '%s'" %(Encontrado2.titular.cpf))
				Aqui = self.bd.executaSELECT(sql)
				saldo2 = float(Aqui[0][0])
				if(saldo2+valor <= Encontrado2.limite):
					sql = ("UPDATE conta SET saldo = '%f' WHERE cpf_cliente = '%s'" %(saldo2+valor,Encontrado2.titular.cpf))
					sql2 = ("UPDATE conta SET saldo = '%f' WHERE cpf_cliente = '%s'" %(saldo-valor,Encontrado.titular.cpf))	
					self.bd.executaALTERACOES(sql)
					self.bd.executaALTERACOES(sql2)		
					data = datetime.date.today()
					info = ("Transferência realizada de %.2f R$ para a conta de número (%s)." %(valor,Encontrado2.numero))
					sql = ("INSERT INTO historico(conta_num,data,descricao) VALUES ('%s','%s','%s')" %(Encontrado.numero,data,info))
					self.bd.executaALTERACOES(sql)
					info = ("Transferência recebida de %.2f R$ da conta de número (%s)." %(valor,Encontrado.numero))
					sql = ("INSERT INTO historico(conta_num,data,descricao) VALUES ('%s','%s','%s')" %(Encontrado2.numero,data,info))
					self.bd.executaALTERACOES(sql)
					mensagem = "Transferência realizada com sucesso!"
			else:
				data = datetime.date.today()
				info = ("Tentativa de transferência de %.2f R$ recusada." %valor)
				sql = ("INSERT INTO historico(conta_num,data,descricao) VALUES ('%s','%s','%s')" %(Encontrado.numero,data,info))
				self.bd.executaALTERACOES(sql)
				mensagem = "Transferência realizada sem sucesso!"
		return mensagem

# self,nome,sobrenome,cpf,email,tel
# numero,cpf,limite,senha,confirmSENHA

"""
R = Registros()
R.cadastrarCLIENTE("Vinicius","Dias","33469298092","viniciusdias@ufpi.edu.br","999473-2624")
R.cadastrarCLIENTE("Matheus","Victor","61206747307","matheusvictor@ufpi.edu.br","999126-7703")
R.cadastrarCONTA("145-60","33469298092",50.00,"AzulDCDM","AzulDCDM")
R.cadastrarCONTA("754-00","61206747307",500.00,"ToLove","ToLove")
R.EfetuarDEPOSITAR("33469298092",20.00)
R.EfetuarDEPOSITAR("33469298092",20.00)
R.EfetuarTRASFERENCIA("33469298092","61206747307",40.00)
R.EfetuarTRASFERENCIA("33469298092","61206747307",700.00)
"""
