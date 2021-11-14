from pessoa import Pessoa
from cliente import Cliente
from conta import Conta
from historico import Historico
from registros import Registros
from conexaoBD import ConexaoBD
import threading
import socket

class ClientThread(threading.Thread):

	def __init__(self, clientAddress, clientsocket):
		threading.Thread.__init__(self)
		
		self.cAddress = clientAddress
		self.csocket = clientsocket
		self.sinc = threading.Lock()
		#self.conexao = None
		#self.serv = None
		self.banco = ConexaoBD()
		self.registros = Registros()
		#self.menu()
		print("Nova conexão: ", clientAddress)

		#self.iniciar()
		#print('')
		#self.menu()


	def recebe_dados(self):
		'''
            Metodo para converter a string recebida em uma lista
		'''
		dados_recebidos = self.csocket.recv(1024).decode()
		dados = list(dados_recebidos.split(';'))
		#print(f'Recebido: {dados} : {type(dados)}')
		return dados

	def enviar_dados(self,dados):
		'''
			Metodo para enviar uma string ao cliente
		'''
		#print(f"dados = {dados}")
		self.csocket.send(str(dados).encode())
		#print("Enviado!")


	def run(self):

		'''
			Indice do Menu:
			[OK] - 1 - login
			[OK] - 2 - Cadastrar cliente
			[OK] - 3 - Cadastrar conta
			[OK] - 4 - Extrato
			[OK] - 5 - Histórico
			[OK] - 6 - Saque
			[OK] - 7 - Depósito
			[OK] - 8 - Transferência <- Fazer depois.
			[OK] - 0 - Fazer o sevridor parar <- fazer depois.
		'''

		# print("chegou aqui!")
        
		while True:
            
			d = self.recebe_dados()

			if d[0]=='1':
				self.login(d)

			elif d[0]=='2':
				self.cadastrar_cliente(d)

			elif d[0]=='3':
				self.cadastrar_conta(d)

			elif d[0]=='4':
				self.extrato(d)

			elif d[0]=='5':
				self.historico(d)

			elif d[0]=='6':
				self.saque(d[1], d[2])

			elif d[0] == '7':
				self.deposito(d[1], d[2])

			elif d[0] == '8':
				self.transferencia(d[1], d[2], d[3]) # cpf1, cpf2, valor.

			else:
				print(f'cliente {self.cAddress} desconectado')
				exit()
				#exit()
				'''
				print('cliente encerrado')
				self.csocket = None
				print('aguardando conexao...')
				con, client = self.serv.accept()
				print(f'Conectado a {client}')
				self.conexao = con
				#break'''


	# Funções seguintes

	# Função que chama as funções de LOGIN
	def login(self, dados):
		retorno = self.registros.fazerLOGIN(dados[1], dados[2])
		if retorno[0] == None:
			resultado = (f'{0};{retorno[1]}')
		else:
			resultado = (f'{1};{retorno[0].numero};{retorno[0].titular.cpf};{retorno[0].titular.nome};{retorno[0].titular.sobrenome}')
		#print(f'Mensagem = {retorno[0]}')
		self.enviar_dados(resultado)


	def cadastrar_cliente(self, dados):
		retorno = self.registros.cadastrarCLIENTE(dados[1], dados[2], dados[3], dados[4], dados[5])
		if retorno[0] == None:
			resultado = (f'{0};{retorno[1]}')
		else:
			resultado = (f'{1};{retorno[1]}')
		self. enviar_dados(resultado)

    
	def cadastrar_conta(self, dados):
		# def cadastrarCONTA(self,numero,cpf,limite,senha,confirmSENHA)
		#print(dados)
		retorno = self.registros.cadastrarCONTA(dados[1], dados[2], dados[3], dados[4], dados[5])
		#print(f"retorno.cadastrar_conta = {retorno}")
		if retorno[0] == 1:
			resultado = (f'{0};{retorno[1]}')
		else:
			resultado = (f'{1};{retorno[1]}')
		self.enviar_dados(resultado)


	def extrato(self, dados):
		c = self.registros.buscaCONTA(dados[1])
		if c == None:
			resultado = (f'{0};A conta buscada não foi encontrada!')
		else:
			resultado = (f'{1};{c.saldo};{c.limite}')
		self.enviar_dados(resultado)


	def historico(self, dados):
		esse = self.registros.buscaCONTA(dados[1])
		if esse == None:
			resultado = (f'{0};A conta buscada não foi encontrada!')
		else:
			mensagem = self.registros.pegaHISTORICO(esse)
			h = ''
			for i in range(0, len(mensagem)):
				h = h + (f"{mensagem[i][1]} - {mensagem[i][2]} \n\n")
			resultado = (f'{1};{h}')
		self.enviar_dados(resultado)


	def saque(self, cpf, valor):
		self.sinc.acquire()
		if '' in [cpf, valor]:
			resultado = (f'{0};Não foi possível realizar o saque!')
		else:
			s = self.registros.EfetuarSAQUE(cpf, valor)
			resultado = (f'{1};{s}')
		self.sinc.release()
		self.enviar_dados(resultado)


	def deposito(self, cpf, valor):
		self.sinc.acquire()
		if '' in [cpf, valor]:
			resultado = (f'{0};Não foi possível realizar o deposito!')
		else:
			d = self.registros.EfetuarDEPOSITAR(cpf, valor)
			resultado = (f'{1};{d}')
		self.sinc.release()
		self.enviar_dados(resultado)


	def transferencia(self, cpf1, cpf2, valor):
		self.sinc.acquire()
		if '' in [cpf1, cpf2, valor]:
			resultado = (f'{0};Nao foi possivel realizar a transferencia!')
		else:
			t = self.registros.EfetuarTRANSFERENCIA(cpf1, cpf2, valor)
			resultado = (f'{1};{t}')
		self.sinc.release()
		self.enviar_dados(resultado)

