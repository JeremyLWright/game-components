# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewCharacter.ui'
#
# Created: Mon Jul  4 15:53:05 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogAgent(object):
    def setupUi(self, DialogAgent):
        DialogAgent.setObjectName(_fromUtf8("DialogAgent"))
        DialogAgent.resize(400, 300)
        self.formLayoutWidget = QtGui.QWidget(DialogAgent)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 361, 141))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit_agentNameBox = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_agentNameBox.setObjectName(_fromUtf8("lineEdit_agentNameBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_agentNameBox)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_agentHealthPoints = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_agentHealthPoints.setObjectName(_fromUtf8("lineEdit_agentHealthPoints"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_agentHealthPoints)
        self.buttonBox = QtGui.QDialogButtonBox(self.formLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(DialogAgent)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogAgent.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogAgent.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogAgent)

    def retranslateUi(self, DialogAgent):
        DialogAgent.setWindowTitle(QtGui.QApplication.translate("DialogAgent", "New Character", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogAgent", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogAgent", "Health Points", None, QtGui.QApplication.UnicodeUTF8))

