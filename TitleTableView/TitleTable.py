
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import json
from crawler.ptt import *
from TitleTableView import TitelTableUI


class TitleTableWindow(QMainWindow):
    callArticleContent = pyqtSignal(dict)
    goBackToStartupSignal=pyqtSignal()
    pageNum=0
    def __init__(self, parent= None):
        super(TitleTableWindow, self).__init__(parent)
        self.ui=TitelTableUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label_loading.hide()
        self.ui.pushButton_2.clicked.connect(self.callArticleContentfunc)
        self.ui.pushButton_3.clicked.connect(self.callArticleContentfunc)
        self.ui.pushButton_4.clicked.connect(self.callArticleContentfunc)
        self.ui.pushButton_5.clicked.connect(self.callArticleContentfunc)
        self.ui.pushButton_6.clicked.connect(self.callArticleContentfunc)
        self.ui.pushButton_7.clicked.connect(self.callArticleContentfunc)
        self.ui.pushButton_9.clicked.connect(self.goBackToStartup)
        self.ui.pushButton_nextPage.clicked.connect(self.nextPage)
        self.ui.pushButton_prePage.clicked.connect(self.prePage)
        self.ui.pushButton_update.clicked.connect(self.updateTitleTable)
        self.articleArray=[0,0]
        self.titleArray=[0,0]
        self.getTitleAndArticleContent()
        self.setButtonTitle()
    def updateTitleTable(self):
        self.ui.label_loading.show()
        parse_articles(start, end, board)
        self.ui.label_loading.hide()

    def prePage(self):
        self.pageNum=self.pageNum+1
        self.setButtonTitle()


    def nextPage(self):
        if self.pageNum > 0 :
            self.pageNum=self.pageNum-1
            self.setButtonTitle()


    def getTitleAndArticleContent(self):

        #with open('crawler/output.json', 'r',encoding='utf-8') as f:
        with open('output.json', 'r',encoding='utf-8') as f:
            data = f.readlines()

        f.close()
        for article in data:
            article=article[0:len(article)-2]
            article=json.loads(article)
            self.articleArray.append(article)
            print(article)



    def setButtonTitle(self):
        for index in range(2,8):
            buttonName="pushButton_" + str(index)
            pushButton = self.findChild(QPushButton,buttonName )
            pushButton.setText(self.articleArray[index+self.pageNum*6]['article_title'])

    def goBackToStartup(self):
        self.goBackToStartupSignal.emit()
        self.close()


    def callArticleContentfunc(self):
        print("callArticleContent clicked")
        sending_button = self.sender()
        buttonName=sending_button.objectName()
        pos=buttonName.find("_")
        index=int(buttonName[pos+1])

        self.callArticleContent.emit(self.articleArray[index+self.pageNum*6])
        self.close()

    def btnExitClicked(self):
        print("Exit clicked")
        self.close()


