# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbc_news_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 19:00:00 2020

@author: 施崇祐
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import json, pathlib

##### My Code #####
'''
新聞格式
    * MyGroupBox
        * QVBoxLayout (垂直排序)
            * label (設定圖片上去)
            * label (設定標題上去)
                * 文字太長會影響GroupBox大小，因此文字超過12個就...
                * 當滑鼠hover變成淺藍色 離開則變回來
'''
class MyGroupBox(QtWidgets.QGroupBox):
    '''
    每個標題label
        * 設定進入label 以及 離開label函數
    '''
    class MyTitleLabel(QtWidgets.QLabel):
        def __init__(self, *args, **kwargs):
            QtWidgets.QLabel.__init__(self, *args, **kwargs)
            # 設定文字風格
            font = QtGui.QFont()
            font.setPointSize(10) # 文字大小為10
            font.setBold(True)    # 粗體
            font.setWeight(75)    # 文字粗細為75
            self.setFont(font)    # 設定文字
            self.setAlignment(QtCore.Qt.AlignCenter)  # 靠其label中間

        # 進入label (hover)
        def enterEvent(self, event):
            self.setStyleSheet("QLabel {color: #1167ad};") # 改成淺藍色 https://www.google.com/search?ei=4Hd7XuHNOYPVmAXA77HwCw&q=color+%231167AD&oq=color+%231167AD&gs_l=psy-ab.3...504980.504980..505798...0.0..0.157.285.2j1......0....2j1..gws-wiz.-CHIx9g7yl0&ved=0ahUKEwjhvdDP97XoAhWDKqYKHcB3DL4Q4dUDCAs&uact=5

        # 離開label
        def leaveEvent(self, event):
            self.setStyleSheet("QLabel {color: #000000};") # 改回黑色

    # 建立標題label函數
    def createMyTitleLabel(self, title):
        return MyGroupBox.MyTitleLabel(title)

    def __init__(self, title, picture_link, news_url, *args, **kwargs):
        QtWidgets.QGroupBox.__init__(self, *args, **kwargs)
        self.picture_link = picture_link
        self.news_url = news_url

        # 定義 picture label
        # 讓 picture label 可以點
        # 讓 picture 符合label的size
        self.picture = QtWidgets.QLabel()
        self.picture.mousePressEvent = self.Clicked_Label
        self.picture.setScaledContents(True)

        # 設定圖片
        if self.picture_link not in Ui_MainWindow.webImageDict:
            Ui_MainWindow.webImageDict[self.picture_link] = QtGui.QPixmap(
                QtGui.QImage(self.picture_link).smoothScaled(300, 225))
        self.picture.setPixmap(Ui_MainWindow.webImageDict[self.picture_link])

        # 設定title長度最大為12
        # 建立title label
        # 讓title label可以點
        if len(title) > 12:
            title = title[:12] + "..."
        self.title = self.createMyTitleLabel(title)
        self.title.mousePressEvent = self.Clicked_Label

        # 設定垂直layout
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.picture)
        vbox.addWidget(self.title)
        vbox.addStretch(1)
        self.setLayout(vbox)

    '''
    被點的時候開啟連結
    '''
    def Clicked_Label(self, event):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(self.news_url))
####################

'''
新聞版面
'''
class Ui_MainWindow(object):
    webImageDict = {} # 佔存title對應的圖片，格式為 {標題: QPixmap()}
    curPath = str(pathlib.Path(__file__).parent.absolute()) # 設定絕對路徑 (因為執行後路徑是main.py的執行路徑)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1200, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea_mainTable = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_mainTable.setGeometry(QtCore.QRect(0, 150, 1200, 750))
        self.scrollArea_mainTable.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea_mainTable.setObjectName("scrollArea_mainTable")
        self.scrollArea_mainTable.setWidget(self.scrollAreaWidgetContents)
        self.label_bbc_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_bbc_logo.setGeometry(QtCore.QRect(0, 0, 600, 75))
        self.label_bbc_logo.setObjectName("label_bbc_logo")
        self.label_bbc_red_bar = QtWidgets.QLabel(self.centralwidget)
        self.label_bbc_red_bar.setGeometry(QtCore.QRect(0, 75, 1200, 75))
        self.label_bbc_red_bar.setObjectName("label_bbc_red_bar")
        self.pushButton_go_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_go_back.setGeometry(QtCore.QRect(900, 25, 300, 50))
        self.pushButton_go_back.setObjectName("pushButton_go_back")
        MainWindow.setCentralWidget(self.centralwidget)

        ##### My Code #####
        MainWindow.setStyleSheet("QMainWindow {background: 'white';}") # 將背景轉成白色
        self.label_bbc_logo.setPixmap(QtGui.QPixmap(Ui_MainWindow.curPath+'/src/BBC.png'))  # 設定白色的BBC logo
        self.label_bbc_logo.mousePressEvent = self.Clicked_label_bbc_logo # 讓白色的BBC logo能被按
        self.label_bbc_red_bar.setPixmap(QtGui.QPixmap(Ui_MainWindow.curPath+'/src/NEWS_Chinese.png')) # 設定紅色的BBC logo
        self.label_bbc_red_bar.mousePressEvent = self.Clicked_label_bbc_red_bar # 讓紅色的BBC logo能被按
        ####################

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ##### My Code #####
    '''
    更新版面
        * returnData = {標題: [圖片位置，新聞網址，對應的圖片連結, 抓取時間]}
    '''
    def UpdateNews(self, returnData):
        # 刪除所有的新聞
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().deleteLater()

        # 新增新聞
        #   * 依照時間順續排序 (由新到舊)
        #   * 3*3排列
        for i, (key, values) in enumerate(sorted(returnData.items(), key=lambda item: item[1][3], reverse=True)):
            self.gridLayout.addWidget(MyGroupBox(key, values[0], values[1]), i//3, i%3)

    '''
    預存 data.json中的圖片
        * 轉成(300*225)存在webImageDict變數中
        * webImageDict = {標題: 圖片(QPixmap)}
    '''
    def PreLoad(self):
        import os
        if os.path.exists(Ui_MainWindow.curPath + "/src/data.json"):     # 如果有data.json這個檔案
            with open(Ui_MainWindow.curPath+'/src/data.json', 'r') as f: # 開啟檔案
                returnData = json.load(f)                       # 讀取到returnData

            for key, values in returnData.items(): # 將資訊抓出來
                Ui_MainWindow.webImageDict[values[0]] = QtGui.QPixmap(QtGui.QImage(values[0]).smoothScaled(300, 225)) # 轉成QPixmap 並轉成 (300*225)

    '''
    按下label開啟連結
    '''
    def Clicked_label_bbc_logo(self, event):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://www.bbc.com/'))

    def Clicked_label_bbc_red_bar(self, event):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://www.bbc.com/zhongwen/trad'))

    ####################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BBC News"))
        self.pushButton_go_back.setText(_translate("MainWindow", "回首頁"))