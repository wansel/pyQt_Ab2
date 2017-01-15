# -*- coding: utf-8 -*-
#Codigo inicial
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from errors import ValorInvalidoError
from errors import SaldoInsuficienteError
from conta import Conta
# add:Cores
from PyQt5 import QtGui
from PyQt5 import QtCore
#add QLabel, QPushButton, QGridLayout, QLineEdit
from PyQt5.QtWidgets import QLabel, QPushButton, QGridLayout,QLineEdit
#MessageBox
from PyQt5.QtWidgets import QInputDialog
#font
#QfontDatabase
class Tela(QWidget):
	def __init__(self):
		palette = QtGui.QPalette()
		#Adicionando Fontes
		QtGui.QFontDatabase.addApplicationFont("font/Roboto-BlackItalic.ttf")
		QtGui.QFontDatabase.addApplicationFont("font/Roboto-Bold.ttf")
		QtGui.QFontDatabase.addApplicationFont("font/Roboto-BoldItalic.ttf")
		QtGui.QFontDatabase.addApplicationFont("font/Roboto-Italic.ttf")
		QtGui.QFontDatabase.addApplicationFont("font/Roboto-Light.ttf")
		QtGui.QFontDatabase.addApplicationFont("font/Roboto-LightItalic.ttf")
		QtGui.QFontDatabase.addApplicationFont("font/Roboto-Medium.ttf")
		QtGui.QFontDatabase.addApplicationFont("font/Roboto-MediumItalic.ttf")
		QtGui.QFontDatabase.addApplicationFont("font/Roboto-Regular.ttf")
		QtGui.QFontDatabase.addApplicationFont("font/Roboto-Thin.ttf")
		QtGui.QFontDatabase.addApplicationFont("font/Roboto-ThinItalic.ttf")
		QtGui.QFontDatabase.addApplicationFont("font/Roboto-Black.ttf")
		#Definindo cor de fundo da Janela
		palette.setColor(QtGui.QPalette.Background, QtGui.QColor(0xbdbdbd)) #
		self = QWidget()
		#window.resize(9,16)
		self.setWindowTitle('Sistema Bancário - Wansel Lemos')
		self.setPalette(palette)
		
		#Criando componentes
		lb_inicio = QLabel('<h1>Bem vindo, como deseja prosseguir?<h1>', self)
		ln_conta = QLineEdit(self)
		bt_cadastro = QPushButton('Cadastrar conta', self)
		bt_saldo = QPushButton('Verificar Saldo', self)
		bt_saque = QPushButton('Realizar Saque', self)
		bt_deposito = QPushButton('Realizar Deposito', self)
		bt_extrato = QPushButton('Imprimir Extrato', self)
		bt_sair = QPushButton('Encerrar', self)

		#Dicas
		bt_cadastro.setToolTip("Cadastre uma nova conta no sistema")
		bt_saldo.setToolTip("Verifique o saldo de uma conta")
		bt_saque.setToolTip("Realize um saque em uma conta. A mesma deve ser previamente cadastrada no sistema.")
		bt_deposito.setToolTip("Deposite um valor após informar o número da conta")
		bt_extrato.setToolTip("Imprima na tela o histórico de transações de uma conta")
		bt_sair.setToolTip("Encerre o programa, as informações serão perdidas :(")
		
		#Formatação
		sshFile = "style.stylesheet"
		with open(sshFile,"r") as fh:
			self.setStyleSheet(fh.read())

		#acoes

		bt_cadastro.clicked.connect(cadastrarConta())
		#Grid Layout - adicionando componentes
		grid = QGridLayout()
		#grid.setSize(5,3)
		self.setLayout(grid)
		grid.addWidget(lb_inicio,1,1,1,1)
		grid.addWidget(ln_conta,2,1,1,1)
		grid.addWidget(bt_cadastro,4,1,1,1)
		grid.addWidget(bt_saldo,5,1,1,1)
		grid.addWidget(bt_saque,6,1,1,1)
		grid.addWidget(bt_deposito,7,1,1,1)
		grid.addWidget(bt_extrato,8,1,1,1)
		grid.addWidget(bt_sair,10,1,2,1)
		ln_conta.setText("Digite o número da conta neste campo")
		self.show()

	def cadastrarConta():
		print ("Workou")
