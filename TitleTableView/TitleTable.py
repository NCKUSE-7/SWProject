
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from TitleTableView import TitelTableUI


class TitleTableWindow(QMainWindow):
    callArticleContent = pyqtSignal(list)
    goBackToStartupSignal=pyqtSignal()
    def __init__(self, parent= None):
        super(TitleTableWindow, self).__init__(parent)
        self.ui=TitelTableUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.callArticleContentfunc)
        self.ui.pushButton_3.clicked.connect(self.callArticleContentfunc)
        self.ui.pushButton_4.clicked.connect(self.callArticleContentfunc)
        self.ui.pushButton_5.clicked.connect(self.callArticleContentfunc)
        self.ui.pushButton_6.clicked.connect(self.callArticleContentfunc)
        self.ui.pushButton_7.clicked.connect(self.callArticleContentfunc)
        self.ui.pushButton_9.clicked.connect(self.goBackToStartup)
        self.articleArray=[0,0]
        self.titleArray=[0,0]
        self.getTitleAndArticleContent()

    def getTitleAndArticleContent(self):

        str1="title"
        str2="article"

        for index in range(2,8):
            self.articleArray.append(str2+str(index))
            self.titleArray.append(str1+str(index))
            print(self.articleArray[index])
            print(self.titleArray[index])

        for index in range(2,8):
            buttonName="pushButton_" + str(index)
            pushButton = self.findChild(QPushButton,buttonName )
            pushButton.setText(self.titleArray[index])

    def goBackToStartup(self):
        self.goBackToStartupSignal.emit()
        self.close()


    def callArticleContentfunc(self):
        print("callArticleContent clicked")
        sending_button = self.sender()
        buttonName=sending_button.objectName()
        pos=buttonName.find("_")
        index=int(buttonName[pos+1])
        list=[self.titleArray[index],self.articleArray[index]]


        self.callArticleContent.emit(list)
        #self.callArticleContent.emit("fdsjkfsjdk")
        self.close()

    def btnExitClicked(self):
        print("Exit clicked")
        self.close()


