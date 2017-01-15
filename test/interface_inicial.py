#Codigo inicial dado no slide
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

	app = QApplication(sys.argv)

	window = QWidget()
	window.resize(300,400)
	window.setWindowTitle('Hello Qt')
	window.show()

	sys.exit(app.exec_())