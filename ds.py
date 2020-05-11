# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DS.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import os
from PyQt5 import QtCore, QtGui, QtWidgets
root = tk.Tk()
root.withdraw()


class Ui_MainWindow(object):
    def __init__(self):
        self.paths = list()
        self.files=list()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(845, 505)
        MainWindow.setFixedSize(845, 505)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(30, 160, 341, 61))
        self.textEdit_7.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.textEdit_7.setObjectName("textEdit_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 80, 461, 61))
        self.label_6.setStyleSheet("font: 20pt \"MV Boli\";\n"
"background:#bebede;\n"
"color:blue;\n"
"border-radius:12px;")
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 250, 191, 61))
        self.pushButton_2.setStyleSheet("font: 20pt \"MV Boli\";\n"
"background:#bebede;\n"
"color:blue;\n"
"\n"
"border-radius:12px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 370, 301, 61))
        self.pushButton_3.setStyleSheet("font: 20pt \"MV Boli\";\n"
"background:#bebede;\n"
"color:blue;\n"
"\n"
"border-radius:12px;")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_3.clicked.connect(self.select)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def sent_tokenize(self):
        for file in self.paths:
            f = open(file, 'r')
            text = f.read()
            t = text.split('\n')
            self.files.append(t)

    def select(self):
        try:

            file_path = filedialog.askdirectory()
            entries = os.listdir(file_path)
            for entry in entries:
                i=entry.rfind('.')
                t=entry[i+1:]
                if(t != 'txt'):
                    raise TypeError

            for file in entries:
                self.paths.append(file_path + '/' + file)

        except TypeError:
            messagebox.showerror('Error', "Please make sure that the folder has txt files only")
        except:
            messagebox.showerror('Error',"Please select a folder")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text Search Tool"))
        self.label_6.setText(_translate("MainWindow", "  Enter the word here"))
        self.pushButton_2.setText(_translate("MainWindow", "Search"))
        self.pushButton_3.setText(_translate("MainWindow", "Select Folder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
