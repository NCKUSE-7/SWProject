from __future__ import unicode_literals
import json
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets
from VirusCrawler.VirusCrawlerCode import crawler
from VirusCrawler.VirusCrawlerUI import Ui_Flight


class Flight(QtWidgets.QMainWindow):
    def __init__(self):
        super(Flight, self).__init__()
        self.ui = Ui_Flight()
        self.ui.setupUi(self)
#        self.ui.flighttable.hide()
        self.ui.retranslateUi(Fl)
        self._translate = QtCore.QCoreApplication.translate
        self.ui.flighttable.setColumnWidth(0, 125)
        self.ui.flighttable.setColumnWidth(1, 125)
        self.ui.flighttable.setColumnWidth(2, 220)
        self.ui.flighttable.setColumnWidth(5, 125)
        self.loaddata()

    def loaddata(self) :
        with open('C:\Code\\flightinfo\VirusCrawler\\fi_out.json') as f:
            self.FData = json.load(f, encoding='utf-8')
        num = len(self.FData)
        self.ui.flighttable.setRowCount(num)
        for i in range(num):
            for j in range(6):
                if j == 3:
                    url = self.FData["flight" + str(i)][2]  #'https://web.taoyuan-airport.com/upload/airlogo/CI.gif'
#                   data = urllib.request.urlopen(url).read()
                    x = url.split('/')
                    image = Image.open('C:\Code\\flightinfo\VirusCrawler\pic\\' + x[5])
                    qimage = ImageQt(image)
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap.fromImage(qimage), QtGui.QIcon.Normal, QtGui.QIcon.On)
                    self.ui.item.setIcon(icon)
                    self.ui.flighttable.setItem(0, j, self.ui.item)
#--------------------------------------------
#                    image = QtGui.QImage()
#                    image.loadFromData(data)
#                    icon = QtGui.QIcon()
#                    icon.addPixmap(QtGui.QPixmap(image), QtGui.QIcon.Normal, QtGui.QIcon.On)
#                    self.ui.item.setIcon(icon)
#                    self.ui.item = self.ui.flighttable.item(0, j)
#---------------------------------------
                self.ui.item = QtWidgets.QTableWidgetItem()
                self.ui.flighttable.setItem(i, j, self.ui.item)
        for i in range(num):
            for j in range(6):
                self.ui.item = self.ui.flighttable.item(i, j)
                if j > 1:
                    self.ui.item.setText(self._translate("Flight", self.FData["flight" + str(i)][j + 1]))
                else:
                    self.ui.item.setText(self._translate("Flight", self.FData["flight" + str(i)][j]))
        self.ui.flighttable.itemActivated.connect(self.itemActivated_event)
        self.ui.reload.clicked.connect(self.readj)

    def readj(self):
        self.FData = json.loads(crawler(), encoding='utf-8')
        self.loaddata()

    def itemActivated_event(self,item):
        json_file = open("C:\Code\\flightinfo\VirusCrawler\jsonfiles\FlightUrl", "r", encoding='utf-8')
        Flight.FData = json.load(json_file)
        json_file.close()
        if (item.text() == '全亞州航空' or item.text() == '中華航空' or item.text() == '馬來西亞' or item.text() == '泰國獅子航空' or item.text() == '土耳其航空' \
                or item.text() == '達美航空' or item.text() == '泰國航空' or item.text() == '香港航空' or item.text() == '日本航空' or item.text() == '越南航空' \
                or item.text() == '紐西蘭航空' or item.text() == '印度航空' or item.text() == '酷鳥航空' or item.text() == '夏威夷航空' or item.text() == '長榮航空' \
                or item.text() == '東方航空' or item.text() == '曼谷航空' or item.text() == '星宇航空' or item.text() == '聯合航空'or item.text() == '法國航空' \
                or item.text() == '華信航空' or item.text() == '全日本航空' or item.text() == '星悅航空' or item.text() == '新加坡航空' or item.text() == '汶萊航空' \
                or item.text() == '勝安航空' or item.text() == '馬印航空' or item.text() == '國泰港龍' or item.text() == '菲律賓航空' or item.text() == '大韓航空' \
                or item.text() == '韓亞航空' or item.text() == '酷航' or item.text() == '樂桃航空' or item.text() == '巴拿馬航空' or item.text() == '荷蘭航空' \
                or item.text() == '加拿大航空' or item.text() =='澳洲航空' or item.text() == '巴澤航空' or item.text() == '德國航空' or item.text() == '以色列航空')\
                or item.text() == '真航空':
            QtGui.QDesktopServices.openUrl(QtCore.QUrl(Flight.FData[item.text()]))
        else:
            print(item.text())


#def url_to_image(url):
#    # download the image, convert it to a NumPy array, and then read
#    # it into OpenCV format
#    resp = urllib.urlopen(url)
#    image = np.asarray(bytearray(resp.read()), dtype="uint8")
#    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
#    # return the image
#    return image


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Fl = QtWidgets.QWidget()
    #    ui = Ui_Flight()     #original
    Fl = Flight()
    #    Fl.ui.setupUi(Fl)
    Fl.show()
    sys.exit(app.exec_())