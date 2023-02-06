from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtGui, QtCore
import sys
import xml.etree.ElementTree as ET
import os
import string


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.submit_button.clicked.connect(self.submit)


    def submit(self):
        desired_channel = self.channel_dropdown.currentText()
        bit = self.bit_dropdown.currentText()
        office_build = self.office_build_edit_area.text()
        enable_updates = self.enable_updates_dropdown.currentText()

        parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
        tree = ET.parse("config.xml", parser=parser)
        root = tree.getroot()



        for elememnt in root.iter():
            if elememnt.tag == "Add":
                elememnt.attrib["Channel"] = f"{desired_channel}"

        for elememnt in root.iter():
            if elememnt.tag == "Add":
                elememnt.attrib["Version"] = f"{office_build}"

        for elememnt in root.iter():
            if elememnt.tag == "Add":
                elememnt.attrib["OfficeClientEdition"] = f"{bit}"

        comments = [element for element in root.iter() if element.tag == ET.Comment]

        for comment in comments:
            if "Enabled" in comment.text:
                comment.text = f"  <Updates Enabled=\"{enable_updates}\" Channel=\"{desired_channel}\" />  "


        tree.write("config.xml")
        os.system('setup /configure config.xml')




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyWindow()
    mainWindow.show()
    sys.exit(app.exec_())