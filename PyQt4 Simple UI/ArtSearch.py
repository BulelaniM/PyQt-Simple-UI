# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ArtSearch.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def closeCheck(self):
        sys.exit(app.exec_())
        print("Program closed")
     

        
    def setupUi(self, MainWindow):
    
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(625, 573)
        MainWindow.setStyleSheet(_fromUtf8("QWidget{\n"
"    background-color: qlineargradient(spread:pad, x1:0.391773, y1:0.665, x2:1, y2:0, stop:0.403409 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"QLineEdit{background-color:none\n"
"}\n"
"QPushButton{background-color:none}\n"
"QTextEdit{background-color:none\n"
"}\n"
"QTextBrowserl{background-color:none\n"
"}\n"
"QMenuBar{\n"
"    background-color: qlineargradient(spread:pad, x1:0.391773, y1:0.665, x2:1, y2:0, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.art_name = QtGui.QLabel(self.centralwidget)
        self.art_name.setGeometry(QtCore.QRect(70, 80, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.art_name.setFont(font)
        self.art_name.setObjectName(_fromUtf8("art_name"))
        self.buy_link = QtGui.QLabel(self.centralwidget)
        self.buy_link.setGeometry(QtCore.QRect(70, 130, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.buy_link.setFont(font)
        self.buy_link.setObjectName(_fromUtf8("buy_link"))
        self.soc_med_det = QtGui.QLabel(self.centralwidget)
        self.soc_med_det.setGeometry(QtCore.QRect(70, 180, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.soc_med_det.setFont(font)
        self.soc_med_det.setObjectName(_fromUtf8("soc_med_det"))
        self.submit_btn = QtGui.QPushButton(self.centralwidget)
        self.submit_btn.setGeometry(QtCore.QRect(420, 230, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.submit_btn.setFont(font)
        self.submit_btn.setObjectName(_fromUtf8("submit_btn"))
        self.lineEdit_artname = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_artname.setGeometry(QtCore.QRect(200, 80, 171, 20))
        self.lineEdit_artname.setObjectName(_fromUtf8("lineEdit_artname"))
        self.lineEdit_purchaselink = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_purchaselink.setGeometry(QtCore.QRect(200, 130, 171, 20))
        self.lineEdit_purchaselink.setObjectName(_fromUtf8("lineEdit_purchaselink"))
        self.textEdit_addart_det = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_addart_det.setGeometry(QtCore.QRect(200, 180, 171, 71))
        self.textEdit_addart_det.setObjectName(_fromUtf8("textEdit_addart_det"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 280, 531, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.headlabel = QtGui.QLabel(self.centralwidget)
        self.headlabel.setGeometry(QtCore.QRect(140, 10, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.headlabel.setFont(font)
        self.headlabel.setObjectName(_fromUtf8("headlabel"))
        self.art_search = QtGui.QLabel(self.centralwidget)
        self.art_search.setGeometry(QtCore.QRect(70, 320, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.art_search.setFont(font)
        self.art_search.setObjectName(_fromUtf8("art_search"))
        self.art_det = QtGui.QLabel(self.centralwidget)
        self.art_det.setGeometry(QtCore.QRect(70, 380, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.art_det.setFont(font)
        self.art_det.setObjectName(_fromUtf8("art_det"))
        self.lineEdit_searchart = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_searchart.setGeometry(QtCore.QRect(200, 320, 181, 20))
        self.lineEdit_searchart.setObjectName(_fromUtf8("lineEdit_searchart"))
        self.search_btn = QtGui.QPushButton(self.centralwidget)
        self.search_btn.setGeometry(QtCore.QRect(420, 320, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.search_btn.setFont(font)
        self.search_btn.setObjectName(_fromUtf8("search_btn"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(200, 380, 181, 101))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.saveButton = QtGui.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(430, 480, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.closeButton = QtGui.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(510, 480, 75, 23))
######################################close button event#################
        self.closeButton.clicked.connect(self.closeCheck)
######################################close button event ###############
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.closeButton.setFont(font)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
##################Exit file drop down######################
        self.actionExit.triggered.connect(self.closeCheck)
########################Exit file drop down###############
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ArtSearch", None))
        self.art_name.setText(_translate("MainWindow", "Artist Name", None))
        self.buy_link.setText(_translate("MainWindow", "Purchase Link", None))
        self.soc_med_det.setText(_translate("MainWindow", "Social Media", None))
        self.submit_btn.setText(_translate("MainWindow", "Submit", None))
        self.headlabel.setText(_translate("MainWindow", "ARTIST INFORMATION", None))
        self.art_search.setText(_translate("MainWindow", "Search Artist", None))
        self.art_det.setText(_translate("MainWindow", "Artist Details", None))
        self.search_btn.setText(_translate("MainWindow", "Search", None))
        self.saveButton.setText(_translate("MainWindow", "Save", None))
        self.closeButton.setText(_translate("MainWindow", "Close", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save As", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

