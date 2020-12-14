# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/UI/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 636)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.storeButton = QtWidgets.QPushButton(self.widget)
        self.storeButton.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(18)
        self.storeButton.setFont(font)
        self.storeButton.setAccessibleName("")
        self.storeButton.setObjectName("storeButton")
        self.horizontalLayout.addWidget(self.storeButton)
        self.profileButton = QtWidgets.QPushButton(self.widget)
        self.profileButton.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(18)
        self.profileButton.setFont(font)
        self.profileButton.setObjectName("profileButton")
        self.horizontalLayout.addWidget(self.profileButton)
        self.statisticButton = QtWidgets.QPushButton(self.widget)
        self.statisticButton.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(18)
        self.statisticButton.setFont(font)
        self.statisticButton.setObjectName("statisticButton")
        self.horizontalLayout.addWidget(self.statisticButton)
        self.outButton = QtWidgets.QPushButton(self.widget)
        self.outButton.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(18)
        self.outButton.setFont(font)
        self.outButton.setObjectName("outButton")
        self.horizontalLayout.addWidget(self.outButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.widget)
        self.ViewField = QtWidgets.QWidget(self.centralwidget)
        self.ViewField.setEnabled(True)
        self.ViewField.setAccessibleName("")
        self.ViewField.setObjectName("ViewField")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ViewField)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.algsField = QtWidgets.QScrollArea(self.ViewField)
        self.algsField.setWidgetResizable(True)
        self.algsField.setObjectName("algsField")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 694, 500))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.algsField.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.algsField)
        self.InfoField = QtWidgets.QGroupBox(self.ViewField)
        self.InfoField.setObjectName("InfoField")
        self.verticalLayout_3.addWidget(self.InfoField)
        self.verticalLayout.addWidget(self.ViewField)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.storeButton.setText(_translate("MainWindow", "Store"))
        self.profileButton.setText(_translate("MainWindow", "My profile"))
        self.statisticButton.setText(_translate("MainWindow", "Statistics"))
        self.outButton.setText(_translate("MainWindow", "Sign out"))
        self.label_8.setText(_translate("MainWindow", "List of algorithms:"))
        self.InfoField.setTitle(_translate("MainWindow", "GroupBox"))
