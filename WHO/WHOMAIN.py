from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QFrame,QAbstractItemView, QTableWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from WHO.WHOUI import Ui_MainWindow
import json
import sys
import random
number=0
tTotalcases='0'

class MainWindow(QtWidgets.QMainWindow):


    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #設定標題和圖示
        self.setWindowTitle('防疫一把罩')
        self.setWindowIcon(QtGui.QIcon('德賽.jpg'))
        #隱藏標題和圖示
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #設定背景
       # image=QtGui.QPixmap()
       # image.load('D:\PYQT\美景.jpg')
       # image=image.scaled(self.width(),self.height())
        palette=QtGui.QPalette()
        palette.setBrush(self.backgroundRole(),QtGui.QColor(80,150,210))#RGB
        self.setPalette(palette)



        #設定選項(離開)
        self.ui.retranslateUi(self)
        self.ui.actionClose.setShortcut('Esc')
        self.ui.actionClose.triggered.connect(app.exit)
        # 設定ComboBox
      #  choices = ['','病例數','死亡人數','痊癒人數']
      #  self.ui.comboBox.addItems(choices)
      #  self.ui.comboBox.currentIndexChanged.connect(self.display)
      #  self.display()
        # 設定QLCDNumber
       # self.ui.lcdNumber.display(number)
        # 設定Qtable
        self.ui.font = QFont('標楷體', 20)
        self.ui.font.setBold(True)  # 设置字体加粗

        self.ui.tableWidget.setColumnCount(10)
        self.ui.tableWidget.setRowCount(250)
        self.ui.tableWidget.setHorizontalHeaderLabels(['國家', '感染人數', '死亡人數','痊癒人數','感染新增','死亡新增','Active cases','重症','TotCases1M','TotDeaths1M'])  # 设置表头文字
        self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        """
        # 讀取Txt檔
        a=0
        with open('D:\PYQT\Countries.txt', 'r', encoding='utf-8') as file:
            for countries in file:
                self.ui.tableWidget.setItem(a, 0, QTableWidgetItem(countries))
                #print(countries)
                a=a+1
        b=0
        with open('D:\PYQT\TotalCases.txt', 'r', encoding='utf-8') as file:
            for TotalCases in file:
                self.ui.tableWidget.setItem(b, 1, QTableWidgetItem(TotalCases))
                b=b+1
                print(TotalCases)
        c = 0
        with open('D:\PYQT\TotalDeaths.txt', 'r', encoding='utf-8') as file:
            for TotalCases in file:
                self.ui.tableWidget.setItem(c, 2, QTableWidgetItem(TotalCases))
                c = c + 1
        b = 0
        with open('D:\PYQT\TotalRecovered.txt', 'r', encoding='utf-8') as file:
            for TotalCases in file:
                self.ui.tableWidget.setItem(b, 3, QTableWidgetItem(TotalCases))
                b = b + 1
        b = 0
        with open('D:/PYQT/NewCases.txt', 'r', encoding='utf-8') as file:
            for TotalCases in file:
                self.ui.tableWidget.setItem(b, 4, QTableWidgetItem(TotalCases))
                b = b + 1
        b = 0
        with open('D:/PYQT/NewDeaths.txt', 'r', encoding='utf-8') as file:
            for TotalCases in file:
                self.ui.tableWidget.setItem(b, 5, QTableWidgetItem(TotalCases))
                b = b + 1
        b = 0
        with open('D:/PYQT/ActiveCases.txt', 'r', encoding='utf-8') as file:
            for TotalCases in file:
                self.ui.tableWidget.setItem(b, 6, QTableWidgetItem(TotalCases))
                b = b + 1
        b = 0
        with open('D:/PYQT/SeriousCritical.txt', 'r', encoding='utf-8') as file:
            for TotalCases in file:
                self.ui.tableWidget.setItem(b, 7, QTableWidgetItem(TotalCases))
                b = b + 1
        b = 0
        with open('D:/PYQT/TotCases1M.txt', 'r', encoding='utf-8') as file:
            for TotalCases in file:
                self.ui.tableWidget.setItem(b, 8, QTableWidgetItem(TotalCases))
                b = b + 1
        b = 0
        with open('D:/PYQT/TotDeaths1M.txt', 'r', encoding='utf-8') as file:
            for TotalCases in file:
                self.ui.tableWidget.setItem(b, 9, QTableWidgetItem(TotalCases))
                b = b + 1

        """

        # 設定字大小
        self.ui.label.setFont(QtGui.QFont('標楷體',30))
       # self.ui.label_2.setFont(QtGui.QFont('標楷體', 25))
        self.ui.label_3.setFont(QtGui.QFont('標楷體', 25))
        #self.ui.pushButton_3.setFont(QtGui.QFont('標楷體', 25))
        self.ui.pushButton_2.setFont(QtGui.QFont('標楷體', 30))
        self.ui.pushButton.setFont(QtGui.QFont('標楷體', 25))

        pixmap = QPixmap("D:\PYQT\德賽.jpg")  # 按指定路径找到图片，注意路径必须用双引号包围，不能用单引号
        self.ui.label.setPixmap(pixmap)
       # self.ui.label_2.setText('台灣目前的')
        self.ui.label_3.setText('COVID-19 Situation Table')
        #self.ui.pushButton_3.setText('台灣目前狀態')
        self.ui.pushButton_2.setText('回首頁')
        self.ui.pushButton.setText("刷新")


        # 連接按鈕與爬蟲功能
        self.ui.pushButton.clicked.connect(self.Web_Crawler)
        #連接按鈕與刷新功能
        self.ui.pushButton.clicked.connect(self.Reset)
        #台灣狀態
        #self.ui.pushButton_3.clicked.connect(self.buttonClicked)

    def Web_Crawler(empty):
        Total_case = open('Coronavirus_Cases.txt', 'wt', encoding="utf-8")
        Countries_two = open('Countries.txt', 'wt', encoding="utf-8")
        TotalCases = open('TotalCases.txt', 'wt', encoding="utf-8")
        NewCases = open('NewCases.txt', 'wt', encoding="utf-8")
        TotalDeaths = open('TotalDeaths.txt', 'wt', encoding="utf-8")
        NewDeaths = open('NewDeaths.txt', 'wt', encoding="utf-8")
        TotalRecovered = open('TotalRecovered.txt', 'wt', encoding="utf-8")
        ActiveCases = open('ActiveCases.txt', 'wt', encoding="utf-8")
        SeriousCritical = open('SeriousCritical.txt', 'wt', encoding="utf-8")
        TotCases1M = open('TotCases1M.txt', 'wt', encoding="utf-8")
        TotDeaths1M = open('TotDeaths1M.txt', 'wt', encoding="utf-8")

        import urllib.request as req
        url = "https://www.worldometers.info/coronavirus/#countries"
        request = req.Request(url, headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        })
        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")

        import bs4
        root = bs4.BeautifulSoup(data, "html.parser")

        Coronavirus_Cases = root.find_all("div", class_="maincounter-number")
        for maincounter_number in Coronavirus_Cases:
            Total_case.write(str(maincounter_number.span.string))
            Total_case.write("\n")

        Countries = root.find_all("td", style="font-weight: bold; font-size:15px; text-align:left;")
        Main = root.find_all("td")

        china = []
        for i in range(9):
            china.append(str(Main[(int)(len(Main) / 2) - 19 + i].string))
        china_num = china[0].split(',')

        Count = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        check_re = 0
        for Country in Countries:
            if Country.string == "China":
                break
            check = 0
            country_num = str(Main[Count[1]].string).split(',')
            if check_re == 1:
                check = 0
            elif len(china_num) > len(country_num):
                check = 1
                check_re = 1
            elif len(china_num) == len(country_num):
                for i in range(len(china_num)):
                    check = 0
                    if int(china_num[i]) > int(country_num[i]):
                        check = 1
                        check_re = 1
                        break
                    elif int(china_num[i]) < int(country_num[i]):
                        break
            if check == 1:
                Countries_two.write("China" + "\n")
                TotalCases.write(china[0] + "\n")
                NewCases.write(china[1] + "\n")
                TotalDeaths.write(china[2] + "\n")
                NewDeaths.write(china[3] + "\n")
                TotalRecovered.write(china[4] + "\n")
                ActiveCases.write(china[5] + "\n")
                SeriousCritical.write(china[6] + "\n")
                TotCases1M.write(china[7] + "\n")
                TotDeaths1M.write(china[8] + "\n")

            Countries_two.write(str(Country.string) + "\n")
            TotalCases.write(str(Main[Count[1]].string) + "\n")
            NewCases.write(str(Main[Count[2]].string) + "\n")
            TotalDeaths.write(str(Main[Count[3]].string) + "\n")
            NewDeaths.write(str(Main[Count[4]].string) + "\n")
            TotalRecovered.write(str(Main[Count[5]].string) + "\n")
            ActiveCases.write(str(Main[Count[6]].string) + "\n")
            SeriousCritical.write(str(Main[Count[7]].string) + "\n")
            TotCases1M.write(str(Main[Count[8]].string) + "\n")
            TotDeaths1M.write(str(Main[Count[9]].string) + "\n")
            for i in range(10):
                Count[i] = Count[i] + 10

        Total_case.close()
        Countries_two.close()
        TotalCases.close()
        NewCases.close()
        TotalDeaths.close()
        NewDeaths.close()
        TotalRecovered.close()
        ActiveCases.close()
        SeriousCritical.close()
        TotCases1M.close()
        TotDeaths1M.close()

    # Web_Crawler()





    def Reset(self):
        # 讀取Txt檔
        t = 0
        a = 0
        tTotalcases ='0'
        with open('Countries.txt', 'r', encoding='utf-8') as file:
            for countries in file:
                self.ui.tableWidget.setItem(a, 0, QTableWidgetItem(countries))
                a= a + 1
        b = 0
        with open('TotalCases.txt', 'r', encoding='utf-8') as file:
            for TotalCases in file:
                self.ui.tableWidget.setItem(b, 1, QTableWidgetItem(TotalCases))
                b = b + 1
               # print(TotalCases)
        c = 0
        with open('TotalDeaths.txt', 'r', encoding='utf-8') as file:
            for TotalCases in file:
                self.ui.tableWidget.setItem(c, 2, QTableWidgetItem(TotalCases))
                c = c + 1
        b = 0
        with open('TotalRecovered.txt', 'r', encoding='utf-8') as file:
            for TotalCases in file:
                self.ui.tableWidget.setItem(b, 3, QTableWidgetItem(TotalCases))
                b = b + 1
        b = 0
        with open('NewCases.txt', 'r', encoding='utf-8') as file:
            for TotalCases in file:
                self.ui.tableWidget.setItem(b, 4, QTableWidgetItem(TotalCases))
                b = b + 1
        b = 0
        with open('NewDeaths.txt', 'r', encoding='utf-8') as file:
            for TotalCases in file:
                self.ui.tableWidget.setItem(b, 5, QTableWidgetItem(TotalCases))
                b = b + 1
        b = 0
        with open('ActiveCases.txt', 'r', encoding='utf-8') as file:
            for TotalCases in file:
                self.ui.tableWidget.setItem(b, 6, QTableWidgetItem(TotalCases))
                b = b + 1
        b = 0
        with open('SeriousCritical.txt', 'r', encoding='utf-8') as file:
            for TotalCases in file:
                self.ui.tableWidget.setItem(b, 7, QTableWidgetItem(TotalCases))
                b = b + 1
        b = 0
        with open('TotCases1M.txt', 'r', encoding='utf-8') as file:
            for TotalCases in file:
                self.ui.tableWidget.setItem(b, 8, QTableWidgetItem(TotalCases))
                b = b + 1
        b = 0
        with open('TotDeaths1M.txt', 'r', encoding='utf-8') as file:
            for TotalCases in file:
                self.ui.tableWidget.setItem(b, 9, QTableWidgetItem(TotalCases))
                b = b + 1

    def buttonClicked(self):
       # self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(tTotalCases))
        self.ui.label.setText(' 感染人數:\n 死亡人數:\n 痊癒人數: ')



    def display(self):

        with open('TotalCases.txt', 'r', encoding='utf-8') as file:
           for  TotalCases in file:
                self.ui.label.setText('%s  '  % TotalCases)




if __name__ == "__main__":
        app = QtWidgets.QApplication([])
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())