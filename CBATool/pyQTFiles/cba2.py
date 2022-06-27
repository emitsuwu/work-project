# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cba2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(346, 227)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.titleLabel = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayout.addWidget(self.titleLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nameLabel = QtWidgets.QLabel(Dialog)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout_2.addWidget(self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.horizontalLayout_2.addWidget(self.nameLineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.priceLabel = QtWidgets.QLabel(Dialog)
        self.priceLabel.setObjectName("priceLabel")
        self.horizontalLayout_4.addWidget(self.priceLabel)
        self.priceLineEdit = QtWidgets.QLineEdit(Dialog)
        self.priceLineEdit.setObjectName("priceLineEdit")
        self.horizontalLayout_4.addWidget(self.priceLineEdit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.amtLabel = QtWidgets.QLabel(Dialog)
        self.amtLabel.setObjectName("amtLabel")
        self.horizontalLayout_3.addWidget(self.amtLabel)
        self.amtLineEdit = QtWidgets.QLineEdit(Dialog)
        self.amtLineEdit.setObjectName("amtLineEdit")
        self.horizontalLayout_3.addWidget(self.amtLineEdit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.submitPushButton = QtWidgets.QPushButton(Dialog)
        self.submitPushButton.setObjectName("submitPushButton")
        self.horizontalLayout_5.addWidget(self.submitPushButton)
        self.submitPushButton.clicked.connect(self.setValues) # THIS CONNECTS TO THE setValues DEF
        self.verticalLayout.addLayout(self.horizontalLayout_5)

    def setValues(self, Dialog):
        self.retranslateUi(Dialog)
        # nValue = self.nameLineEdit.text()
        # # nameLineEdit might not need to be error checked since it's a string and it can be named anything...?
        try:
            pValue = self.priceLineEdit.text()
            float(pValue)
            print("This is a true value and passes the float test.")
        except ValueError:
            print("Failed the float test.")
            pValue = None

        try:
            aValue = self.amtLineEdit.text()
            int(aValue)
            print("This is a true value and passes the int test.")
        except ValueError:
            print("Failed the int test.")
            aValue = None

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.titleLabel.setText(_translate("Dialog", "CBA TOOL"))
        self.nameLabel.setText(_translate("Dialog", "Name:"))
        self.priceLabel.setText(_translate("Dialog", "Price:"))
        self.amtLabel.setText(_translate("Dialog", "Amt:"))
        self.submitPushButton.setText(_translate("Dialog", "Submit"))
