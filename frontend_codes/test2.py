from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(893, 496)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 891, 501))
        self.label.setAutoFillBackground(True)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(r"D:\\prayukti\\prayukti_2023_proj\\frontend_codes\\B.G\\Black_Template.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1, 1, 891, 501))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.movie = QMovie(r"D:\\prayukti\\prayukti_2023_proj\\frontend_codes\\ExtraGui\\WELCOME_PAGE.gif")
        self.label_2.setMovie(self.movie)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
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
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    QtCore.QTimer.singleShot(5100,MainWindow.close)
    sys.exit(app.exec_())

