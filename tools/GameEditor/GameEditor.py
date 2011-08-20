import sys
from PyQt4 import QtGui,QtCore
from UI import *
import NewCharacter
import json

class GameEditor(QtGui.QMainWindow):
    def __init__(self, parent=None):
        #build parent user interface
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        data = open("../../prototype/map.json", "rw")
        self.db = json.load(data)

        QtCore.QObject.connect(self.ui.buttonSaveDescription, QtCore.SIGNAL('clicked()'), self.CommitDialogText)
        QtCore.QObject.connect(self.ui.buttonNewLocation, QtCore.SIGNAL('clicked()'), self.NewLocation)
        QtCore.QObject.connect(self.ui.comboBoxNorthExit, QtCore.SIGNAL('currentIndexChanged(QString)'), self.NorthExitChanged)
        QtCore.QObject.connect(self.ui.comboBoxSouthExit, QtCore.SIGNAL('currentIndexChanged(QString)'), self.SouthExitChanged)
        QtCore.QObject.connect(self.ui.comboBoxEastExit, QtCore.SIGNAL('currentIndexChanged(QString)'), self.EastExitChanged)
        QtCore.QObject.connect(self.ui.comboBoxWestExit, QtCore.SIGNAL('currentIndexChanged(QString)'), self.WestExitChanged)

        for room in self.db.keys():
            self.ui.comboBoxNorthExit.addItem(room)
            self.ui.comboBoxSouthExit.addItem(room)
            self.ui.comboBoxEastExit.addItem(room)
            self.ui.comboBoxWestExit.addItem(room)
            self.ui.listWidgetLocations.addItem(room)

    def CommitDialogText(self):
        print "Saving Dialog to Database."

    def SouthExitChanged(self, string):
        print "South Changed"

    def EastExitChanged(self, string):
        print "East Changed"

    def WestExitChanged(self, string):
        print "West Changed"

    def NorthExitChanged(self, string):
        print "North Changed"

    def NewLocation(self):
        print "New Trigger Added."

    def NewLocationExit(self):
        print "New Trigger Added."

    def NewTrigger(self):
        print "New Trigger Added."

    def NewCharacter(self):
        class NewCharacterDialog(QtGui.QDialog, NewCharacter.Ui_DialogAgent):
            def __init__(self, parent=None):
                QtGui.QDialog.__init__(self,parent)
                self.setupUi(self)
            def GetValues(self):
                return (self.lineEdit_agentNameBox.text(),self.lineEdit_agentHealthPoints.text(),)
        dlg = NewCharacterDialog()
        if dlg.exec_():
            self.ui.comboBox.addItem(dlg.GetValues()[0])

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = GameEditor()
    myapp.show()
    sys.exit(app.exec_())
