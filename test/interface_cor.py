#Codigo inicial + adicionar plano de fundo (cor solida)
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtGui
from PyQt5 import QtCore
#from PyQt5 import QPalette
if __name__ == '__main__':

	app = QApplication(sys.argv)
	teste = (12,12,12,212)
	palette = QtGui.QPalette()
	#palette.setColor(QtGui.QPalette.Background, QtCore.Qt.gray)
	palette.setColor(QtGui.QPalette.Background, QtGui.QColor(0xececec))


	window = QWidget()
	window.setPalette(palette)
	window.resize(300,400)
	window.setWindowTitle('Hello Qt')
	
	window.show()

	sys.exit(app.exec_())