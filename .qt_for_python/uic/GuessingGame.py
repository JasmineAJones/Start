
from random import uniform

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractScrollArea, QWidget, QSizePolicy

import time

from datetime import datetime

### Below is a guessing gambling game. You have a choice between 1,2 or 3 And can choose your wager amount based on how much money you have. You start out with $200 and the game ends 
### once you've accumulated $10,000 or more



def rand(gues):
    x = int(uniform(1,4))
    if gues == x:
        return True
    return False

def lost(m, percent):
    money = m*100
    t = round(((money - (percent * money))/100),2)
    return t

def won(m, percent):
    money = m*100
    t = round(((money + (percent * money))/100),2)
    return t

def toIntp(p):
    speChars = "%"
    pp = p.replace(speChars, '')
    p = float(pp)/100
    return p

def toIntm(p):
    speChars = "$"
    pp = p.replace(speChars, '')
    p = float(pp)
    return p

def checkmon(m):
    if m <= 0.01:
        return True
    elif m >= 400:
        return 'won'


class Ui_GuessWindow(object):
    
    def clicked_btn(self,n):
        self.winLose.clear()
        m = toIntm(self.money.toPlainText())
        p = toIntp(self.percentBox.currentText())

        if rand(n) == True:
            time.sleep(1)
            self.winLose.setText("You Won!!")
            self.money.setText("$"+str(won(m,p)))
            
        else:
            time.sleep(1)
            self.winLose.setText("You Lost :(") 
            self.money.setText("$"+str(lost(m,p)))

            m = toIntm(self.money.toPlainText())
            if checkmon(m) == True:
                self.openLoseWindow()
            elif checkmon(m) == 'won':
                self.openWinWindow()  
        self.count = self.count+1

 
    def openLoseWindow(self): ### Opening lose window
                                                 
        self.ui = Ui_LoseForm()
        self.LostWindow = QWidget()
        self.ui.setupUi(self.LostWindow,self.count)
        self.LostWindow.show()

    def openWinWindow(self): ### Opening win window
                                                 
        self.ui = Ui_WinForm()
        self.WinWindow = QWidget()
        self.ui.setupUi(self.WinWindow,self.money.toPlainText())
        self.WinWindow.show()

    def setupUi(self, GuessWindow):
        self.count = 1
        
        GuessWindow.setObjectName("GuessWindow")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        GuessWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(GuessWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.moneyLabel = QtWidgets.QLabel(self.centralwidget)
        self.moneyLabel.setObjectName("moneyLabel")
        self.gridLayout.addWidget(self.moneyLabel, 2, 1, 1, 1)

        self.percentLabel = QtWidgets.QLabel(self.centralwidget)
        self.percentLabel.setObjectName("percentLabel")
        self.gridLayout.addWidget(self.percentLabel, 4, 1, 1, 2)

        self.winLose = QtWidgets.QTextBrowser(self.centralwidget)
        self.winLose.setMaximumSize(QtCore.QSize(700, 20))
        self.winLose.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.winLose.setFrameShadow(QtWidgets.QFrame.Plain)
        self.winLose.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.winLose.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.winLose.setObjectName("winLose")
        self.gridLayout.addWidget(self.winLose, 10, 1, 1, 4)


        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setObjectName("one")
        self.gridLayout.addWidget(self.one, 8, 2, 1, 1)
        self.one.clicked.connect(lambda: self.clicked_btn(1))

        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setObjectName("two")
        self.gridLayout.addWidget(self.two, 8, 3, 1, 1)
        self.two.clicked.connect(lambda: self.clicked_btn(2))

        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setObjectName("three")
        self.gridLayout.addWidget(self.three, 8, 4, 1, 1)
        self.three.clicked.connect(lambda: self.clicked_btn(3))

        self.prompt = QtWidgets.QLabel(self.centralwidget)
        self.prompt.setObjectName("prompt")
        self.gridLayout.addWidget(self.prompt, 6, 1, 1, 1)
        
        self.percentBox = QtWidgets.QComboBox(self.centralwidget)
        self.percentBox.setMaximumSize(QtCore.QSize(120, 20))
        self.percentBox.setObjectName("percentBox")
        self.percentBox.addItem("")
        self.percentBox.addItem("")
        self.percentBox.addItem("")
        self.percentBox.addItem("")
        self.percentBox.addItem("")
        self.percentBox.addItem("")
        self.percentBox.addItem("")
        self.gridLayout.addWidget(self.percentBox, 4, 3, 1, 1)
        
        self.money = QtWidgets.QTextBrowser(self.centralwidget)
        self.money.setMaximumSize(QtCore.QSize(120, 25))
        self.money.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.money.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.money.setObjectName("money")
        self.gridLayout.addWidget(self.money, 2, 3, 1, 1)
        
        self.Title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(14)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.gridLayout.addWidget(self.Title, 0, 1, 1, 2)
        GuessWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(GuessWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 332, 22))
        self.menubar.setObjectName("menubar")
        GuessWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(GuessWindow)
        self.statusbar.setObjectName("statusbar")
        GuessWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GuessWindow)
        QtCore.QMetaObject.connectSlotsByName(GuessWindow)


    def retranslateUi(self, GuessWindow):
        _translate = QtCore.QCoreApplication.translate
        GuessWindow.setWindowTitle(_translate("GuessWindow", "GuessWindow"))
        self.moneyLabel.setText(_translate("GuessWindow", "Your Money:"))
        self.percentLabel.setText(_translate("GuessWindow", "Choose a percentage"))
        self.two.setText(_translate("GuessWindow", "2"))
        self.one.setText(_translate("GuessWindow", "1"))
        self.three.setText(_translate("GuessWindow", "3"))
        self.prompt.setText(_translate("GuessWindow", "Make a guess..."))
        self.percentBox.setItemText(0, _translate("GuessWindow", "5%"))
        self.percentBox.setItemText(1, _translate("GuessWindow", "15%"))
        self.percentBox.setItemText(2, _translate("GuessWindow", "25%"))
        self.percentBox.setItemText(3, _translate("GuessWindow", "50%"))
        self.percentBox.setItemText(4, _translate("GuessWindow", "75%"))
        self.percentBox.setItemText(5, _translate("GuessWindow", "85%"))
        self.percentBox.setItemText(6, _translate("GuessWindow", "100%"))
        self.money.setText(_translate("GuessWindow", "$200"))
        self.Title.setText(_translate("GuessWindow", "Guessing Game"))

class Ui_LoseForm(object):

    def clicked_yes(self):
        QApplication.closeAllWindows()
        self.GuessWindow = QMainWindow()
        self.ui = Ui_GuessWindow()
        self.ui.setupUi(self.GuessWindow)
        self.GuessWindow.show()

    def clicked_no(self):
        sys.exit()

    def setupUi(self, Form, count):
        Form.setObjectName("Form")
        Form.resize(267, 170)
        Form.setMinimumSize(QtCore.QSize(267, 170))
        Form.setMaximumSize(QtCore.QSize(267, 170))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.Title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(14)
        self.Title.setFont(font)
        self.Title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title.setAutoFillBackground(False)
        self.Title.setTextFormat(QtCore.Qt.AutoText)
        self.Title.setScaledContents(False)
        self.Title.setObjectName("Title")
        self.gridLayout.addWidget(self.Title, 1, 3, 1, 1)

        self.yes = QtWidgets.QPushButton(Form)
        self.yes.setObjectName("yes")
        self.gridLayout.addWidget(self.yes, 14, 3, 1, 1)
        self.yes.clicked.connect(self.clicked_yes)

        self.no = QtWidgets.QPushButton(Form)
        self.no.setObjectName("no")
        self.gridLayout.addWidget(self.no, 15, 3, 1, 1)
        self.no.clicked.connect(self.clicked_no)
        
        self.roundLabel = QtWidgets.QLabel(Form)
        self.roundLabel.setObjectName("roundLabel")
        self.gridLayout.addWidget(self.roundLabel, 3, 3, 1, 1)
        self.rounds = QtWidgets.QTextBrowser(Form)
        self.rounds.setEnabled(True)
        self.rounds.setMaximumSize(QtCore.QSize(50, 25))
        self.rounds.setObjectName("rounds")
        self.rounds.setText(str(count))
        self.gridLayout.addWidget(self.rounds, 4, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Title.setText(_translate("Form", "You Lose! Retry?"))
        self.yes.setText(_translate("Form", "Yes"))
        self.no.setText(_translate("Form", "No"))
        self.roundLabel.setText(_translate("Form", "Rounds:"))   

class Ui_WinForm(object):

    def clicked_yes(self):
        QApplication.closeAllWindows()
        self.GuessWindow = QMainWindow()
        self.ui = Ui_GuessWindow()
        self.ui.setupUi(self.GuessWindow)
        self.GuessWindow.show()

    def clicked_no(self):
        sys.exit()

    def setupUi(self, Form, mon):
        Form.setObjectName("Form")
        Form.resize(267, 170)
        Form.setMinimumSize(QtCore.QSize(267, 170))
        Form.setMaximumSize(QtCore.QSize(267, 170))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.Title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(14)
        self.Title.setFont(font)
        self.Title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title.setAutoFillBackground(False)
        self.Title.setTextFormat(QtCore.Qt.AutoText)
        self.Title.setScaledContents(False)
        self.Title.setObjectName("Title")
        self.gridLayout.addWidget(self.Title, 1, 3, 1, 1)

        self.yes = QtWidgets.QPushButton(Form)
        self.yes.setObjectName("yes")
        self.gridLayout.addWidget(self.yes, 14, 3, 1, 1)
        self.yes.clicked.connect(self.clicked_yes)

        self.no = QtWidgets.QPushButton(Form)
        self.no.setObjectName("no")
        self.gridLayout.addWidget(self.no, 15, 3, 1, 1)
        self.no.clicked.connect(self.clicked_no)
        
        self.roundLabel = QtWidgets.QLabel(Form)
        self.roundLabel.setObjectName("roundLabel")
        self.gridLayout.addWidget(self.roundLabel, 3, 3, 1, 1)
        self.rounds = QtWidgets.QTextBrowser(Form)
        self.rounds.setEnabled(True)
        self.rounds.setMaximumSize(QtCore.QSize(50, 25))
        self.rounds.setObjectName("rounds")
        self.rounds.setText(mon)
        self.gridLayout.addWidget(self.rounds, 4, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Title.setText(_translate("Form", "You Win! Try Again?"))
        self.yes.setText(_translate("Form", "Yes"))
        self.no.setText(_translate("Form", "No"))
        self.roundLabel.setText(_translate("Form", "Money:"))   

if __name__ == "__main__": #### Creates Scene ####
    import sys
    app = QApplication(sys.argv)
    ui = Ui_GuessWindow()
    GuessWindow = QMainWindow()
    LostWindow = QWidget()
    WinWindow = QWidget()
    ui.setupUi(GuessWindow)
    GuessWindow.show()
    sys.exit(app.exec())
