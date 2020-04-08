# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VirusCrawlerUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Flight(object):
    def setupUi(self, Flight):
        Flight.setObjectName("Flight")
        Flight.resize(1200, 900)
        self.background = QtWidgets.QLabel(Flight)
        self.background.setGeometry(QtCore.QRect(0, 0, 1200, 900))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("pic/abstract-blue-geometric-shapes-background_1035-17545.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.flightinfo = QtWidgets.QPushButton(Flight)
        self.flightinfo.setGeometry(QtCore.QRect(490, 460, 93, 28))
        self.flightinfo.setObjectName("flightinfo")
        self.main = QtWidgets.QPushButton(Flight)
        self.main.setGeometry(QtCore.QRect(30, 20, 93, 28))
        self.main.setObjectName("main")
        self.flighttable = QtWidgets.QTableWidget(Flight)
        self.flighttable.setGeometry(QtCore.QRect(0, 100, 1200, 900))
        self.flighttable.setInputMethodHints(QtCore.Qt.ImhNone)
        self.flighttable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.flighttable.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.flighttable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.flighttable.setRowCount(90)
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
        self.flighttable.horizontalHeader().setDefaultSectionSize(140)
        self.flighttable.verticalHeader().setDefaultSectionSize(40)
        self.reload = QtWidgets.QPushButton(Flight)
        self.reload.setGeometry(QtCore.QRect(180, 20, 93, 28))
        self.reload.setObjectName("reload")
        self.search = QtWidgets.QPushButton(Flight)
        self.search.setGeometry(QtCore.QRect(530, 20, 93, 28))
        self.search.setObjectName("search")
        self.textEdit = QtWidgets.QTextEdit(Flight)
        self.textEdit.setGeometry(QtCore.QRect(360, 20, 151, 31))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Flight)
        self.main.clicked.connect(self.flighttable.hide)
        self.flightinfo.clicked.connect(self.flighttable.show)
        self.flightinfo.clicked.connect(self.search.show)
        self.flightinfo.clicked.connect(self.textEdit.show)
        QtCore.QMetaObject.connectSlotsByName(Flight)

    def retranslateUi(self, Flight):
        _translate = QtCore.QCoreApplication.translate
        Flight.setWindowTitle(_translate("Flight", "Form"))
        self.flightinfo.setText(_translate("Flight", "flightinfo"))
        self.main.setText(_translate("Flight", "main"))
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
        self.reload.setText(_translate("Flight", "reload"))
        self.search.setText(_translate("Flight", "search"))
