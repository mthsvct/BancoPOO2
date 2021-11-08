import socket
import sys
from pessoa import Pessoa
from cliente import Cliente
from conta import Conta
from historico import Historico
from registros import Registros
from conexaoBD import ConexaoBD
import pdb

class Servidor():
    '''
    Classe que representa o servidor do banco
    '''
    def __init__(self):
        self.conexao = None
        self.serv = None
        self.banco = ConexaoBD()
        self.registros = Registros()
        self.iniciar()
        print('')
        self.menu()

    def iniciar(self):
        '''
            Metodo que inicia a conexao do servidor
        '''
        host = 'localhost'
        port = 8000
        addr = (host, port)
        serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        serv_socket.bind(addr)
        serv_socket.listen(10)
        print('aguardando conexao...')
        con, client = serv_socket.accept()
        print(f'Conectado a {client}')
        self.conexao = con
        self.serv = serv_socket

    
    def recebe_dados(self):
        '''
            Metodo para converter a string recebida em uma lista
        '''
        dados_recebidos = self.conexao.recv(1024).decode()
        dados = list(dados_recebidos.split(';'))
        print(f'Recebido: {dados} : {type(dados)}')
        return dados
    

    def enviar_dados(self,dados):
        '''
            Metodo para enviar uma string ao cliente
        '''
        print(f"dados = {dados}")
        self.conexao.send(str(dados).encode())
        print("Enviado!")
        

    def menu(self):



        '''
            Metodo que recebe dados de um cliente e chama um metodo de acordo com o primeiro item:
            1 - login
            2 - Cadastrar cliente
            3 - Cadastrar conta
            4 - Extrato
            5 - Histórico
            6 - Saque
            7 - Depósito


        '''
        print("chegou aqui!")
        
        i = 0
        while True:
            d = self.recebe_dados()
            #print(f'd = {d}')
            if d[0]=='1':
                #print('MENU -> Login')
                self.login(d)

            elif d[0]=='2':
                self.cadastrar_cliente(d)

            elif d[0]=='3':
                #print("---->cadastrar_conta")
                self.cadastrar_conta(d)

            elif d[0]=='4':
                self.extrato(d)

            elif d[0]=='5':
                self.historico(d)

            elif d[0]=='6':
                self.saque(d[1], d[2])

            elif d[0]=='7':
                self.deposito(d[1], d[2])

            else:
                print('cliente encerrado')
                self.conexao = None
                print('aguardando conexao...')
                con, client = self.serv.accept()
                print(f'Conectado a {client}')
                self.conexao = con
                    #break


                '''

                elif d[0]=='4':
                    #self.saque(d)
                elif d[0]=='5':
                    #self.extrato()
                elif d[0]=='6':
                    #self.transferencia(d)

            except:
                print('cliente encerrado')
                self.conexao = None
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
        print(f'Mensagem = {retorno[0]}')
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
        if '' in [cpf, valor]:
            resultado = (f'{0};Não foi possível realizar o saqu!')
        else:
            s = self.registros.EfetuarSAQUE(cpf, valor)
            resultado = (f'{1};{s}')
        self.enviar_dados(resultado)


    def deposito(self, cpf, valor):
        if '' in [cpf, valor]:
            resultado = (f'{0};Não foi possível realizar o saqu!')
        else:
            d = self.registros.EfetuarDEPOSITAR(cpf, valor)
            resultado = (f'{1};{d}')
        self.enviar_dados(resultado)