# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DS.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import Series as DS
import string



import os
from PyQt5 import QtCore, QtGui, QtWidgets
root = Tk()

root.withdraw()
class text_box(object):
    def __init__(self, title, text=None):
        if text == None:
            self.Text = list()
        else:
            self.Text = list(text)
        self.Title=str(title)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 100, 600, 500))
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.print()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def print(self):
        for i in range(len(self.Text)):
           self.textEdit.insertPlainText (self.Text[i])
           self.textEdit.insertPlainText("\n")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", self.Title))




class Ui_MainWindow(object):
    def __init__(self):
        self.paths = list()
        self.files=list()
        self.window=list()
        self.library=DS.Series()
        self.count=0
        self.index=0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(845, 505)
        MainWindow.setFixedSize(845, 505)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(30, 160, 341, 61))
        self.textEdit_7.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"border: 1px solid; border-radius:10px; background-color: palette(base);\n"
"")
        self.textEdit_7.setObjectName("textEdit_7")
        ##
        self.textEdit_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(440, 150, 341, 200))
        self.textEdit_8.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"border: 1px solid; border-radius:10px; background-color: palette(base);\n"
"")
        self.textEdit_8.setObjectName("textEdit_8")
        ##
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 80, 350, 61))
        self.label_6.setStyleSheet("font: 20pt \"MV Boli\";\n"
"background:#bebede;\n"
"color:blue;\n"
"border-radius:12px;")
        self.label_6.setObjectName("label_6")


        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 346, 130, 61))
        self.label_7.setStyleSheet("font: 20pt \"MV Boli\";\n"
                                   "color:blue;\n"
                                   "border-radius:12px;")
        self.label_7.setObjectName("label_7")


        ##
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 410, 150, 61))
        self.label_8.setStyleSheet("font: 20pt \"MV Boli\";\n"
                                   "color:blue;\n"
                                   "border-radius:12px;")
        self.label_8.setObjectName("label_8")
        #self.label_8.hide()
        ##

        ##
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(430, 80, 410, 61))
        self.label_9.setStyleSheet("font: 20pt \"MV Boli\";\n"
"background:#bebede;\n"
"color:blue;\n"
"border-radius:12px;")
        self.label_9.setObjectName("label_9")
        ##

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 250, 191, 61))
        self.pushButton_2.setStyleSheet("font: 20pt \"MV Boli\";\n"
"background:#bebede;\n"
"color:blue;\n"
"\n"
"border-radius:12px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 420, 301, 61))
        self.pushButton_3.setStyleSheet("font: 20pt \"MV Boli\";\n"
"background:#bebede;\n"
"color:blue;\n"
"\n"
"border-radius:12px;")
        self.pushButton_3.setObjectName("pushButton_3")

        ##
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(515, 360, 200, 45))
        self.pushButton_4.setStyleSheet("font: 20pt \"MV Boli\";\n"
                                        "background:#bebede;\n"
                                        "color:blue;\n"
                                        "\n"
                                        "border-radius:12px;")
        self.pushButton_4.setObjectName("pushButton_4")
        #self.pushButton_4.setEnabled(False)
        ##



        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_3.clicked.connect(self.select)
        self.pushButton_2.clicked.connect(self.search)
        self.pushButton_4.clicked.connect(self.show_more)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        self.progress = QtWidgets.QProgressBar(self.centralwidget)
        self.progress.setGeometry(30, 400, 300, 25)
        self.progress.setMaximum(1000)
        self.progress.setValue(0)

    def print_text_box_value(self,x):
        f = open(self.paths[x], "r",encoding="utf8")
        m = f.readlines()
        f.close()

        path=self.paths[x]
        ind=path.rfind('/')
        title=path[ind+1:]

        self.window.append(QtWidgets.QMainWindow())
        self.ui = text_box(title,m)
        self.ui.setupUi(self.window[len(self.window)-1])
        self.window[len(self.window)-1].show()


    def sent_tokenize(self):
        for file in self.paths:
            print(file)
            f = open(file, 'r',encoding="utf8")
            text = f.read()
            t = text.split('\n')
            self.files.append(t)


    def build_series(self):
        for x in range(len(self.paths)):
            self.count+=1
            self.progress.setValue(self.count)
            #print(self.paths[x])
            f = open(self.paths[x], "r", encoding="utf8")
            file= f.readlines()
            for y in file:
                temp = y.split()
                for z in temp:
                    after_edit = z.translate(str.maketrans('', '', string.punctuation))
                    if not after_edit == '':
                        after_edit=after_edit.lower()
                        self.library.insert_set(after_edit, x)
            f.close()


    def select(self):
        try:

            self.paths=list()
            self.library=DS.Series()
            self.count=0
            self.progress.setValue(0)
            file_path = filedialog.askdirectory()
            entries = os.listdir(file_path)
            self.label_8.setText("Processing")
            for entry in entries:
                i=entry.rfind('.')
                t=entry[i+1:]
                if(t != 'txt'):
                    raise TypeError

            for file in entries:
                self.paths.append(file_path + '/' + file)

            self.progress.setMaximum(len(self.paths))
            self.build_series()
            self.label_8.setText("Done")
            #print(self.library.items())



        except TypeError:
            messagebox.showerror('Error', "Please make sure that the folder has txt files only")
        except:
            messagebox.showerror('Error',"Please select a folder")

    def show_more(self):
        try:
            c=0
            l = len(self.mySet)
            s=list(self.mySet)
            while(1):

                if(self.index == l):
                    messagebox.showinfo("Info","No more files")
                    break
                if (c==5):
                    break
                self.print_text_box_value(s[self.index])
                self.index+=1
                if(self.index ==l ):
                    break
                c+=1
        except:
            messagebox.showerror('Error',"Please select a folder")   


    def search(self):
        """search for word in self.library using binary search
        if exit itterate throw the given value which is a set and for each index print the file using
        self.print_text_box_value function
        if doesn't exit show a message box with (doesn't exit) message"""
        self.index=0
        word=self.textEdit_7.toPlainText()
        word=word.lower()
        self.textEdit_8.clear()
        ##
        self.mySet=set()
        self.mySet=self.library.binary_search(word)
        if self.mySet == None:
            messagebox.showinfo("Error", "doesn't exit")
        else:
            c=0
            for x in self.mySet:
                if c<5:
                    self.print_text_box_value(x)
                    c+=1
                    self.index+=1

                path=self.paths[x]
                t=path.rfind('/')
                self.textEdit_8.insertPlainText(path[t+1:])
                self.textEdit_8.insertPlainText("\n")


        ##

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text Search Tool"))
        self.label_6.setText(_translate("MainWindow", "  Enter the word here"))
        self.label_7.setText(_translate("MainWindow", "Status"))
        self.label_8.setText(_translate("MainWindow", "Not Active"))
        self.label_9.setText(_translate("MainWindow", " Files contain the Query word"))
        self.pushButton_2.setText(_translate("MainWindow", "Search"))
        self.pushButton_3.setText(_translate("MainWindow", "Select Folder"))
        self.pushButton_4.setText(_translate("MainWindow", "Show More"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    mainloop()
    sys.exit(app.exec_())
