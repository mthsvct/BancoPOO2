import socket
import sys
from pessoa import Pessoa
from cliente import Cliente
from conta import Conta
from historico import Historico
from registros import Registros
from conexaoBD import ConexaoBD
import pdb

from multithread import ClientThread

class Servidor():
    '''
    Classe que representa o servidor do banco
    '''
    def __init__(self):
        self.run()
        '''
        self.conexao = None
        self.serv = None
        self.banco = ConexaoBD()
        self.registros = Registros()
        self.iniciar()
        print('')
        self.menu()
        '''


    def run(self):
        host = 'localhost'
        port = 8000
        addr = (host, port)
        serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        serv_socket.bind(addr)
        print('servidor iniciado')
        print('aguardando nova conexão...')
        while True:
            serv_socket.listen(1)
            clientsock, clienteAddress = serv_socket.accept()
            newthread = ClientThread(clienteAddress,clientsock)
            newthread.start()



    '''
    def iniciar(self):
        # Metodo que inicia a conexao do servidor
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
        self.serv = serv_socket'''


if __name__ == '__main__':
    servidor = Servidor()
    sys.exit()