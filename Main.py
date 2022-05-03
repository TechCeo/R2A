# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tobiproject.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWinExtras import QtWin
import sys



QtWin.setCurrentProcessExplicitAppUserModelID("main")



class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(510, 610)
        MainWindow.setAnimated(True)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ResultBox = QtWidgets.QLabel(self.centralwidget)
        self.ResultBox.setGeometry(QtCore.QRect(90, 320, 341, 51))
        self.ResultBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ResultBox.setAutoFillBackground(False)
        self.ResultBox.setStyleSheet("background-color: rgb(35, 196, 244);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(13, 200, 241, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 14pt \"Trebuchet MS\";")
        self.ResultBox.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.ResultBox.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ResultBox.setLineWidth(0)
        self.ResultBox.setTextFormat(QtCore.Qt.RichText)
        self.ResultBox.setScaledContents(False)
        self.ResultBox.setIndent(-1)
        self.ResultBox.setObjectName("ResultBox")
        

        self.TranslateButton = QtWidgets.QPushButton(self.centralwidget)
        self.TranslateButton.setGeometry(QtCore.QRect(90, 430, 151, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.TranslateButton.setFont(font)
        self.TranslateButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.TranslateButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.TranslateButton.setAcceptDrops(False)
        self.TranslateButton.setAutoFillBackground(False)
        self.TranslateButton.setStyleSheet("background-color: rgb(60, 145, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(94, 94, 94);")
        self.TranslateButton.setAutoDefault(False)
        self.TranslateButton.setDefault(True)
        self.TranslateButton.setFlat(False)
        self.TranslateButton.setObjectName("TranslateButton")
        


        self.ClearButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearButton.setGeometry(QtCore.QRect(280, 430, 151, 51))
        self.ClearButton.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 88, 32);\n"
"background-color: rgb(240, 58, 13);\n"
"")
        self.ClearButton.setObjectName("ClearButton")
        
        self.Label1 = QtWidgets.QLabel(self.centralwidget)
        self.Label1.setGeometry(QtCore.QRect(100, 150, 131, 21))
        self.Label1.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.Label1.setObjectName("Label1")
        
        self.Label1_2 = QtWidgets.QLabel(self.centralwidget)
        self.Label1_2.setGeometry(QtCore.QRect(90, 280, 201, 41))
        self.Label1_2.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.Label1_2.setObjectName("Label1_2")


        self.Label1_3 = QtWidgets.QLabel(self.centralwidget)
        self.Label1_3.setGeometry(QtCore.QRect(190, 550, 201, 41))
        self.Label1_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.Label1_3.setObjectName("Label1_2")
        

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(90, 130, 341, 131))
        self.groupBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        

        self.InputBox = QtWidgets.QLineEdit(self.groupBox)
        self.InputBox.setGeometry(QtCore.QRect(10, 50, 321, 51))
        self.InputBox.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(10, 230, 250);\n"
"")
        self.InputBox.setDragEnabled(False)
        self.InputBox.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.InputBox.setClearButtonEnabled(False)
        self.InputBox.setObjectName("InputBox")
        

        self.Headinglabel = QtWidgets.QLabel(self.centralwidget)
        self.Headinglabel.setGeometry(QtCore.QRect(60, 50, 401, 51))
        self.Headinglabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.Headinglabel.setObjectName("Headinglabel")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #####

        self.TranslateButton.clicked.connect(self.decode_roman_numeral)
        self.ClearButton.clicked.connect(self.Clearform)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Roman to Arabic Num Translator"))
        self.ResultBox.setText(_translate("MainWindow", " Answer"))
        self.TranslateButton.setText(_translate("MainWindow", "Translate"))
        self.ClearButton.setText(_translate("MainWindow", "Clear"))
        self.Label1.setText(_translate("MainWindow", "Roman Numeral"))
        self.Label1_2.setText(_translate("MainWindow", "Arabic Numeral Representation"))
        self.Label1_3.setText(_translate("MainWindow", "_TechCeo2020_"))
        self.InputBox.setPlaceholderText(_translate("MainWindow", "Enter Roman Numerals Here"))
        self.Headinglabel.setText(_translate("MainWindow", "ROMAN 2 ARABIC NUMERAL TRANSLATOR"))




    def decode_roman_numeral(self):
        roman = self.InputBox.text().upper()
        """Calculate the numeric value of a Roman numeral (in capital letters)"""
        trans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        try:
            for i in roman:
                if i in trans:

                    values = [trans[r] for r in roman]
                    x = str(sum(
                    val if val >= next_val else -val
                    for val, next_val in zip(values[:-1], values[1:])
                    ) + values[-1])
                    self.ResultBox.setText(x)

                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("ERROR: Invalid input")
                    msg.setText("Enter a valid Roman Numeral")
                    msg.setIcon(QMessageBox.Critical)
                    y = msg.exec_()
                    break

            
        except:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR: Invalid input")
            msg.setText("Enter a valid Roman Numeral")
            msg.setIcon(QMessageBox.Critical)
            y = msg.exec_()
        



    def Clearform(self):
        self.ResultBox.setText(" ")
        self.InputBox.clear()
    	


        
   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('appicon.ico'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
