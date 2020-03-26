#mainWin.py
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from articleContentView.articleContentUI import *


class articleContentWindow(QMainWindow, Ui_MainWindow):
    goBackToTitleTableSignal= pyqtSignal()

    def __init__(self, parent=None):
        super(articleContentWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.goBackToTitleTable)
        #  self.exitSignal.connect(lambda: print("emit"))

    def goBackToTitleTable(self):
        print("go back to TitleTable")
        self.goBackToTitleTableSignal.emit()
        self.close()

    '''
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        print("closed")
        self.exitSignal.emit()
        self.close()
    '''

