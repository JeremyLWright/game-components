import sys
from PyQt4 import QtGui,QtCore
from UI import *
import NewCharacter

class GameEditor(QtGui.QMainWindow):
    def __init__(self, parent=None):
        #build parent user interface
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton_NewCharacter, QtCore.SIGNAL('clicked()'), self.NewCharacter)
        QtCore.QObject.connect(self.ui.pushButton_CommitDialogText, QtCore.SIGNAL('clicked()'), self.CommitDialogText)
        QtCore.QObject.connect(self.ui.pushButton_NewTrigger, QtCore.SIGNAL('clicked()'), self.NewTrigger)

    def CommitDialogText(self):
        print "Saving Dialog to Database."

    def NewTrigger(self):
        print "New Trigger Added."

    def NewCharacter(self):
        class NewCharacterDialog(QtGui.QDialog, NewCharacter.Ui_DialogAgent):
            def __init__(self, parent=None):
                QtGui.QDialog.__init__(self,parent)
                self.setupUi(self)
            def GetValues(self):
                return (self.lineEdit_agentNameBox.text(),)
        dlg = NewCharacterDialog()
        if dlg.exec_():
            self.ui.comboBox.addItem(dlg.GetValues()[0])

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = GameEditor()
    myapp.show()
    sys.exit(app.exec_())
