from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fill_textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.fill_textEdit.setGeometry(QtCore.QRect(30, 20, 741, 161))
        self.fill_textEdit.setObjectName("fill_textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_it())
        self.pushButton.setGeometry(QtCore.QRect(360, 200, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.read_textEdit = QtWidgets.QListWidget(self.centralwidget)
        self.read_textEdit.setGeometry(QtCore.QRect(30, 250, 741, 161))
        self.read_textEdit.setObjectName("read_textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #Add into Check Box
    def add_it(self):
        #Grab item
        item = self.fill_textEdit.text()
        #add to Check Box
        self.read_textEdit.addItem(item)
        #clear input
        self.fill_textEdit.setText("")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys. exit(app.exec_())