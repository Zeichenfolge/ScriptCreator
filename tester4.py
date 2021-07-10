from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
#Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
#Buttons
        self.final_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.final_pushButton.setGeometry(QtCore.QRect(430, 400, 31, 91))
        self.final_pushButton.setObjectName("final_pushButton")
    #
        self.check_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_it())
        self.check_pushButton.setGeometry(QtCore.QRect(180, 300, 93, 28))
        self.check_pushButton.setObjectName("check_pushButton")
#list
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(470, 20, 301, 481))
        self.listWidget.setObjectName("listWidget")
#ComboBox
        self.variable_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.variable_comboBox.setGeometry(QtCore.QRect(110, 70, 301, 41))
        self.variable_comboBox.setObjectName("variable_comboBox")
#Line (description)
        self.descr_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.descr_lineEdit.setGeometry(QtCore.QRect(87, 264, 331, 31))
        self.descr_lineEdit.setObjectName("descr_lineEdit")
#Label
        self.descr_label = QtWidgets.QLabel(self.centralwidget)
        self.descr_label.setGeometry(QtCore.QRect(13, 270, 70, 16))
        self.variable_comboBox.setEditable(True)
        self.descr_label.setObjectName("descr_label")
###Variables of Combo Box
        self.variable_comboBox.addItem("H1_PGM_PrgStatus")
        self.variable_comboBox.addItem("H2_PGM_PrgStatus")
        self.variable_comboBox.addItem("M1_HYGSUP_Control")
        self.variable_comboBox.addItem("M2_Onlineplus")
#Textbox (check)
        self.check_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.check_textEdit.setGeometry(QtCore.QRect(10, 340, 411, 161))
        self.check_textEdit.setObjectName("check_textEdit")
#Radio_Button
        self.checkRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.checkRadioButton.setGeometry(QtCore.QRect(10, 30, 61, 20))
        self.checkRadioButton.setObjectName("checkRadioButton")
    #
        self.waitRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.waitRadioButton.setGeometry(QtCore.QRect(10, 60, 61, 20))
        self.waitRadioButton.setObjectName("waitRadioButton")
###?
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

# Add into Check Box
    def add_it(self):
        if  self.checkRadioButton.isChecked():
            self.checkRadioButton.setText("Check ")
            action = self.checkRadioButton.text()
        elif self.waitRadioButton.isChecked():
            self.waitRadioButton.setText("Wait ")
            action = self.waitRadioButton.text()
        else:
            action = 1

        # Grab item
        item = self.variable_comboBox.currentText()
        # Grab description
        item_descr = self.descr_lineEdit.text()
        # add to Check Box

        if action == 1:
            self.check_textEdit.setPlainText("No Button pressed")
        else:
            self.check_textEdit.setPlainText(
                action + "testresult.append(\n     basic_tests.checkStatus(\n          current_status = bus." + item + ",\n          nominal_status = c.PGM_SYNC,\n          descr = " + item_descr + "\n     )\n)")



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.final_pushButton.setText(_translate("MainWindow", "->"))
        self.check_pushButton.setText(_translate("MainWindow", "PushButton"))
        self.descr_label.setText(_translate("MainWindow", "Description:"))
        self.checkRadioButton.setText(_translate("MainWindow", "Check"))
        self.waitRadioButton.setText(_translate("MainWindow", "Wait"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
