import sys
from PyQt4 import QtGui,QtCore
from UI import *

class GameEditor(QtGui.QMainWindow):
    def __init__(self, parent=None):
        #build parent user interface
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = GameEditor()
    myapp.show()
    sys.exit(app.exec_())
