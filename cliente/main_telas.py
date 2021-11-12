# main.py

import sys
import os
import datetime
import socket

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import QCoreApplication

from tela_cadastrar_conta import Tela_cadastrar_conta
from tela_cadastrar_pessoa import Tela_cadastrar_pessoa
from tela_depositar import Tela_depositar
from tela_extrato import Tela_extrato
from tela_inicial import Tela_inicial
from tela_saque import Tela_saque
from tela_transferencia import Tela_transferencia
from tela_login import Tela_login
from tela_apresentar_historico import Tela_apresentar_historico


class Ui_Main(QtWidgets.QWidget):
    
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(640,480) # definição do tamanho da tela

        # Criação das pilhas de interfaces.
        self.QtStack = QtWidgets.QStackedLayout() 
        
        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()

        # Criação do objeto para cada tela
        self.tela_inicial = Tela_inicial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastrar_pessoa = Tela_cadastrar_pessoa()
        self.tela_cadastrar_pessoa.setupUi(self.stack1)

        self.tela_cadastrar_conta = Tela_cadastrar_conta()
        self.tela_cadastrar_conta.setupUi(self.stack2)

        self.tela_extrato = Tela_extrato()
        self.tela_extrato.setupUi(self.stack3)

        self.tela_saque = Tela_saque()
        self.tela_saque.setupUi(self.stack4)

        self.tela_depositar = Tela_depositar()
        self.tela_depositar.setupUi(self.stack5)

        self.tela_transferencia = Tela_transferencia()
        self.tela_transferencia.setupUi(self.stack6)

        self.tela_login = Tela_login()
        self.tela_login.setupUi(self.stack7)

        self.tela_apresentar_historico = Tela_apresentar_historico()
        self.tela_apresentar_historico.setupUi(self.stack8)

        #
        self.QtStack.addWidget(self.stack7) 
        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack8)

class Main(QMainWindow, Ui_Main):
    
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        #self.CAD = Registros()
        #self.logado = Conta()

        self.logado = []

        self.conta_atual = None
        self.conexao = None

        self.tela_login.pushButton.clicked.connect(self.botaoENTRAR)
        self.tela_login.pushButton_2.clicked.connect(self.abrir_tela_cadastro_pessoa)

        # Configuação dos botões de cada tela:
        # Funções dos botões da tela:
        self.tela_inicial.pushButton_2.clicked.connect(self.botaoEXTRATO)
        self.tela_inicial.pushButton_3.clicked.connect(self.abrir_tela_saque)
        self.tela_inicial.pushButton_4.clicked.connect(self.abrir_tela_deposito)
        self.tela_inicial.pushButton_5.clicked.connect(self.abrir_tela_transferir)

        # Funcionalidades dos botões:
        self.tela_extrato.button_historico.clicked.connect(self.botaoHISTORICO)
        self.tela_cadastrar_pessoa.button_cadastrar.clicked.connect(self.botaoCADASTRAR_pessoa)
        self.tela_cadastrar_conta.button_cadastrar.clicked.connect(self.botaoCADASTRAR_conta)
        self.tela_saque.button_sacar.clicked.connect(self.botaoSACAR)
        self.tela_depositar.button_depositar.clicked.connect(self.botaoDEPOSITAR)
        self.tela_transferencia.button_transferir.clicked.connect(self.botaoTRANSFERIR)

        
        # Botão de voltar:
        self.tela_inicial.button_voltar.clicked.connect(self.sair)
        self.tela_cadastrar_pessoa.button_voltar.clicked.connect(self.abrir_tela_login)
        self.tela_cadastrar_conta.button_voltar.clicked.connect(self.abrir_tela_cadastro_pessoa)
        self.tela_transferencia.button_voltar.clicked.connect(self.voltar)
        self.tela_saque.button_voltar.clicked.connect(self.voltar)
        self.tela_depositar.button_voltar.clicked.connect(self.voltar)
        self.tela_extrato.button_voltar.clicked.connect(self.voltar)
        self.tela_apresentar_historico.voltar.clicked.connect(self.botaoEXTRATO)
    
        self.conectar()
    

    #
    def sair(self):
        dados = (f'{0};Sair')
        self.enviar_dados(dados)
        self.logado = []
        self.tela_login.lineEdit.setText("")
        self.tela_login.lineEdit_2.setText("")
        self.QtStack.setCurrentIndex(0)


    def abrir_tela_login(self):
        self.tela_login.lineEdit.setText("")
        self.tela_login.lineEdit_2.setText("")
        self.QtStack.setCurrentIndex(0)

    def voltar(self):
        self.QtStack.setCurrentIndex(1)

    def abrir_tela_cadastro_pessoa(self):
        self.QtStack.setCurrentIndex(2)

    def abrir_tela_cadastro_conta(self):
        self.QtStack.setCurrentIndex(3)

    def abrir_tela_extrato(self):
        self.QtStack.setCurrentIndex(4)

    def abrir_tela_saque(self):
        self.QtStack.setCurrentIndex(5)

    def abrir_tela_deposito(self):
        self.QtStack.setCurrentIndex(6)

    def abrir_tela_transferir(self):
        self.QtStack.setCurrentIndex(7)

    def abrir_tela_apresentar_historico(self):
        self.QtStack.setCurrentIndex(8)


    #iniciar conexao
    def conectar(self):
        '''
        :return:
            vai iniciar a conexao das telas com o servidor
        '''
        ip = 'localhost'
        port = 8000
        addr = ((ip,port))
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente_socket.connect(addr)
        self.conexao = cliente_socket

    def enviar_dados(self,dados):
        '''
        :param dados:
            vai enviar uma string para o servidor
        :return:
        '''
        self.conexao.send(dados.encode())
        #print("Enviado!")
        #except:
        #print('Erro')

    def receber_dados(self):
        '''
        :return:
            o servidor recebe os dados e retorna uma lista
        '''

        dados_recebidos = self.conexao.recv(1024).decode()
        #print(f"dados_recebidos = {dados_recebidos}")
        dados = dados_recebidos.split(';')
        #print(type(dados))
        #print("Recebido!")
        return dados
        
        #except:
            #print('Erro')

    # Função que é acionada quando o usuário clica no botão de entrar na tela de login:
    def botaoENTRAR(self):
        numero = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()
        dados = (f"{1};{numero};{senha}")
        
        #print(f"dados = {dados}")
        self.enviar_dados(dados)

        resposta = self.receber_dados()
        #print("CHEGOU AQUI *")

        #print(f"resposta = {resposta}")

        if resposta[0] != '0':
            self.logado = resposta
            self.tela_inicial.label_bem_vindo.setText(f"Bem vindo, {resposta[3]}!")
            self.QtStack.setCurrentIndex(1)
        else:
            QMessageBox.information(None,'POOII',resposta[1])
        
        self.tela_login.lineEdit.setText("")
        self.tela_login.lineEdit_2.setText("")


    # Função que é acionada quando o usuário clica no botão cadastrar na tela de cadastro de pessoas:
    def botaoCADASTRAR_pessoa(self):
        nome = self.tela_cadastrar_pessoa.lineEdit.text()
        sobrenome = self.tela_cadastrar_pessoa.lineEdit_2.text()
        cpf = self.tela_cadastrar_pessoa.lineEdit_3.text()
        email = self.tela_cadastrar_pessoa.lineEdit_4.text()
        telefone = self.tela_cadastrar_pessoa.lineEdit_5.text()
        
        dados = (f'{2};{nome};{sobrenome};{cpf};{email};{telefone}')
        self.enviar_dados(dados)
        resposta = self.receber_dados()


        #retorno = self.CAD.cadastrarCLIENTE(nome,sobrenome,cpf,email,telefone)
        
        if resposta[0] != '0':
            self.tela_cadastrar_conta.lineEdit.setText(cpf)
            self.tela_cadastrar_conta.label_5.setText(f'{nome} {sobrenome}')
            self.QtStack.setCurrentIndex(3) # Abre a tela de cadastro de conta.
        else:
            QMessageBox.information(None,'POOII',f'{resposta[1]}')

        self.tela_cadastrar_pessoa.lineEdit.setText('')
        self.tela_cadastrar_pessoa.lineEdit_2.setText('')
        self.tela_cadastrar_pessoa.lineEdit_3.setText('')
        self.tela_cadastrar_pessoa.lineEdit_4.setText('')
        self.tela_cadastrar_pessoa.lineEdit_5.setText('')


    # Função que é acionada quando o usuário clica no botão cadastrar na tela de cadastro de contas:
    def botaoCADASTRAR_conta(self):
        cpf = self.tela_cadastrar_conta.lineEdit.text()
        limite = self.tela_cadastrar_conta.lineEdit_2.text()
        limite = float(limite)
        numero = self.tela_cadastrar_conta.lineEdit_3.text()
        senha = self.tela_cadastrar_conta.lineEdit_4.text()
        confirmSENHA = self.tela_cadastrar_conta.lineEdit_5.text()

        dados = (f'{3};{numero};{cpf};{limite};{senha};{confirmSENHA}')
        self.enviar_dados(dados)
        resposta = self.receber_dados()
        #QMessageBox.information(None,'POOII',f'{resposta[1]}')

        #mensagem = self.CAD.cadastrarCONTA(numero,cpf,limite,senha,confirmSENHA)
        self.QtStack.setCurrentIndex(0)

        self.tela_cadastrar_conta.lineEdit.setText('')
        self.tela_cadastrar_conta.lineEdit_2.setText('')
        self.tela_cadastrar_conta.lineEdit_3.setText('')
        self.tela_cadastrar_conta.lineEdit_4.setText('')
        self.tela_cadastrar_conta.lineEdit_5.setText('')

    # Função que é acionada quando o usuário clica no botão de extrato na tela de inicio.
    def botaoEXTRATO(self):
        
        self.tela_extrato.lineEdit.setText("")
        self.tela_extrato.lineEdit_2.setText("")
        self.tela_extrato.lineEdit_3.setText("") 
        self.tela_extrato.lineEdit_4.setText("")
        #self.tela_extrato.lineEdit_5.setText("")

        self.QtStack.setCurrentIndex(4) # Abre a tela de extrato
        dados = (f'{4};{self.logado[2]}') # Busca o CPF
        self.enviar_dados(dados)
        resposta = self.receber_dados()

        # print(self.logado.titular.nome)
        #Esse = self.CAD.buscaCONTA(self.logado.titular.cpf)
        if resposta[0] != '0':
            numero = self.logado[1]
            nome = self.logado[3]
            sobrenome = self.logado[4]
            saldo = resposta[1]
            limite = resposta[2]
            # data = self.logado.historico.data_abertura

            self.tela_extrato.lineEdit.setText(f"{nome} {sobrenome}")
            self.tela_extrato.lineEdit_2.setText(numero)
            self.tela_extrato.lineEdit_3.setText(f"{float(saldo):.2f} R$") 
            self.tela_extrato.lineEdit_4.setText(f"{float(limite):.2f} R$")
            #self.tela_extrato.lineEdit_5.setText(f"{data}")
        else:
            QMessageBox.information(None,'POOII',f'{resposta[1]}')


    # Função que é acionada quando o usuário clica no botão de histórico na tela de extrato.
    def botaoHISTORICO(self):
        self.QtStack.setCurrentIndex(8)

        dados = (f'{5};{self.logado[2]}') # Mandei o CPF
        self.enviar_dados(dados)
        resposta = self.receber_dados()


        if resposta[0] != '0':
            self.tela_apresentar_historico.textBrowser.setText(resposta[1])
        else:
            QMessageBox.information(None,'POOII',f'{resposta[1]}')


    # Função que é acionada quando o usuário clica no botão de saque na tela de saque.
    def botaoSACAR(self):
        valor = self.tela_saque.lineEdit_2.text()
        dados = (f'{6};{self.logado[2]};{valor}') # Manda o CPF e valor
        self.enviar_dados(dados)
        resposta = self.receber_dados()
        QMessageBox.information(None,'POOII',f'{resposta[1]}')
        self.tela_saque.lineEdit_2.setText('')


    # Função que é acionada quando o usuário clica no botão de deposito na tela de depósito.
    def botaoDEPOSITAR(self):
        valor = self.tela_depositar.lineEdit_2.text()
        dados = (f'{7};{self.logado[2]};{valor}') # Manda o CPF e valor
        self.enviar_dados(dados)
        resposta = self.receber_dados()
        QMessageBox.information(None,'POOII',f'{resposta[1]}')
        self.tela_depositar.lineEdit_2.setText('')
        

    # Função que é acionada quando o usuário clica no botão transferir na tela de transferência.
    def botaoTRANSFERIR(self):
        cpf2 = self.tela_transferencia.lineEdit_2.text()
        valor = self.tela_transferencia.lineEdit_3.text()
        dados = (f'{8};{self.logado[2]};{cpf2};{valor}')
        
        self.enviar_dados(dados)
        resposta = self.receber_dados()

        QMessageBox.information(None,'POOII',f'{resposta[1]}')
        
        self.tela_transferencia.lineEdit_2.setText('')
        self.tela_transferencia.lineEdit_3.setText('')   
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
