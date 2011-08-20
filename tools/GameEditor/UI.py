# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GameEditor.ui'
#
# Created: Fri Aug 19 23:17:01 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1049, 780)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 691, 331))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.buttonSaveDescription = QtGui.QPushButton(self.centralwidget)
        self.buttonSaveDescription.setGeometry(QtCore.QRect(590, 360, 97, 27))
        self.buttonSaveDescription.setObjectName(_fromUtf8("buttonSaveDescription"))
        self.buttonNewLocation = QtGui.QPushButton(self.centralwidget)
        self.buttonNewLocation.setGeometry(QtCore.QRect(900, 650, 141, 27))
        self.buttonNewLocation.setObjectName(_fromUtf8("buttonNewLocation"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 350, 321, 221))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayoutWidget = QtGui.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 261, 131))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.comboBoxNorthExit = QtGui.QComboBox(self.formLayoutWidget)
        self.comboBoxNorthExit.setObjectName(_fromUtf8("comboBoxNorthExit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBoxNorthExit)
        self.comboBoxEastExit = QtGui.QComboBox(self.formLayoutWidget)
        self.comboBoxEastExit.setObjectName(_fromUtf8("comboBoxEastExit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBoxEastExit)
        self.comboBoxWestExit = QtGui.QComboBox(self.formLayoutWidget)
        self.comboBoxWestExit.setObjectName(_fromUtf8("comboBoxWestExit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.comboBoxWestExit)
        self.comboBoxSouthExit = QtGui.QComboBox(self.formLayoutWidget)
        self.comboBoxSouthExit.setObjectName(_fromUtf8("comboBoxSouthExit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBoxSouthExit)
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.listWidgetLocations = QtGui.QListWidget(self.centralwidget)
        self.listWidgetLocations.setGeometry(QtCore.QRect(710, 10, 331, 631))
        self.listWidgetLocations.setObjectName(_fromUtf8("listWidgetLocations"))
        self.lineEditNewLocation = QtGui.QLineEdit(self.centralwidget)
        self.lineEditNewLocation.setGeometry(QtCore.QRect(710, 650, 181, 27))
        self.lineEditNewLocation.setObjectName(_fromUtf8("lineEditNewLocation"))
        self.pushButtonRenameLocation = QtGui.QPushButton(self.centralwidget)
        self.pushButtonRenameLocation.setGeometry(QtCore.QRect(900, 680, 141, 27))
        self.pushButtonRenameLocation.setObjectName(_fromUtf8("pushButtonRenameLocation"))
        self.lineEditRenameLocation = QtGui.QLineEdit(self.centralwidget)
        self.lineEditRenameLocation.setGeometry(QtCore.QRect(710, 680, 181, 27))
        self.lineEditRenameLocation.setObjectName(_fromUtf8("lineEditRenameLocation"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1049, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Database = QtGui.QAction(MainWindow)
        self.actionOpen_Database.setObjectName(_fromUtf8("actionOpen_Database"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionOpen_Database)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Practicum Game Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSaveDescription.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonNewLocation.setText(QtGui.QApplication.translate("MainWindow", "Add New Location", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Exits", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "North", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "East", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "South", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "West", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRenameLocation.setText(QtGui.QApplication.translate("MainWindow", "Rename Location", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Database.setText(QtGui.QApplication.translate("MainWindow", "Open Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

