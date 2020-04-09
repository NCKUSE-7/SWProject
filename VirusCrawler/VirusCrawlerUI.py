# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VirusCrawlerUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Flight(object):
    def setupUi(self, Flight):
        Flight.setObjectName("Flight")
        Flight.resize(1200, 900)
        self.main = QtWidgets.QPushButton(Flight)
        self.main.setGeometry(QtCore.QRect(2, 0, 125, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        self.main.setFont(font)
        self.main.setObjectName("main")
        self.flighttable = QtWidgets.QTableWidget(Flight)
        self.flighttable.setGeometry(QtCore.QRect(0, 50, 1200, 950))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.flighttable.setFont(font)
        self.flighttable.setInputMethodHints(QtCore.Qt.ImhNone)
        self.flighttable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.flighttable.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.flighttable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.flighttable.setRowCount(100)
        self.flighttable.setColumnCount(6)
        self.flighttable.setObjectName("flighttable")
        item = QtWidgets.QTableWidgetItem()
        self.flighttable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.flighttable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.flighttable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.flighttable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.flighttable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.flighttable.setHorizontalHeaderItem(5, item)
        self.flighttable.horizontalHeader().setDefaultSectionSize(190)
        self.flighttable.verticalHeader().setDefaultSectionSize(40)
        self.reload = QtWidgets.QPushButton(Flight)
        self.reload.setGeometry(QtCore.QRect(150, 0, 125, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        self.reload.setFont(font)
        self.reload.setObjectName("reload")

        self.retranslateUi(Flight)
        self.main.clicked.connect(self.flighttable.hide)
        QtCore.QMetaObject.connectSlotsByName(Flight)

    def retranslateUi(self, Flight):
        _translate = QtCore.QCoreApplication.translate
        Flight.setWindowTitle(_translate("Flight", "Form"))
        self.main.setText(_translate("Flight", "Main"))
        item = self.flighttable.horizontalHeaderItem(0)
        item.setText(_translate("Flight", "出入境"))
        item = self.flighttable.horizontalHeaderItem(1)
        item.setText(_translate("Flight", "表定時間"))
        item = self.flighttable.horizontalHeaderItem(2)
        item.setText(_translate("Flight", "航空公司"))
        item = self.flighttable.horizontalHeaderItem(3)
        item.setText(_translate("Flight", "班機編號"))
        item = self.flighttable.horizontalHeaderItem(4)
        item.setText(_translate("Flight", "往來城市"))
        item = self.flighttable.horizontalHeaderItem(5)
        item.setText(_translate("Flight", "狀態"))
        self.reload.setText(_translate("Flight", "Reload"))
