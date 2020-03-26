from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from TitleTableView.TitleTable import TitleTableWindow

from startupView.startup import startupWindow
from articleContentView.articleContent import articleContentWindow


class ViewController:
    def loadArticleContent(self,list):
        self.articleContentWindow= articleContentWindow()
        self.articleContentWindow.goBackToTitleTableSignal.connect(self.loadTitleTable)
        self.articleContentWindow.show()
        self.articleContentWindow.label_title.setText(list[0])
        self.articleContentWindow.textBrowser.setHtml(list[1])

    def loadTitleTable(self):
        self.TitleTableWindow=TitleTableWindow()

        self.TitleTableWindow.goBackToStartupSignal.connect(self.loadStartup)
        self.TitleTableWindow.callArticleContent.connect(self.loadArticleContent)
        self.TitleTableWindow.show()
    def loadStartup(self):
        self.startupWindow=startupWindow()
        self.startupWindow.goToTitleTableSignal.connect(self.loadTitleTable)
        self.startupWindow.show()
    '''
    def addMenu(self):
        self.menuUI=startupView.testUI.Ui_MainWindow()
        self.menuUI.setupUi(self.articleContentWindow)
    '''



if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = ViewController()
    view.loadStartup()
    sys.exit(app.exec_())

