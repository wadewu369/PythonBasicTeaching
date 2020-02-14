# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import time
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QListView, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import pyqtSlot

from mark_tool import Ui_MainWindow

class Mark(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        # 繼承Ui_MainWindow 也就是 mark_tool 內的 class
        super(Mark, self).__init__(parent)

        # 建立ui介面
        self.setupUi(self)
        # 這功能主要是點擊了這個按鈕要執行什麼？
        # self.TestButton 這個 function 在 mark_tool.Ui_MainWindow內
        # 因為已經繼承了Ui_MainWindow，因此執行執行 self.TestButton
        # 點擊了時候會套用下方的function test_button_clicked，會將值輸出
        # 如果沒有這行，點擊按鈕不會有任何的東做
        self.TestButton.clicked.connect(self.test_button_clicked)

    def test_button_clicked(self):
        print('test')

if __name__ == "__main__":
    
    # 第一行必備，系統呼叫
    app = QApplication(sys.argv)

    # 指定 Mark Class 會先執行__init__
    window = Mark()

    # 將GUI介面顯示出來
    window.show()

    # 關閉系統
    sys.exit(app.exec_())
