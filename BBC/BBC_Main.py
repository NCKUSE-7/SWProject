# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 19:00:00 2020

@author: 施崇祐
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from BBC.BBC_UI import Ui_MainWindow
from BBC.BBC_WebCrawer import CoronavirusTopic
from typing import Dict
import json, sys, multiprocessing, time, os

'''
開了一個Process去更新資料
    * 每10秒會更新一次 (為了demo)
    * 進去任意button後會中止更新
'''

def webCrawl() -> None:
    while True:
        print("Start BBC WebCrawl...")
        CoronavirusTopic()  # generate new data.json in src and download new picture to picture folder
        print("Finish BBC WebCrawl...")
        time.sleep(10)      # 每10秒

class BBCWindow(QtWidgets.QMainWindow):
    goBackToStartupSignal = QtCore.pyqtSignal() # 返回首頁的signal
    process_webcrawling = multiprocessing.Process(target=webCrawl)  # 設定Process

    def __init__(self, parent= None):
        super(BBCWindow, self).__init__(parent)
        self.ui = Ui_MainWindow() # 建立BBC介面
        self.ui.setupUi(self)
        self.ui.pushButton_go_back.clicked.connect(self.goBackToStartup) # 設定回首頁的button
        self.ui.PreLoad() # 先把圖片的路徑跟大小轉成(300*225)，佔存在一個dict中

    '''
    跑Process
    '''
    def processRun(self) -> None:
        if not BBCWindow.process_webcrawling.is_alive():
            BBCWindow.process_webcrawling = multiprocessing.Process(target=webCrawl) # 設定Process
            BBCWindow.process_webcrawling.start() # 開始process

    '''
    回首頁
    '''
    def goBackToStartup(self) -> None:
        self.goBackToStartupSignal.emit() # 傳出回首頁signal
        self.hide() # 將BBC介面藏起來

    '''
    更新介面資訊
        * 每次點進BBC都會刷新一次
    '''
    def update(self) -> None:
        BBCWindow.process_webcrawling.terminate() # 中止process爬蟲
        print("Terminate BBC WebCrawl")
        self.ui.UpdateNews(self.getData()) # 重新讀取data.json，並更新到介面

    '''
    抓取data.json
    '''
    def getData(self) -> Dict:
        with open(Ui_MainWindow.curPath + '/src/data.json', 'r') as f:
            return json.load(f)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    bbc = BBCWindow()
    bbc.show()
    sys.exit(app.exec_())