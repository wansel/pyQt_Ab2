#Codigo inicial dado no slide
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel

if __name__ == '__main__':

	app = QApplication(sys.argv)

	window = QWidget()
	window.resize(300,400)
	window.setWindowTitle('Hello Qt')
	window.show()
	##inicio
	lb_inicio = QLabel('Bem vindo, como deseja prosseguir?', window)
	bt_cadastro = QPushButton('Cadastrar conta', window)
	bt_saldo = QPushButton('Verificar Saldo', window)
	bt_saque = QPushButton('Realizar Saque', window)
	bt_deposito = QPushButton('Realizar Deposito', window)
	bt_extrato = QPushButton('Imprimir Extrato', window)
	bt_sair = QPushButton('Encerrar', window)

	#Grid Layout
	grid = QGridLayout()
	window.setLayout(grid)
	grid.addWidget(lb_inicio,1,1,1,1)
	grid.addWidget(bt_cadastro,1,1,2,1)
	grid.addWidget(bt_saldo,1,1,3,1)
	grid.addWidget(bt_saque,1,1,4,1)
	grid.addWidget(bt_deposito,1,1,5,1)
	grid.addWidget(bt_extrato,1,1,6,1)
	grid.addWidget(bt_sair,1,1,7,1)
	##fim
	sys.exit(app.exec_())