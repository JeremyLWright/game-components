# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GameEditor.ui'
#
# Created: Mon Jul  4 15:17:29 2011
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
        MainWindow.resize(799, 600)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton_NewCharacter = QtGui.QPushButton(self.centralwidget)
        self.pushButton_NewCharacter.setGeometry(QtCore.QRect(690, 40, 97, 27))
        self.pushButton_NewCharacter.setObjectName(_fromUtf8("pushButton_NewCharacter"))
        self.pushButton_NewTrigger = QtGui.QPushButton(self.centralwidget)
        self.pushButton_NewTrigger.setGeometry(QtCore.QRect(530, 520, 97, 27))
        self.pushButton_NewTrigger.setObjectName(_fromUtf8("pushButton_NewTrigger"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 10, 67, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(610, 10, 181, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(530, 80, 261, 431))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 80, 511, 291))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.pushButton_CommitDialogText = QtGui.QPushButton(self.centralwidget)
        self.pushButton_CommitDialogText.setGeometry(QtCore.QRect(420, 380, 97, 27))
        self.pushButton_CommitDialogText.setObjectName(_fromUtf8("pushButton_CommitDialogText"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 25))
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
        self.pushButton_NewCharacter.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_NewTrigger.setText(QtGui.QApplication.translate("MainWindow", "New Trigger", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Characters", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CommitDialogText.setText(QtGui.QApplication.translate("MainWindow", "Commit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Database.setText(QtGui.QApplication.translate("MainWindow", "Open Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

