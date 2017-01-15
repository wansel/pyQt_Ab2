# -*- coding: utf-8 -*-
#Codigo inicial
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QGridLayout,QLineEdit, QInputDialog,QMessageBox)

# add:Cores
from PyQt5 import QtGui
from PyQt5 import QtCore

contas = {}
transacoes = []

class Tela(QWidget):
	
	def __init__(self, parent=None):
		super(Tela, self).__init__()
		self.initUI(self)
		
	def initUI(self,args):
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
		palette = QtGui.QPalette()
		palette.setColor(QtGui.QPalette.Background, QtGui.QColor(0xbdbdbd)) #
		self.setWindowTitle('Sistema Bancário - Wansel Lemos')
		self.setPalette(palette)
		self.show()
		#Criando os componentes
		self.lb_inicio = QLabel('<h1>Bem vindo, como deseja prosseguir?<h1>', self)
		self.ln_conta = QLineEdit(self)
		self.bt_cadastro = QPushButton('Cadastrar conta', self)
		self.bt_saldo = QPushButton('Verificar Saldo', self)
		self.bt_saque = QPushButton('Realizar Saque', self)
		self.bt_deposito = QPushButton('Realizar Deposito', self)
		self.bt_extrato = QPushButton('Imprimir Extrato', self)
		self.bt_sair = QPushButton('Encerrar', self)
		self.lb_ultimaAcao = QLabel('',self)
		#Dicas (Tooltips)
		self.bt_cadastro.setToolTip("Cadastre uma nova conta no sistema")
		self.bt_saldo.setToolTip("Verifique o saldo de uma conta")
		self.bt_saque.setToolTip("Realize um saque em uma conta. A mesma deve ser previamente cadastrada no sistema.")
		self.bt_deposito.setToolTip("Deposite um valor após informar o número da conta")
		self.bt_extrato.setToolTip("Imprima na tela o histórico de transações de uma conta")
		self.bt_sair.setToolTip("Encerre o programa, as informações serão perdidas :(")
		#Formatação (folha de estilos, personalização dos botões e labels)
		sshFile = "style.stylesheet"
		with open(sshFile,"r") as fh:
			self.setStyleSheet(fh.read())
		#Ações
		self.bt_cadastro.clicked.connect(self.cadastrarConta)
		self.bt_saldo.clicked.connect(self.checarSaldo)
		self.bt_saque.clicked.connect(self.realizarSaque)
		self.bt_deposito.clicked.connect(self.realizarDeposito)
		self.bt_extrato.clicked.connect(self.imprimirExtrato)
		self.bt_sair.clicked.connect(self.sair)

		#Grid Layout
		grid = QGridLayout(self)
		#Posicionando os componentes na grade
		grid.addWidget(self.lb_inicio,1,1,1,1)
		grid.addWidget(self.ln_conta,2,1,1,1)
		grid.addWidget(self.bt_cadastro,4,1,1,1)
		grid.addWidget(self.bt_saldo,5,1,1,1)
		grid.addWidget(self.bt_saque,6,1,1,1)
		grid.addWidget(self.bt_deposito,7,1,1,1)
		grid.addWidget(self.bt_extrato,8,1,1,1)
		grid.addWidget(self.bt_sair,10,1,2,1)
		grid.addWidget(self.lb_ultimaAcao,11,1,2,1)
		self.ln_conta.setText("Digite o número da conta neste campo")
		self.setLayout(grid)
	#Atualização label que mostra a ultima ação do usuário
	def UpdateUltimaAcao(self,acao):
		self.lb_ultimaAcao.setText(acao)
	#Cadastrar Conta
	def cadastrarConta(self):
		try:
			msg = QMessageBox(self)
			msg.setWindowTitle("Confirme antes de prossegir")
			msg.setText("Deseja Cadastrar essa conta?")
			msg.setInformativeText("{}".format(self.ln_conta.text()))
			msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
			retorno = (msg.exec_())

			if(retorno==QMessageBox.Yes):
				if self.ln_conta.text() in contas :
					self.UpdateUltimaAcao("Conta já cadastrada, operação não realizada.")
				else:
					contas[self.ln_conta.text()] = 0
					transacoes.append([self.ln_conta.text(), 0])
					self.UpdateUltimaAcao("Conta <b>{}</b> cadastrada".format(self.ln_conta.text()))
			else:
				self.UpdateUltimaAcao("Operação <b>Cadastrar Conta</b> Cancelada pelo Usuário.")
		except Exception as error:
			ErrorMessage = QMessageBox(self)
			ErrorMessage.setText("Algo Inesperado Aconteceu:")
			ErrorMessage.setInformativeText(error)
			ErrorMessage.setStandardButtons(QMessageBox.Yes)
			ErrorMessage.exec_()
	#Saldo
	def checarSaldo(self):
		if self.ln_conta.text() in contas:
			msg = QMessageBox(self)
			msg.setWindowTitle("Saldo")
			msg.setText("Saldo Disponível:")
			msg.setInformativeText("<b>R${:.2f}</b>".format(contas[self.ln_conta.text()]))
			msg.setStandardButtons(QMessageBox.Yes)
			self.UpdateUltimaAcao("Saldo verificado")
			msg.exec_()
		else:
			self.UpdateUltimaAcao("Conta não existente")
	#Saque
	def realizarSaque(self):
		ok = False
		if self.ln_conta.text() in contas:
			msg, ok = QInputDialog.getDouble(self, "Insira o Valor para o Saque:", "Disponível: {:.2f}".format(contas[self.ln_conta.text()]))
			if(msg<=contas[self.ln_conta.text()] and msg>0 and ok):
				contas[self.ln_conta.text()]-= msg
				transacoes.append([self.ln_conta.text(), -(msg)])
				self.UpdateUltimaAcao("Saque no valor de R$ {:.2f} realizado com sucesso".format(msg))
			elif(not ok):
				self.UpdateUltimaAcao("Operação de Saque Cancelada pelo Usuário.")
			elif(ok):
				self.UpdateUltimaAcao("Saldo insifuciente, operação cancelada.")
		else:
			self.UpdateUltimaAcao("Conta não existente")

	#Depósito
	def realizarDeposito(self):
		ok = False
		if self.ln_conta.text() in contas:
			msg, ok = QInputDialog.getDouble(self, "Insira o Valor para o Deposíto:","R$")
			if (self.ln_conta.text() in contas and msg>0 and ok):
				contas[self.ln_conta.text()] += msg
				transacoes.append([self.ln_conta.text(), msg])
			elif(msg<=0 and ok):
				self.UpdateUltimaAcao("Valor inválido.")
			elif(not ok):
				self.UpdateUltimaAcao("Operação de Depósito cancelada pelo usuário")
		else:
			self.UpdateUltimaAcao("Conta não existente")
	#Extrato
	def imprimirExtrato(self):
		if(self.ln_conta.text() in contas):
			extrato = "<b>Extrato - Conta "+self.ln_conta.text() + "</b><ln><br/>"
			for x in transacoes:
				if(x[0] == self.ln_conta.text()):
					extrato+= "R$ "+str(x[1])
					if(x[1]>0): #Operações iguais a zero são proibídas pelo sistema (exceto a de cadastro)
						extrato += " ( Depósito)<br/>"
					elif(x[1]<0):
						extrato += " (Saque)<br/>"
					else:
						extrato+= " (Abertura)<br/>"
			msg = QMessageBox(self)
			msg.setText(extrato)
			msg.setWindowTitle("Extrato")
			msg.setStandardButtons(QMessageBox.Yes)
			msg.exec_()
			print(extrato)
			self.UpdateUltimaAcao("Extrato verificado")
		else:
			self.UpdateUltimaAcao("Conta não existente")
	#Sair do sistema
	def sair(self):
		self.close()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Tela()
	sys.exit(app.exec_())