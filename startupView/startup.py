#mainWin.py
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from startupView.startupUI import *


class startupWindow(QMainWindow, Ui_MainWindow):
    goToTitleTableSignal= pyqtSignal()

    def __init__(self, parent=None):
        super(startupWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.goToTitleTable)
        '''
        self.pushButton_2.clicked.connect(self.goBackToTitleTable)
        self.pushButton_3.clicked.connect(self.goBackToTitleTable)
        self.pushButton_4.clicked.connect(self.goBackToTitleTable)
        '''
        #  self.exitSignal.connect(lambda: print("emit"))

    def goToTitleTable(self):
        print("go to TitleTable")
        self.goToTitleTableSignal.emit()
        self.close()
    '''   
    def goBackToTitleTable(self):
        print("go back to TitleTable")
        self.goBackToTitleTableSignal.emit()
        self.close()
    def goBackToTitleTable(self):
        print("go back to TitleTable")
        self.goBackToTitleTableSignal.emit()
        self.close()
    def goBackToTitleTable(self):
        print("go back to TitleTable")
        self.goBackToTitleTableSignal.emit()
        self.close()


    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        print("closed")
        self.exitSignal.emit()
        self.close()
    '''

