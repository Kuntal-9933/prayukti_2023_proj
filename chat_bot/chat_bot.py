from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 408)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-16, -155, 1421, 881))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.user_pic = QtWidgets.QLabel(self.centralwidget)
        self.user_pic.setGeometry(QtCore.QRect(60, 40, 71, 71))
        self.user_pic.setText("")
        self.user_pic.setPixmap(QtGui.QPixmap("F:\\jarvis_code_files\\prayukti_2023_proj\\chat_bot\\user_pic.png"))
        self.user_pic.setScaledContents(True)
        self.user_pic.setObjectName("user_pic")
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(150, 40, 681, 71))
        self.text_1.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"background-color: rgb(209, 209, 209);\n"
"")
        self.text_1.setText("")
        self.text_1.setObjectName("text_1")
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(150, 180, 681, 161))
        self.text_2.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"background-color: rgb(209, 209, 209);\n"
"")
        self.text_2.setText("")
        self.text_2.setObjectName("text_2")
        self.bot_pic = QtWidgets.QLabel(self.centralwidget)
        self.bot_pic.setGeometry(QtCore.QRect(50, 220, 81, 81))
        self.bot_pic.setText("")
        self.movie=QMovie("F:\\jarvis_code_files\\prayukti_2023_proj\\chat_bot\\bot_pic.gif")
        self.bot_pic.setMovie(self.movie)
        self.bot_pic.setScaledContents(True)
        self.bot_pic.setObjectName("bot_pic")
        self.movie.start()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
# import chat_bot_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
