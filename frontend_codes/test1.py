# # -*- coding: utf-8 -*-


# # Form implementation generated from reading ui file 'test1.ui'
# #
# # Created by: PyQt5 UI code generator 5.15.9
# #
# # WARNING: Any manual changes made to this file will be lost when pyuic5 is
# # run again.  Do not edit this file unless you know what you are doing.


# from PyQt5 import QtCore, QtGui, QtWidgets
# # from PySide6.QtWidgets import QLabel,QApplication,QWidget
# # from PySide6.QtGui import QIcon,QMovie
# from PyQt5.QtGui import QMovie 
# from PyQt5.QtCore import Qt
# import sys

# class Ui_Dialog(object):
#     def setupUi(self, Dialog):
#         Dialog.setObjectName("Dialog")
#         Dialog.resize(1129, 834)
        
#         # # self.centralwidget = QtWidgets.QWidget(Ui_Dialog)
#         # # self.centralwidget.setObjectName("centralwidget")

#         # self.label = QtWidgets.QLabel(self.centralwidget)
#         # self.label.setGeometry(QtCore.QRect(25, 25, 200, 200))
#         # self.label.setMinimumSize(QtCore.QSize(200, 200))
#         # self.label.setMaximumSize(QtCore.QSize(200, 200))
#         # self.label.setObjectName("label")

#         # # Ui_Dialog.setCentralWidget(self.centralwidget)

#         Dialog.setAutoFillBackground(False)
#         Dialog.setStyleSheet("")
#         Dialog.setSizeGripEnabled(False)
#         self.BG_1 = QtWidgets.QLabel(Dialog)
#         self.BG_1.setGeometry(QtCore.QRect(-140, -130, 1311, 1071))
#         self.BG_1.setText("")
#         self.BG_1.setPixmap(QtGui.QPixmap("E:\jarvis\B.G\Black_Template.jpg"))
#         self.BG_1.setScaledContents(True)
#         self.BG_1.setObjectName("BG_1")
#         self.Bg_2 = QtWidgets.QLabel(Dialog)
#         self.Bg_2.setGeometry(QtCore.QRect(30, 20, 381, 281))
#         self.Bg_2.setStyleSheet("background-color: rgb(85, 170, 255);")
#         self.Bg_2.setText("")
#         self.Bg_2.setObjectName("Bg_2")
#         self.Bg_3 = QtWidgets.QLabel(Dialog)
#         self.Bg_3.setGeometry(QtCore.QRect(440, 20, 421, 281))
#         self.Bg_3.setStyleSheet("background-color: rgb(85, 170, 255);")
#         self.Bg_3.setText("")
#         self.Bg_3.setObjectName("Bg_3")
#         self.gif_1 = QtWidgets.QLabel(Dialog)
#         self.gif_1.setGeometry(QtCore.QRect(50, 40, 341, 241))
#         self.gif_1.setText("")
#         self.gif_1.setPixmap(QtGui.QPixmap("E:\jarvis\B.G\Iron_Template_1.gif"))
#         self.gif_1.setScaledContents(True)
#         self.gif_1.setObjectName("gif_1")
#         self.gif_2 = QtWidgets.QLabel(Dialog)
#         self.gif_2.setGeometry(QtCore.QRect(460, 40, 381, 251))
#         self.gif_2.setText("")
#         self.gif_2.setPixmap(QtGui.QPixmap("E:\jarvis\ExtraGui\live.gif"))
#         self.gif_2.setScaledContents(True)
#         self.gif_2.setObjectName("gif_2")
#         self.gif_3 = QtWidgets.QLabel(Dialog)
#         self.gif_3.setGeometry(QtCore.QRect(20, 360, 511, 341))
#         self.gif_3.setText("")
#         self.gif_3.setPixmap(QtGui.QPixmap("E:\jarvis\VoiceReg\Qualt.gif"))
#         self.gif_3.setScaledContents(True)
#         self.gif_3.setObjectName("gif_3")
#         self.gif_4 = QtWidgets.QLabel(Dialog)
#         self.gif_4.setGeometry(QtCore.QRect(920, 40, 161, 241))
#         self.gif_4.setText("")
#         self.gif_4.setPixmap(QtGui.QPixmap("E:\jarvis\ExtraGui\Earth.gif"))
       
#         self.gif_4 = QMovie("E:\jarvis\ExtraGui\Earth.gif")
#         self.label.setMovie(self.gif_4)
#         self.gif_4.start()

#         self.gif_4.setScaledContents(True)
#         self.gif_4.setObjectName("gif_4")
#         self.Bg_4 = QtWidgets.QLabel(Dialog)
#         self.Bg_4.setGeometry(QtCore.QRect(900, 20, 201, 281))
#         self.Bg_4.setStyleSheet("background-color: rgb(85, 170, 255);")
#         self.Bg_4.setText("")
#         self.Bg_4.setObjectName("Bg_4")
#         self.BG_1.raise_()
#         self.Bg_2.raise_()
#         self.Bg_3.raise_()
#         self.gif_1.raise_()
#         self.gif_2.raise_()
#         self.gif_3.raise_()
#         self.Bg_4.raise_()
#         self.gif_4.raise_()

#         self.retranslateUi(Dialog)
#         QtCore.QMetaObject.connectSlotsByName(Dialog)

#     def retranslateUi(self, Dialog):
#         _translate = QtCore.QCoreApplication.translate
#         Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

# # class Window (QWidget):
# #     def __int__(self):
# #         label=QLabel(self)
# #         movie=QMovie("E:\jarvis\ExtraGui\Earth.gif")
# #         label.setMovie(movie)
# #         movie.start()


# def startAnimation(self):
#         self.movie.start()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     window=QtWidgets.QMainWindow()
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     # app=QApplication([])
#     # window=Window()
#     # window.show()
#     sys.exit(app.exec_())


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # create label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 25, 200, 200))
        self.label.setMinimumSize(QtCore.QSize(200, 200))
        self.label.setMaximumSize(QtCore.QSize(200, 200))
        self.label.setObjectName("label")

        # add label to main window
        MainWindow.setCentralWidget(self.centralwidget)

        # set qmovie as label
        self.movie = QMovie("F:\\jarvis_code_files\\prayukti_2023_proj\\frontend_codes\\ExtraGui\\Earth.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
    
