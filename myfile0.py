# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myfile0.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1229, 902)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Gif1 = QtWidgets.QLabel(self.centralwidget)
        self.Gif1.setGeometry(QtCore.QRect(0, -80, 1331, 931))
        self.Gif1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"\n"
"QPushButton{border-radius:25px;}")
        self.Gif1.setText("")
        self.Gif1.setPixmap(QtGui.QPixmap("Black_Template.jpg"))
        self.Gif1.setScaledContents(True)
        self.Gif1.setObjectName("Gif1")
        self.Gif3 = QtWidgets.QLabel(self.centralwidget)
        self.Gif3.setGeometry(QtCore.QRect(0, -10, 1231, 671))
        self.Gif3.setText("")
        self.Gif3.setPixmap(QtGui.QPixmap("Jarvis_Gui (2).gif"))
        self.Gif3.setScaledContents(True)
        self.Gif3.setObjectName("Gif3")
        self.Gif4 = QtWidgets.QLabel(self.centralwidget)
        self.Gif4.setGeometry(QtCore.QRect(0, 690, 311, 131))
        self.Gif4.setText("")
        self.Gif4.setPixmap(QtGui.QPixmap("abstract-hud-ui-gui-future-futuristic-screen-system-virtual-design_115579-713.jpg"))
        self.Gif4.setScaledContents(True)
        self.Gif4.setObjectName("Gif4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(230, 640, 491, 61))
        self.label_9.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 0);\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"")
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(970, 730, 131, 41))
        self.pushButton.setStyleSheet("QPushButton{ \n"
"   border-radius:18px;\n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"   background-color: rgb(255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   \n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1060, 780, 141, 41))
        self.pushButton_2.setStyleSheet("QPushButton{ \n"
"   border-radius:18px;\n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"   \n"
"    background-color: rgb(194, 200, 192);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   \n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 730, 211, 71))
        self.textBrowser.setStyleSheet("background-color: Transparent;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);\n"
"border-radius:none;")
        self.textBrowser.setObjectName("textBrowser")
        self.Gif5 = QtWidgets.QLabel(self.centralwidget)
        self.Gif5.setGeometry(QtCore.QRect(660, 680, 301, 131))
        self.Gif5.setText("")
        self.Gif5.setPixmap(QtGui.QPixmap("abstract-hud-ui-gui-future-futuristic-screen-system-virtual-design_115579-713.jpg"))
        self.Gif5.setScaledContents(True)
        self.Gif5.setObjectName("Gif5")
        self.gif2 = QtWidgets.QLabel(self.centralwidget)
        self.gif2.setGeometry(QtCore.QRect(280, 710, 391, 121))
        self.gif2.setText("")
        self.gif2.setPixmap(QtGui.QPixmap("im (1).gif"))
        self.gif2.setScaledContents(True)
        self.gif2.setObjectName("gif2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(700, 720, 221, 71))
        self.textBrowser_2.setStyleSheet("\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"border-radius:none;\n"
"background-color: Transparent;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", " JARVIS- MY PERSONAL ASSISTANT"))
        self.pushButton.setText(_translate("MainWindow", "RUN"))
        self.pushButton_2.setText(_translate("MainWindow", "TERMINATE"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Shows-current-Date</p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Shows-current-time</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
