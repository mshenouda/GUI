from gui_handler import GUI
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread

class CONTROL:

	def __init__(self):
		pass

	def execute(self):
		app = QtWidgets.QApplication(sys.argv)
		MainWindow = QtWidgets.QMainWindow()
		ui = GUI()
		ui.setupUi(MainWindow)
		MainWindow.show()
		sys.exit(app.exec_())



if __name__ == "__main__":
	ctrl = CONTROL()
	ctrl.execute()