from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import xml.etree.ElementTree as ET
import os
import requests
from bs4 import BeautifulSoup


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        app.setStyle('windowsvista')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.channel_dropdown = QtWidgets.QComboBox(self.centralwidget)
        self.channel_dropdown.setGeometry(QtCore.QRect(320, 40, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.channel_dropdown.setFont(font)
        self.channel_dropdown.setAccessibleDescription("")
        self.channel_dropdown.setStyleSheet("background-color: rgb(227, 227, 227);\n"
                                            "alternate-background-color: rgb(227, 227, 227);")
        self.channel_dropdown.setObjectName("channel_dropdown")
        self.channel_dropdown.addItem("")
        self.channel_dropdown.addItem("")
        self.channel_dropdown.addItem("")
        self.channel_dropdown.addItem("")
        self.channel_dropdown.addItem("")
        self.channel_dropdown.addItem("")
        self.office_channel_label = QtWidgets.QLabel(self.centralwidget)
        self.office_channel_label.setGeometry(QtCore.QRect(120, 40, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.office_channel_label.setFont(font)
        self.office_channel_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.office_channel_label.setObjectName("office_channel_label")
        self.enable_updates_label = QtWidgets.QLabel(self.centralwidget)
        self.enable_updates_label.setGeometry(QtCore.QRect(110, 220, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.enable_updates_label.setFont(font)
        self.enable_updates_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.enable_updates_label.setObjectName("enable_updates_label")
        self.enable_updates_dropdown = QtWidgets.QComboBox(self.centralwidget)
        self.enable_updates_dropdown.setGeometry(QtCore.QRect(320, 220, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.enable_updates_dropdown.setFont(font)
        self.enable_updates_dropdown.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.enable_updates_dropdown.setObjectName("enable_updates_dropdown")
        self.enable_updates_dropdown.addItem("")
        self.enable_updates_dropdown.addItem("")
        self.office_build_label = QtWidgets.QLabel(self.centralwidget)
        self.office_build_label.setGeometry(QtCore.QRect(150, 100, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.office_build_label.setFont(font)
        self.office_build_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.office_build_label.setObjectName("office_build_label")
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(280, 290, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.submit_button.setFont(font)
        self.submit_button.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.submit_button.setObjectName("submit_button")
        self.bit_label = QtWidgets.QLabel(self.centralwidget)
        self.bit_label.setGeometry(QtCore.QRect(60, 160, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.bit_label.setFont(font)
        self.bit_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_label.setObjectName("bit_label")
        self.bit_dropdown = QtWidgets.QComboBox(self.centralwidget)
        self.bit_dropdown.setGeometry(QtCore.QRect(320, 160, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.bit_dropdown.setFont(font)
        self.bit_dropdown.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.bit_dropdown.setObjectName("bit_dropdown")
        self.bit_dropdown.addItem("")
        self.bit_dropdown.addItem("")
        self.office_build_dropdown = QtWidgets.QComboBox(self.centralwidget)
        self.office_build_dropdown.setGeometry(QtCore.QRect(320, 100, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.office_build_dropdown.setFont(font)
        self.office_build_dropdown.setAccessibleDescription("")
        self.office_build_dropdown.setStyleSheet("background-color: rgb(227, 227, 227);\n"
                                                    "alternate-background-color: rgb(227, 227, 227);")
        self.office_build_dropdown.setEditable(False)
        self.office_build_dropdown.setObjectName("office_build_dropdown")
        self.office_channel_label.raise_()
        self.enable_updates_label.raise_()
        self.enable_updates_dropdown.raise_()
        self.office_build_label.raise_()
        self.submit_button.raise_()
        self.bit_label.raise_()
        self.bit_dropdown.raise_()
        self.channel_dropdown.raise_()
        self.office_build_dropdown.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.office_versions()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.channel_dropdown, self.office_build_dropdown)
        MainWindow.setTabOrder(self.office_build_dropdown, self.bit_dropdown)
        MainWindow.setTabOrder(self.bit_dropdown, self.enable_updates_dropdown)
        MainWindow.setTabOrder(self.enable_updates_dropdown, self.submit_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.channel_dropdown.setAccessibleName(_translate("MainWindow", "Current Channel Dropdown"))
        self.channel_dropdown.setItemText(0, _translate("MainWindow", "Current"))
        self.channel_dropdown.setItemText(1, _translate("MainWindow", "CurrentPreview"))
        self.channel_dropdown.setItemText(2, _translate("MainWindow", "SemiAnnual"))
        self.channel_dropdown.setItemText(3, _translate("MainWindow", "SemiAnnualPreview"))
        self.channel_dropdown.setItemText(4, _translate("MainWindow", "MonthlyEnterprise"))
        self.channel_dropdown.setItemText(5, _translate("MainWindow", "BetaChannel"))
        self.office_channel_label.setText(_translate("MainWindow", "Office Channel:"))
        self.enable_updates_label.setText(_translate("MainWindow", "Enable Updates:"))
        self.enable_updates_dropdown.setAccessibleName(_translate("MainWindow", "Enable updates drop down"))
        self.enable_updates_dropdown.setItemText(0, _translate("MainWindow", "False"))
        self.enable_updates_dropdown.setItemText(1, _translate("MainWindow", "True"))
        self.office_build_label.setText(_translate("MainWindow", "Office build:"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.bit_label.setText(_translate("MainWindow", "Office Client Edition:"))
        self.bit_dropdown.setAccessibleName(_translate("MainWindow", "Office client edition drop down"))
        self.bit_dropdown.setItemText(0, _translate("MainWindow", "64"))
        self.bit_dropdown.setItemText(1, _translate("MainWindow", "32"))
        self.office_build_dropdown.setAccessibleName(_translate("MainWindow", "Office build dropdown"))

        self.channel_dropdown.activated.connect(self.office_versions)
        self.submit_button.clicked.connect(self.submit)

    def office_versions(self):
        url = 'https://learn.microsoft.com/en-us/officeupdates/update-history-microsoft365-apps-by-date'
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        self.office_build_dropdown.clear()
        self.office_build_dropdown.setCurrentText("")

        urls = []
        for link in soup.find_all('a'):
            if self.channel_dropdown.currentText() == "Current":
                if "current-channel" in str(link.get('href')):
                    self.office_build_dropdown.addItem(link.getText())

            if self.channel_dropdown.currentText() == "SemiAnnualPreview":
                if "semi-annual-enterprise-channel-preview" in str(link.get('href')):
                    self.office_build_dropdown.addItem(link.getText())

            if self.channel_dropdown.currentText() == "SemiAnnual":
                if "semi-annual-enterprise-channel" in str(link.get('href')):
                    self.office_build_dropdown.addItem(link.getText())

            if self.channel_dropdown.currentText() == "MonthlyEnterprise":
                if "monthly-enterprise-channel" in str(link.get('href')):
                    self.office_build_dropdown.addItem(link.getText())

    def submit(self):
        desired_channel = self.channel_dropdown.currentText()
        bit = self.bit_dropdown.currentText()
        office_build = self.office_build_dropdown.currentText()
        enable_updates = self.enable_updates_dropdown.currentText()

        parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
        tree = ET.parse("config.xml", parser=parser)
        root = tree.getroot()

        for elememnt in root.iter():
            if elememnt.tag == "Add":
                elememnt.attrib["Channel"] = f"{desired_channel}"

        for elememnt in root.iter():
            if elememnt.tag == "Add":
                if office_build == "":
                    elememnt.attrib["Version"] = f"{office_build}"

                else:
                    elememnt.attrib["Version"] = f"16.0.{office_build[20:31]}"

        for elememnt in root.iter():
            if elememnt.tag == "Add":
                elememnt.attrib["OfficeClientEdition"] = f"{bit}"

        comments = [element for element in root.iter() if element.tag == ET.Comment]

        for comment in comments:
            if "Enabled" in comment.text:
                comment.text = f"  <Updates Enabled=\"{enable_updates}\" Channel=\"{desired_channel}\" />  "

        pup_up = Pop_Up()
        pup_up.exec()
        tree.write("config.xml")
        os.system('setup /configure config.xml')


class Ui_close_message(object):
    def setupUi(self, close_message):
        close_message.setObjectName("close_message")
        close_message.resize(487, 106)
        close_message.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.buttonBox = QtWidgets.QDialogButtonBox(close_message)
        self.buttonBox.setGeometry(QtCore.QRect(80, 50, 371, 51))
        self.buttonBox.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(close_message)
        self.label.setGeometry(QtCore.QRect(0, 10, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(close_message)
        self.buttonBox.accepted.connect(close_message.accept) # type: ignore
        self.buttonBox.rejected.connect(close_message.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(close_message)

        self.buttonBox.accepted.connect(lambda: mainWindow.hide())

    def retranslateUi(self, close_message):
        _translate = QtCore.QCoreApplication.translate
        close_message.setWindowTitle(_translate("close_message", "Dialog"))
        self.label.setText(_translate("close_message", "Would you like the close the application while office downloads?"))


class Pop_Up(QDialog):
    def __init__(self, parent=None):
        super(Pop_Up, self).__init__()
        self.ui.setupUi(self)
        self.ui = Ui_close_message()
        app.setStyle('windowsvista')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyWindow()
    mainWindow.show()
    sys.exit(app.exec_())