# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1608, 858)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushbutton_fetch_goods_list = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_fetch_goods_list.setGeometry(QtCore.QRect(749, 778, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushbutton_fetch_goods_list.setFont(font)
        self.pushbutton_fetch_goods_list.setObjectName("pushbutton_fetch_goods_list")
        self.tablewidget_goods_list = QtWidgets.QTableWidget(self.centralwidget)
        self.tablewidget_goods_list.setGeometry(QtCore.QRect(0, 60, 1601, 691))
        self.tablewidget_goods_list.setObjectName("tablewidget_goods_list")
        self.tablewidget_goods_list.setColumnCount(0)
        self.tablewidget_goods_list.setRowCount(0)
        self.textedit_keyword = QtWidgets.QTextEdit(self.centralwidget)
        self.textedit_keyword.setGeometry(QtCore.QRect(20, 784, 231, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textedit_keyword.sizePolicy().hasHeightForWidth())
        self.textedit_keyword.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textedit_keyword.setFont(font)
        self.textedit_keyword.setObjectName("textedit_keyword")
        self.pushbutton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_search.setGeometry(QtCore.QRect(260, 780, 113, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushbutton_search.setFont(font)
        self.pushbutton_search.setObjectName("pushbutton_search")
        self.textedit_fetch_page_number = QtWidgets.QTextEdit(self.centralwidget)
        self.textedit_fetch_page_number.setGeometry(QtCore.QRect(440, 784, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textedit_fetch_page_number.setFont(font)
        self.textedit_fetch_page_number.setObjectName("textedit_fetch_page_number")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 790, 60, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 789, 60, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lcdnumber_pages = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdnumber_pages.setGeometry(QtCore.QRect(40, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lcdnumber_pages.setFont(font)
        self.lcdnumber_pages.setProperty("value", 0.0)
        self.lcdnumber_pages.setObjectName("lcdnumber_pages")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.spinbox_thread_number = QtWidgets.QSpinBox(self.centralwidget)
        self.spinbox_thread_number.setGeometry(QtCore.QRect(670, 782, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.spinbox_thread_number.setFont(font)
        self.spinbox_thread_number.setProperty("value", 1)
        self.spinbox_thread_number.setObjectName("spinbox_thread_number")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(610, 789, 60, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(790, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lcdnumber_time = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdnumber_time.setGeometry(QtCore.QRect(830, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lcdnumber_time.setFont(font)
        self.lcdnumber_time.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdnumber_time.setSmallDecimalPoint(False)
        self.lcdnumber_time.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdnumber_time.setProperty("value", 0.0)
        self.lcdnumber_time.setObjectName("lcdnumber_time")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(920, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lcdnumber_every_page_goods_number = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdnumber_every_page_goods_number.setGeometry(QtCore.QRect(240, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lcdnumber_every_page_goods_number.setFont(font)
        self.lcdnumber_every_page_goods_number.setProperty("value", 0.0)
        self.lcdnumber_every_page_goods_number.setObjectName("lcdnumber_every_page_goods_number")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(190, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(330, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.pushbutton_load_goods_list = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_load_goods_list.setGeometry(QtCore.QRect(910, 778, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushbutton_load_goods_list.setFont(font)
        self.pushbutton_load_goods_list.setObjectName("pushbutton_load_goods_list")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "可视化爬虫"))
        self.pushbutton_fetch_goods_list.setText(_translate("MainWindow", "抓取商品列表"))
        self.pushbutton_search.setText(_translate("MainWindow", "搜索"))
        self.textedit_fetch_page_number.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">1</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "抓取前"))
        self.label_2.setText(_translate("MainWindow", "页"))
        self.label_5.setText(_translate("MainWindow", "共"))
        self.label_6.setText(_translate("MainWindow", "页"))
        self.label_7.setText(_translate("MainWindow", "线程"))
        self.label_8.setText(_translate("MainWindow", "耗时"))
        self.label_9.setText(_translate("MainWindow", "秒"))
        self.label_10.setText(_translate("MainWindow", "每页"))
        self.label_11.setText(_translate("MainWindow", "件商品"))
        self.pushbutton_load_goods_list.setText(_translate("MainWindow", "装载商品列表"))

