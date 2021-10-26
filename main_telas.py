# main.py

import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import QCoreApplication

from pessoa import Pessoa
from cliente import Cliente
from conta import Conta
from historico import Historico
from principal import DadosCadastros
from tela_cadastrar_conta import Tela_cadastrar_conta
from tela_cadastrar_pessoa import Tela_cadastrar_pessoa
from tela_depositar import Tela_depositar
from tela_extrato import Tela_extrato
from tela_inicial import Tela_inicial
from tela_saque import Tela_saque
from tela_transferencia import Tela_transferencia
from tela_login import Tela_login


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

        #
        self.QtStack.addWidget(self.stack7) 
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

        self.CAD = DadosCadastros()
        self.usuario_logado = Conta()

        self.tela_login.pushButton.clicked.connect(self.fazer_login)
        self.tela_login.pushButton_2.clicked.connect(self.abrir_tela_cadastro_pessoa)

        # Configuação dos botões de cada tela:
        # Funções dos botões da tela:
        
        self.tela_inicial.pushButton_2.clicked.connect(self.BExtrato)
        self.tela_inicial.pushButton_3.clicked.connect(self.abrir_tela_saque)
        self.tela_inicial.pushButton_4.clicked.connect(self.abrir_tela_deposito)
        self.tela_inicial.pushButton_5.clicked.connect(self.abrir_tela_transferir)

        # Funcionalidades dos botões:
        self.tela_cadastrar_pessoa.button_cadastrar.clicked.connect(self.BCadastrarPessoa)
        self.tela_cadastrar_conta.button_cadastrar.clicked.connect(self.BCadastrarConta)
        #self.tela_extrato.Buscar.clicked.connect(self.BExtrato)
        self.tela_saque.button_sacar.clicked.connect(self.BSacar)
        self.tela_depositar.button_depositar.clicked.connect(self.BDepositar)
        self.tela_transferencia.button_transferir.clicked.connect(self.BTransferir)
        
        #self.tela_saque.button_buscar.clicked.connect(self.BBuscar1)
        #self.tela_depositar.button_buscar.clicked.connect(self.BBuscar2)
        self.tela_cadastrar_conta.button_selecionar.clicked.connect(self.BBuscar3)
        
        # Botão de voltar:
        self.tela_inicial.button_voltar.clicked.connect(self.sair)
        self.tela_cadastrar_pessoa.button_voltar.clicked.connect(self.abrir_tela_login)
        self.tela_cadastrar_conta.button_voltar.clicked.connect(self.abrir_tela_cadastro_pessoa)
        self.tela_transferencia.button_voltar.clicked.connect(self.voltar)
        self.tela_saque.button_voltar.clicked.connect(self.voltar)
        self.tela_depositar.button_voltar.clicked.connect(self.voltar)
        self.tela_extrato.button_voltar.clicked.connect(self.voltar)
    
    def fazer_login(self):
        numero = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()
        if numero != '' and senha != '':
            usuario = self.CAD.BuscarConta(numero)
            if(usuario != None):
                self.usuario_logado = None
                self.usuario_logado = usuario
                if(senha == usuario.senha):
                    # Foi digitado a senha correta!
                    self.tela_inicial.label_bem_vindo.setText(f"Bem vindo, {usuario.titular.nome}!")
                    self.QtStack.setCurrentIndex(1)
                else:
                    QMessageBox.information(None,'POOII','Senha incorreta!')
                    self.tela_cadastrar_pessoa.lineEdit_2.setText('')

            else:
                QMessageBox.information(None,'POOII','Conta nao encontrada. Por favor, realize o cadastro antes do login.')
        else:
            QMessageBox.information(None,'POOII','Todos os valores devem ser preenchidos!') 

    #
    def BBuscar1(self):
        cpf = self.tela_saque.lineEdit.text()
        if cpf != '':
            Pessoa = self.CAD.BuscarPessoa(cpf)
            if Pessoa != None:
                QMessageBox.information(None,'POOII','O CPF possui conta!')
            else:
                QMessageBox.information(None,'POOII','O CPF não possui conta!')
        else:
            QMessageBox.information(None,'POOII','O valor deve ser preenchido!')
    
    #
    def BBuscar2(self):
        cpf = self.tela_depositar.lineEdit.text()
        if cpf != '':
            Pessoa = self.CAD.BuscarPessoa(cpf)
            if Pessoa != None:
                QMessageBox.information(None,'POOII','O CPF possui conta!')
            else:
                QMessageBox.information(None,'POOII','O CPF não possui conta!')
        else:
            QMessageBox.information(None,'POOII','O valor deve ser preenchido!') 
    
    #
    def BBuscar3(self):
        cpf = self.tela_cadastrar_conta.lineEdit.text()
        if cpf != '':
            Pessoa = self.CAD.BuscarCPF(cpf)
            if Pessoa != None:
                QMessageBox.information(None,'POOII','Cliente cadastrado!')
            else:
                QMessageBox.information(None,'POOII','Cliente não cadastrado!')
        else:
            QMessageBox.information(None,'POOII','O valor deve ser preenchido!')        
       
    #
    def BCadastrarPessoa(self):
        nome = self.tela_cadastrar_pessoa.lineEdit.text()
        sobrenome = self.tela_cadastrar_pessoa.lineEdit_2.text()
        cpf = self.tela_cadastrar_pessoa.lineEdit_3.text()
        email = self.tela_cadastrar_pessoa.lineEdit_4.text()
        telefone = self.tela_cadastrar_pessoa.lineEdit_5.text()
        
        self.tela_cadastrar_pessoa.lineEdit.setText("")
        self.tela_cadastrar_pessoa.lineEdit_2.setText("")
        self.tela_cadastrar_pessoa.lineEdit_3.setText("")
        self.tela_cadastrar_pessoa.lineEdit_4.setText("")
        self.tela_cadastrar_pessoa.lineEdit_5.setText("")

        if not (nome == '' or sobrenome == '' or cpf == '' or email == '' or telefone == ''):
            C = Cliente(Pessoa(nome, sobrenome, cpf, email, telefone))
            if(self.CAD.CadastrarCliente(C)):
                QMessageBox.information(None,'POOII','Cadastro Realizado com Sucesso!')
                self.tela_cadastrar_conta.lineEdit.setText(C.cpf)
                self.tela_cadastrar_conta.label_5.setText(f'{C.nome} {C.sobrenome}')
                self.QtStack.setCurrentIndex(3)
            else:
                QMessageBox.information(None,'POOII','Esse CPF já foi cadastrado!') 
        else:
            QMessageBox.information(None,'POOII','Todos os valores devem ser preenchidos!') 
    
    #
    def BCadastrarConta(self):
        cpf = self.tela_cadastrar_conta.lineEdit.text()
        limite = self.tela_cadastrar_conta.lineEdit_2.text()
        limite = float(limite)
        numero = self.tela_cadastrar_conta.lineEdit_3.text()
        senha = self.tela_cadastrar_conta.lineEdit_4.text()
        confirmSENHA = self.tela_cadastrar_conta.lineEdit_5.text()
        if not (cpf == '' or limite == '' or numero == '' or senha == '' or confirmSENHA == ''):
            
            if senha == confirmSENHA:
                Pessoa = self.CAD.BuscarCPF(cpf)
                if Pessoa != None:
                    C = Conta(numero,Pessoa,limite,senha)
                    if(self.CAD.AdicionarConta(C)):
                        QMessageBox.information(None,'POOII','Cadastro da Conta Realizada com Sucesso!') 
                        self.tela_cadastrar_conta.lineEdit.setText('')
                        self.tela_cadastrar_conta.lineEdit_2.setText('')
                        self.tela_cadastrar_conta.lineEdit_3.setText('')
                        self.tela_cadastrar_conta.lineEdit_4.setText('')
                        self.tela_cadastrar_conta.lineEdit_5.setText('')
                        self.QtStack.setCurrentIndex(0)
                    else:
                        QMessageBox.information(None,'POOII','Conta existente ou Cliente já tem conta!')
                else:
                    QMessageBox.information(None,'POOII','Operação Inválida!')
            else:
                QMessageBox.information(None,'POOII','Erro na confirmacao de senha, tente novamente.')
        else:
            QMessageBox.information(None,'POOII','Todos os valores devem ser preenchidos!')          
    
    #
    def BExtrato(self):

        self.QtStack.setCurrentIndex(4)
        print(self.usuario_logado.titular.nome)

        nome = self.usuario_logado.titular.nome
        sobrenome = self.usuario_logado.titular.sobrenome
        numero = self.usuario_logado.numero
        saldo = self.usuario_logado.saldo
        limite = self.usuario_logado.limite
        data = self.usuario_logado.historico.data_abertura

        self.tela_extrato.lineEdit.setText(f"{nome} {sobrenome}")
        self.tela_extrato.lineEdit_2.setText(numero)
        self.tela_extrato.lineEdit_3.setText(f"{float(saldo):.2f} R$") 
        self.tela_extrato.lineEdit_4.setText(f"{float(limite):.2f} R$")
        self.tela_extrato.lineEdit_5.setText(f"{data}")


    #
    def BSacar(self):
        self.QtStack.setCurrentIndex(5)
        valor = self.tela_saque.lineEdit_2.text()
        valor1 = float(valor)
        if self.usuario_logado.saca(valor1):
            QMessageBox.information(None,'POOII','Saque efetuado com sucesso!')
            self.tela_saque.lineEdit_2.setText('')
        else:
            QMessageBox.information(None,'POOII','Erro no saque.')
        self.QtStack.setCurrentIndex(1)

    #
    def BDepositar(self):
        valor = self.tela_depositar.lineEdit_2.text()
        valor1 = float(valor)
        if self.usuario_logado.deposita(valor1):
            QMessageBox.information(None,'POOII','Depósito efetuado com sucesso!')
            self.tela_depositar.lineEdit_2.setText('')
        else:
            QMessageBox.information(None,'POOII','Depósito efetuado sem sucesso!')
        self.QtStack.setCurrentIndex(1)

    #
    def BTransferir(self):
        cpf1 = self.tela_transferencia.lineEdit.text()
        cpf2 = self.tela_transferencia.lineEdit_2.text()
        valor = self.tela_transferencia.lineEdit_3.text()
        if cpf1 != '' and cpf2 != '' and valor != '':
            valor1 = float(valor)
            C1 = self.CAD.BuscarPessoa(cpf1)
            C2 = self.CAD.BuscarPessoa(cpf2)
            if C1 != None and C2 != None:
                if C1.transfere(C2,valor1):
                    QMessageBox.information(None,'POOII','Tranferência efetuada com sucesso!')
                    self.tela_transferencia.lineEdit.setText('')
                    self.tela_transferencia.lineEdit_2.setText('')
                    self.tela_transferencia.lineEdit_3.setText('')
                else:
                    QMessageBox.information(None,'POOII','Tranferência efetuada sem sucesso!')
            else:
                    QMessageBox.information(None,'POOII','Tranferência efetuada sem sucesso!')
        else:
            QMessageBox.information(None,'POOII','Todos os valores devem ser preenchidos!') 
    
    #
    def sair(self):
        self.usuario_logado = None
        self.usuario_logado = Conta()
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
