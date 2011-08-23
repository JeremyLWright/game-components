import sys
from PyQt4 import QtGui,QtCore
from UI import *
import NewCharacter
import json

class GameEditor(QtGui.QMainWindow):
    def __init__(self, defaultDatabase="world.json", parent=None):
        #build parent user interface
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBoxNorthExit.addItem("")
        self.ui.comboBoxSouthExit.addItem("")
        self.ui.comboBoxEastExit.addItem("")
        self.ui.comboBoxWestExit.addItem("")
        try:
            data = open(defaultDatabase, "r")
            self.db = json.load(data)
            data.close()
            for room in self.db.keys():
                self.ui.comboBoxNorthExit.addItem(room)
                self.ui.comboBoxSouthExit.addItem(room)
                self.ui.comboBoxEastExit.addItem(room)
                self.ui.comboBoxWestExit.addItem(room)
                self.ui.listWidgetLocations.addItem(room)
        except:
            self.db = {}

        QtCore.QObject.connect(self.ui.buttonSaveDescription, QtCore.SIGNAL('clicked()'), self.CommitDialogText)
        QtCore.QObject.connect(self.ui.buttonNewLocation, QtCore.SIGNAL('clicked()'), self.NewLocation)
        QtCore.QObject.connect(self.ui.comboBoxNorthExit, QtCore.SIGNAL('currentIndexChanged(QString)'), self.NorthExitChanged)
        QtCore.QObject.connect(self.ui.comboBoxSouthExit, QtCore.SIGNAL('currentIndexChanged(QString)'), self.SouthExitChanged)
        QtCore.QObject.connect(self.ui.comboBoxEastExit, QtCore.SIGNAL('currentIndexChanged(QString)'), self.EastExitChanged)
        QtCore.QObject.connect(self.ui.comboBoxWestExit, QtCore.SIGNAL('currentIndexChanged(QString)'), self.WestExitChanged)
        QtCore.QObject.connect(self.ui.listWidgetLocations, QtCore.SIGNAL('currentTextChanged(QString)'), self.locationSelected)
        QtCore.QObject.connect(self.ui.pushButtonRenameLocation, QtCore.SIGNAL('clicked()'), self.renameLocation)
        

    def renameLocation(self):
        currentLocationName = self.getCurrentLocationSelection()
        newLocationName = str(self.ui.lineEditRenameLocation.text())
        self.db[newLocationName] = self.db[currentLocationName]
        del self.db[currentLocationName]
        self.ui.listWidgetLocations.currentItem().setText(newLocationName)
        self.renameComboBox(self.ui.comboBoxNorthExit, currentLocationName, newLocationName)

    
    def renameComboBox(self, comboBox, oldLocation, newLocation):
        idx = comboBox.findText(oldLocation)
        comboBox.removeItem(idx)
        comboBox.addItem(newLocation)

    def saveDatabase(self):
        filename = str(self.ui.lineEditFilename.text())
        data = open(filename, "w")
        jsonData = json.dumps(self.db, sort_keys=True, indent=4)
        data.write(jsonData)
        data.close()

    def CommitDialogText(self):
        print "Saving Dialog to Database."
        self.saveDatabase()

    def setExitComboBox(self, comboBox, location, direction):
        try:
            exits = self.db[str(location)]["Exits"]
            exit = exits[direction]
            exitIndex = comboBox.findText(exit)
            comboBox.setCurrentIndex(exitIndex)
        except:
            comboBox.setCurrentIndex(comboBox.findText(""))


    def locationSelected(self, location):
        print str(location)+" selected"
        exits = self.db[str(location)]["Exits"]
        self.ui.lineEditRenameLocation.setText(str(location))
        self.ui.plainTextEdit.setPlainText(self.db[str(location)]["Description"])
        self.setExitComboBox(self.ui.comboBoxNorthExit, location, "North")
        self.setExitComboBox(self.ui.comboBoxSouthExit, location, "South")
        self.setExitComboBox(self.ui.comboBoxEastExit, location, "East")
        self.setExitComboBox(self.ui.comboBoxWestExit, location, "West")

    def getCurrentLocationSelection(self):
        return str(self.ui.listWidgetLocations.currentItem().text())

    def addBiDirectionalPath(self, direction, target):
        currentLocation = self.getCurrentLocationSelection()
        reverseDirection = ""
        if(direction == "North"):
            reverseDirection = "South"
        elif(direction == "East"):
            reverseDirection = "West"
        elif(direction == "West"):
            reverseDirection = "East"
        elif(direction == "South"):
            reverseDirection = "North"
        else:
            raise "Invalid direction"

        self.db[currentLocation]["Exits"][direction] = str(target)
        self.db[str(target)]["Exits"][reverseDirection] = currentLocation


    def SouthExitChanged(self, string):
        self.addBiDirectionalPath("South", string)

    def EastExitChanged(self, string):
        self.addBiDirectionalPath("East", string)

    def WestExitChanged(self, string):
        self.addBiDirectionalPath("West", string)

    def NorthExitChanged(self, string):
        self.addBiDirectionalPath("North", string)

    def NewLocation(self):
        newLocation = str(self.ui.lineEditNewLocation.text())
        self.ui.comboBoxNorthExit.addItem(newLocation)
        self.ui.comboBoxSouthExit.addItem(newLocation)
        self.ui.comboBoxEastExit.addItem(newLocation)
        self.ui.comboBoxWestExit.addItem(newLocation)
        self.ui.listWidgetLocations.addItem(newLocation)
        self.db[newLocation] = {};
        self.db[newLocation]["Description"] = ""
        self.db[newLocation]["Items"] = []
        self.db[newLocation]["Exits"] = {"North": "", "East": "", "South": "", "West": ""}



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
    myapp = GameEditor(sys.argv[1])
    myapp.show()
    sys.exit(app.exec_())
