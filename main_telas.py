# main.py

import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import QCoreApplication

from tela_inicial import Tela_inicial
from tela_cadastrar_pessoa import Tela_cadastrar_pessoa
from tela_cadastrar_conta import Tela_cadastrar_conta
from tela_depositar import Tela_depositar
from tela_extrato import Tela_extrato
from tela_saque import Tela_saque
from tela_transferencia import Tela_transferencia
from historico import Historico
from cliente import Cliente
from conta import Conta
from principal import DadosCadastros


class Ui_Main(QtWidgets.QWidget):
    
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(640,480) # definição do tamanho da tela

        # Criação das pilhas
        self.QtStack = QtWidgets.QStackedLayout()
        
        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()

        # criação do objeto para cada tela
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

        # 
        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)

class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        # configuação dos botões de cada tela:
        # funções dos botões da tela
        self.tela_inicial.pushButton.clicked.connect( self.abrir_tela_cadastro_pessoa )
        self.tela_inicial.pushButton_2.clicked.connect( self.abrir_tela_cadastro_conta )
        self.tela_inicial.pushButton_3.clicked.connect( self.abrir_tela_extrato )
        self.tela_inicial.pushButton_4.clicked.connect( self.abrir_tela_saque )
        self.tela_inicial.pushButton_5.clicked.connect( self.abrir_tela_deposito )
        self.tela_inicial.pushButton_6.clicked.connect( self.abrir_tela_transferir )

        # Botão de voltar:
        self.tela_cadastrar_pessoa.button_voltar.clicked.connect( self.voltar )
        self.tela_cadastrar_conta.button_voltar.clicked.connect( self.voltar )
        self.tela_transferencia.button_voltar.clicked.connect( self.voltar )
        self.tela_saque.button_voltar.clicked.connect( self.voltar )
        self.tela_depositar.button_voltar.clicked.connect( self.voltar )
        self.tela_extrato.button_voltar.clicked.connect( self.voltar )


    def voltar(self):
        self.QtStack.setCurrentIndex(0)

    def abrir_tela_cadastro_pessoa(self):
        self.QtStack.setCurrentIndex(1)

    def abrir_tela_cadastro_conta(self):
        self.QtStack.setCurrentIndex(2)

    def abrir_tela_extrato(self):
        self.QtStack.setCurrentIndex(3)

    def abrir_tela_saque(self):
        self.QtStack.setCurrentIndex(4)

    def abrir_tela_deposito(self):
        self.QtStack.setCurrentIndex(5)

    def abrir_tela_transferir(self):
        self.QtStack.setCurrentIndex(6)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())





