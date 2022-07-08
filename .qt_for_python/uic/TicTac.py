#
# Created By Jasmine Jones
# 

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import time
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import uniform

def wait():
    time.sleep(1)

class Ui_TicWindow(object):

    def bestSpot(self,count):
        match count:
            case 1:
                z = int(uniform(1,10))
                #While button is disabled, cycle through buttons until you find a button that is enabled#
                while self.btn[z].isEnabled() == False:
                    z = int(uniform(1,10))
                #Then Proceed with...
                self.btn[z].setText("O")
                self.btn[z].setEnabled(False)
            case _:
                all = 0
                for a in self.pair:
                    if self.btn[a[0]].text() == "X" and self.btn[a[1]].text() == "X":
                        if self.btn[a[2]].isEnabled() == False:
                            continue
                            
                        else:
                            self.btn[a[2]].setText("O")
                            self.btn[a[2]].setEnabled(False)
                            break
                    else:
                        all = all + 1
                
                if all == 23:
                    z = int(uniform(1,10))
                    while self.btn[z].isEnabled() == False:
                        z = int(uniform(1,10))
                    self.btn[z].setText("O")
                    self.btn[z].setEnabled(False)

    def check(self,xo):
        #Column#
        if self.pushButton_3.text() == xo and self.pushButton_2.text() == xo and self.pushButton.text() == xo:
            return True
        elif self.pushButton_8.text() == xo and self.pushButton_6.text() == xo and self.pushButton_4.text() == xo:
            return True   
        elif self.pushButton_9.text() == xo and self.pushButton_7.text() == xo and self.pushButton_5.text() == xo:
            return True 
        #Row#
        elif self.pushButton.text() == xo and self.pushButton_6.text() == xo and self.pushButton_7.text() == xo:
            return True
        elif self.pushButton_2.text() == xo and self.pushButton_4.text() == xo and self.pushButton_5.text() == xo:
            return True
        elif self.pushButton_3.text() == xo and self.pushButton_8.text() == xo and self.pushButton_9.text() == xo:
            return True
        #Diagonal#
        elif self.pushButton_9.text() == xo and self.pushButton_4.text() == xo and self.pushButton.text() == xo:
            return True
        elif self.pushButton_7.text() == xo and self.pushButton_4.text() == xo and self.pushButton_3.text() == xo:
            return True
        else:
            return False

    def opponent(self, count):
        xo = "X"
        if count == 9 and self.check("X") == False and self.check("O") == False:
            self.label.setText("Tie!")
            for i in self.btn:
                self.btn[i].setEnabled(False)
        elif self.check(xo) == True:
            self.label.setText("X's Won!")
            for i in self.btn:
                self.btn[i].setEnabled(False)

        elif self.check(xo) == False:
            self.bestSpot(self.count)
            self.count = self.count +1
            if self.check("O") == True:
                self.label.setText("O's Won!")
                for i in self.btn:
                    self.btn[i].setEnabled(False)           

    def x_btn(self,i):
        xo = "O"
        
        if self.check(xo) == False:
            self.btn[i].setText("X")
            self.btn[i].setEnabled(False)
            self.label.setText("....")
            self.count = self.count + 1
            self.opponent(self.count)
        else:
            self.label.setText("O's Won!")
            for i in self.btn:
                self.btn[i].setEnabled(False)

    def retry_btn(self):
        for i in self.btn:
            self.btn[i].setText("")
            self.btn[i].setEnabled(True)
    
        self.label.setText("X's Turn")
        self.count = 0

    def setupUi(self, MainWindow):
        self.count = 0
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton.clicked.connect(lambda: self.x_btn(1))

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.pushButton_2.clicked.connect(lambda: self.x_btn(2))

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.pushButton_3.clicked.connect(lambda: self.x_btn(3))
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 2, 1, 1, 1)
        self.pushButton_4.clicked.connect(lambda: self.x_btn(4))

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 2, 2, 1, 1)
        self.pushButton_5.clicked.connect(lambda: self.x_btn(5))

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 1, 1, 1, 1)
        self.pushButton_6.clicked.connect(lambda: self.x_btn(6))

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 1, 2, 1, 1)
        self.pushButton_7.clicked.connect(lambda: self.x_btn(7))

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 3, 1, 1, 1)
        self.pushButton_8.clicked.connect(lambda: self.x_btn(8))

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 3, 2, 1, 1)
        self.pushButton_9.clicked.connect(lambda: self.x_btn(9))

        #Retry Button#
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 4, 1, 1, 1)
        self.pushButton_10.clicked.connect(self.retry_btn)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn = {
            1: self.pushButton, 2:self.pushButton_2, 3:self.pushButton_3, 
            4: self.pushButton_4, 5:self.pushButton_5, 6:self.pushButton_6, 
            7: self.pushButton_7, 8:self.pushButton_8, 9:self.pushButton_9}

        self.pair = {
            (1,6,7),(1,7,6),(1,2,3),(1,3,2),(1,4,9),(1,9,4),
            (2,4,5),(2,5,4),(2,3,1),
            (3,8,9),(3,9,8),(3,4,7),(3,7,4),
            (6,4,8),(6,8,4),(6,7,1),
            (7,5,9),(7,9,5),(7,4,3),
            (5,4,2),
            (9,8,3),(9,5,7),(9,4,1),
            (8,4,6)
        }

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_10.setText(_translate("MainWindow", "Retry?"))
        #self.pushButton_9.setText(_translate("MainWindow", "X"))
        #self.pushButton.setText(_translate("MainWindow", "X"))
        #self.pushButton_3.setText(_translate("MainWindow", "X"))
        #self.pushButton_2.setText(_translate("MainWindow", "X"))
        #self.pushButton_4.setText(_translate("MainWindow", "X"))
        #self.pushButton_5.setText(_translate("MainWindow", "X"))
        #self.pushButton_7.setText(_translate("MainWindow", "X"))
        #self.pushButton_6.setText(_translate("MainWindow", "X"))
        #self.pushButton_8.setText(_translate("MainWindow", "X"))
        self.label.setText(_translate("MainWindow", "Your Turn..."))

if __name__ == "__main__": #### Creates Scene ####
    import sys
    app = QApplication(sys.argv)
    ui = Ui_TicWindow()
    win = QMainWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec())