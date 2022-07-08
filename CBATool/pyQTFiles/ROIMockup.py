# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'i wrote this myself lets gooo :)'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.(I don't know what I'md doing ;))


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 400)

        # sets everything for the first row
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.row1Info = QtWidgets.QHBoxLayout()
        self.partComboBox = QtWidgets.QComboBox(Form)
        self.yearsSpinBox = QtWidgets.QSpinBox(Form)
        self.sparesSpinBox = QtWidgets.QSpinBox(Form)
        self.yearsLabel = QtWidgets.QLabel(Form)
        self.sparesLabel = QtWidgets.QLabel(Form)

        # changing all settings for partComboBox
        self.partComboBox.setEditable(True)
        self.partComboBox.setMaxVisibleItems(100)
        self.partComboBox.addItem("")
        self.partComboBox.addItem("")
        self.partComboBox.addItem("")

        self.row1Info.setObjectName("row1Info")
        self.partComboBox.setObjectName("partComboBox")
        self.yearsSpinBox.setObjectName("yearsSpinBox")
        self.sparesSpinBox.setObjectName("sparesSpinBox")
        self.yearsLabel.setObjectName("yearsLabel")
        self.sparesLabel.setObjectName("sparesLabel")
        self.yearsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sparesLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yearsSpinBox.setMinimum(1)
        self.yearsSpinBox.setMaximum(100)
        self.sparesSpinBox.setMaximum(10000)
        self.row1Info.addWidget(self.partComboBox)
        self.row1Info.addWidget(self.yearsLabel)
        self.row1Info.addWidget(self.yearsSpinBox)
        self.row1Info.addWidget(self.sparesLabel)
        self.row1Info.addWidget(self.sparesSpinBox)
        self.verticalLayout.addLayout(self.row1Info)

        # sets everything for row 2
        self.row2Info = QtWidgets.QHBoxLayout()
        self.priceLabel = QtWidgets.QLabel(Form)
        self.learnRateSpinBox = QtWidgets.QSpinBox(Form)
        self.percentDecSpinBox = QtWidgets.QSpinBox(Form)
        self.learnRateLabel = QtWidgets.QLabel(Form)
        self.percentDecLabel = QtWidgets.QLabel(Form)
        self.row2Info.setObjectName("row2Info")
        self.priceLabel.setObjectName("priceLabel")
        self.learnRateSpinBox.setObjectName("learnRateSpinBox")
        self.percentDecSpinBox.setObjectName("percentDecSpinBox")
        self.learnRateLabel.setObjectName("learnRateLabel")
        self.percentDecLabel.setObjectName("percentDecLabel")
        self.learnRateLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.percentDecLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.learnRateSpinBox.setMinimum(1)
        self.learnRateSpinBox.setMaximum(100)
        self.percentDecSpinBox.setMaximum(100)
        self.row2Info.addWidget(self.priceLabel)
        self.row2Info.addWidget(self.learnRateLabel)
        self.row2Info.addWidget(self.learnRateSpinBox)
        self.row2Info.addWidget(self.percentDecLabel)
        self.row2Info.addWidget(self.percentDecSpinBox)
        self.verticalLayout.addLayout(self.row2Info)

        # sets everything for row 3 (EXCLUSIVELY THE TABLE)
        self.tableInfo = QtWidgets.QHBoxLayout()
        self.tableView = QtWidgets.QTableView(Form)
        self.tableInfo.setObjectName("tableInfo")
        self.tableView.setObjectName("tableView")
        self.tableInfo.addWidget(self.tableView)
        self.verticalLayout.addLayout(self.tableInfo)

        # sets everything for row 4 (EXCLUSIVELY PUSH BUTTON INPUT)
        self.pushButtonRow = QtWidgets.QHBoxLayout()
        self.pushButtonRow.setObjectName("pushButtonRow")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.runPushButton = QtWidgets.QPushButton(Form)
        self.resetPushButton = QtWidgets.QPushButton(Form)
        self.pdfPushButton = QtWidgets.QPushButton(Form)
        self.runPushButton.setObjectName("runPushButton")
        self.resetPushButton.setObjectName("resetPushButton")
        self.pdfPushButton.setObjectName("pdfPushButton")
        self.pushButtonRow.addItem(spacerItem)
        self.pushButtonRow.addWidget(self.runPushButton)
        self.pushButtonRow.addWidget(self.resetPushButton)
        self.pushButtonRow.addWidget(self.pdfPushButton)
        self.verticalLayout.addLayout(self.pushButtonRow)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ROIMockup"))
        # self.partComboBox.setCurrentText(_translate("Form", "part ID")) PROGRAM DOESN'T CHANGE WHETHER THIS CODE IS COMMENTED OUT OR NOT
        self.partComboBox.setItemText(0, _translate("Form", "Test 1"))
        self.partComboBox.setItemText(1, _translate("Form", "Test 2"))
        self.partComboBox.setItemText(2, _translate("Form", "Test 3"))
        self.yearsLabel.setText(_translate("Form", "# years:"))
        self.sparesLabel.setText(_translate("Form", "# spares:"))
        self.priceLabel.setText(_translate("Form", "Price"))
        self.learnRateLabel.setText(_translate("Form", "learn rate:"))
        self.percentDecLabel.setText(_translate("Form", "% dec:"))
        self.runPushButton.setText(_translate("Form", "RUN"))
        self.resetPushButton.setText(_translate("Form", "RESET"))
        self.pdfPushButton.setText(_translate("Form", "PDF"))

    # this def is for setting up menu bar; expected to be deleted or changed later so don't worry too much about it


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())