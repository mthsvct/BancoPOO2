# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_depositar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_depositar(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(230, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.button_depositar = QtWidgets.QPushButton(self.centralwidget)
        self.button_depositar.setGeometry(QtCore.QRect(260, 265, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_depositar.setFont(font)
        self.button_depositar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_depositar.setObjectName("button_depositar")
        self.button_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.button_voltar.setGeometry(QtCore.QRect(260, 305, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_voltar.setFont(font)
        self.button_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_voltar.setObjectName("button_voltar")
        self.button_buscar = QtWidgets.QPushButton(self.centralwidget)
        self.button_buscar.setGeometry(QtCore.QRect(480, 130, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_buscar.setFont(font)
        self.button_buscar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_buscar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.button_buscar.setObjectName("button_buscar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 135, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 165, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 130, 281, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 160, 281, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 20))
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
        self.titulo.setText(_translate("MainWindow", "DEPOSITAR"))
        self.button_depositar.setText(_translate("MainWindow", "Depositar"))
        self.button_voltar.setText(_translate("MainWindow", "Voltar"))
        self.button_buscar.setText(_translate("MainWindow", "Buscar"))
        self.label.setText(_translate("MainWindow", "CPF DA CONTA:"))
        self.label_2.setText(_translate("MainWindow", "VALOR:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_depositar()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())