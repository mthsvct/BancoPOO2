# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_extrato.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

regula = -30

class Tela_extrato(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(250, 40, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 185+regula, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 210+regula, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 235+regula, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 260+regula, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 285+regula, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 180+regula, 311, 23))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 205+regula, 311, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 230+regula, 311, 23))
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 255+regula, 311, 23))
        self.lineEdit_4.setObjectName("lineEdit_4")
        
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(250, 280+regula, 311, 23))
        self.lineEdit_5.setObjectName("lineEdit_5")
        
        self.button_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.button_voltar.setGeometry(QtCore.QRect(270, 340, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_voltar.setFont(font)
        self.button_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_voltar.setObjectName("button_voltar")
        '''self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(250, 180, 311, 23))
        self.lineEdit_7.setObjectName("lineEdit_7")'''
        '''self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 100, 141, 16))'''
        font = QtGui.QFont()
        font.setPointSize(12)
        #self.label_7.setFont(font)
        #self.label_7.setObjectName("label_7")
        '''self.Buscar = QtWidgets.QPushButton(self.centralwidget)
        self.Buscar.setGeometry(QtCore.QRect(320, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Buscar.setFont(font)
        self.Buscar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Buscar.setObjectName("Buscar")'''
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo.setText(_translate("MainWindow", "EXTRATO"))
        self.label_2.setText(_translate("MainWindow", "NOME:"))
        self.label_3.setText(_translate("MainWindow", "Nº da CONTA:"))
        self.label_4.setText(_translate("MainWindow", "SALDO:"))
        self.label_5.setText(_translate("MainWindow", "LIMITE:"))
        self.label_6.setText(_translate("MainWindow", "DATA DE CRIAÇAO: "))
        self.button_voltar.setText(_translate("MainWindow", "Voltar"))
        #self.label_7.setText(_translate("MainWindow", "Nº da CONTA:"))
        #self.Buscar.setText(_translate("MainWindow", "Buscar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_extrato()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
