# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'i wrote this myself lets gooo :)'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.(I don't know what I'md doing ;))


from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtCore import QSortFilterProxyModel
from PyQt5.QtWidgets import QCompleter, QComboBox
# import CBA_data_maker

class ExtendedComboBox(QComboBox):
    def __init__(self, parent=None):
        super(ExtendedComboBox, self).__init__(parent)

        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setEditable(True)

        # add a filter model to filter matching items
        self.pFilterModel = QSortFilterProxyModel(self)
        self.pFilterModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.model())

        # add a completer, which uses the filter model
        self.completer = QCompleter(self.pFilterModel, self)
        # always show all (filtered) completions
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.completer)

        # connect signals
        self.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        self.completer.activated.connect(self.on_completer_activated)


    # on selection of an item from the completer, select the corresponding item from combobox
    def on_completer_activated(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)
            self.activated[str].emit(self.itemText(index))


    # on model change, update the models of the filter and completer as well
    def setModel(self, model):
        super(ExtendedComboBox, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)


    # on model column change, update the model column of the filter and completer as well
    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(ExtendedComboBox, self).setModelColumn(column)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1366, 768)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        # sets everything for the row 1
        self.row1Info = QtWidgets.QHBoxLayout()
        # self.partComboBox = QtWidgets.QComboBox(Form)
        self.partComboBox = ExtendedComboBox()
        self.yearsSpinBox = QtWidgets.QSpinBox(Form)
        self.sparesSpinBox = QtWidgets.QSpinBox(Form)
        self.partLabel = QtWidgets.QLabel(Form)
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
        self.partLabel.setObjectName("partLabel")
        self.yearsLabel.setObjectName("yearsLabel")
        self.sparesLabel.setObjectName("sparesLabel")
        # self.partLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yearsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sparesLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yearsSpinBox.setMinimum(1)
        self.yearsSpinBox.setMaximum(100)
        self.sparesSpinBox.setMaximum(10000)

        # since the fixed size policy is the same for all spinboxes, just need to define the policy once for all spinboxes
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yearsSpinBox.sizePolicy().hasHeightForWidth())

        bold = QtGui.QFont()
        bold.setBold(True)
        bold.setWeight(75)
        self.partLabel.setFont(bold)
        self.yearsLabel.setFont(bold)
        self.sparesLabel.setFont(bold)
        self.partComboBox.setSizePolicy(sizePolicy)
        self.partLabel.setSizePolicy(sizePolicy)
        self.yearsSpinBox.setSizePolicy(sizePolicy)
        self.sparesSpinBox.setSizePolicy(sizePolicy)
        self.priceLabel = QtWidgets.QLabel(Form)
        self.learnRateSpinBox = QtWidgets.QSpinBox(Form)
        self.percentDecSpinBox = QtWidgets.QSpinBox(Form)
        self.learnRateLabel = QtWidgets.QLabel(Form)
        self.percentDecLabel = QtWidgets.QLabel(Form)
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
        self.priceLabel.setFont(bold)
        self.learnRateLabel.setFont(bold)
        self.percentDecLabel.setFont(bold)
        self.learnRateSpinBox.setSizePolicy(sizePolicy)
        self.percentDecSpinBox.setSizePolicy(sizePolicy)
        self.row1Info.addWidget(self.partLabel)
        self.row1Info.addWidget(self.partComboBox)
        self.row1Info.addWidget(self.priceLabel)
        self.row1Info.addWidget(self.yearsLabel)
        self.row1Info.addWidget(self.yearsSpinBox)
        self.row1Info.addWidget(self.sparesLabel)
        self.row1Info.addWidget(self.sparesSpinBox)
        self.row1Info.addWidget(self.learnRateLabel)
        self.row1Info.addWidget(self.learnRateSpinBox)
        self.row1Info.addWidget(self.percentDecLabel)
        self.row1Info.addWidget(self.percentDecSpinBox)
        self.verticalLayout.addLayout(self.row1Info)

        # sets everything for row 3 (EXCLUSIVELY PUSH BUTTON INPUT)
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

        # sets everything for row 4 (EXCLUSIVELY THE TABLE)
        self.tableInfo = QtWidgets.QHBoxLayout()
        self.tableView = QtWidgets.QTableView(Form)
        self.tableInfo.setObjectName("tableInfo")
        self.tableView.setObjectName("tableView")
        self.tableInfo.addWidget(self.tableView)
        self.verticalLayout.addLayout(self.tableInfo)

        self.retranslateUi(Form)
        self.resetPushButton.clicked.connect(self.setValues)
        # self.runPushButton.clicked.connect(self.popTable)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def setValues(self, Form):
        self.yearsSpinBox.setValue(1)
        self.learnRateSpinBox.setValue(1)
        self.sparesSpinBox.setValue(0)
        self.percentDecSpinBox.setValue(0)

    # this will run when the run button is pressed | currently generates already created qdatabase file
    # def popTable(self, Form):
    #     self.db = QSqlDatabase.addDatabase('QSQLITE')
    #     self.db.setDatabaseName('test.db')
    #
    #     self.model = QSqlTableModel(self, self.db)
    #     self.model.setTable('t1')
    #
    #     self.model.select()
    #
    #     self.tableView = QTableView(self)
    #     self.tableView.setModel(self.model)
    #     self.tableView.setModel(query)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ROIMockup"))

        #PROGRAM DOESN'T CHANGE WHETHER THIS CODE IS COMMENTED OUT OR NOT
        self.partComboBox.setCurrentText(_translate("Form", "part ID"))

        self.partComboBox.setItemText(0, _translate("Form", "Test 1"))
        self.partComboBox.setItemText(1, _translate("Form", "Test 2"))
        self.partComboBox.setItemText(2, _translate("Form", "Test 3"))
        string_list = ['hola muchachos', 'adios amigos', 'hello world', 'good bye']
        self.partComboBox.addItems(string_list)
        self.partLabel.setText(_translate("Form", "select part:"))
        self.yearsLabel.setText(_translate("Form", "no. of years:"))
        self.sparesLabel.setText(_translate("Form", "no. of spares:"))
        self.priceLabel.setText(_translate("Form", "[PRICE WILL SHOW HERE]"))
        self.learnRateLabel.setText(_translate("Form", "learn rate:"))
        self.percentDecLabel.setText(_translate("Form", "percent decrease:"))
        self.runPushButton.setText(_translate("Form", "RUN"))
        self.resetPushButton.setText(_translate("Form", "RESET"))
        self.pdfPushButton.setText(_translate("Form", "PDF"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
