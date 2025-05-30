from PySide6.QtWidgets import (QApplication,QWidget,QDialog,QLineEdit,QPushButton,QVBoxLayout,QLabel,QGridLayout,QHBoxLayout,
                               QComboBox)
from PySide6.QtUiTools import  QUiLoader
from PySide6.QtGui import QIcon,QPainter,QFont
from PySide6.QtCore import Qt,QCoreApplication,QFile
import sys
from Database import DataBase

db=DataBase()
app = QApplication(sys.argv)

def css(file):
    with open(file,'r') as f:
        cont=f.read()
        return  cont

file=QFile("C:/Users/DELL/Desktop/OpenSourceInterface/source2.ui")
loader = QUiLoader()
window = loader.load(file)

window.title1.setObjectName("title1")
window.title1.setStyleSheet(css("Interface.css"))



Rooms=[["Warge","Cr7","Javis","Rufus","Yoyi","Victor"],["Raymond","Esdras","Washington","Davie","Blessings","TableCut"]]

def MakeTheRoom():
    data = db.RetriveDB()

    for room in range(1,5):
        widget = QWidget()
        window.TabW.addTab(widget,str(room))
        window.TabW.setCurrentIndex(1)

        layout = QVBoxLayout()

        for dat in data:
            if int(dat[2]) == room:
                widget2= QWidget()
                label=QLabel(str(dat[0]))

                label.setObjectName("Ids")
                label.setStyleSheet(css("Interface.css"))

                dropMenu = QComboBox()

                dropMenu.setObjectName("dropMenu")
                dropMenu.setStyleSheet(css("Interface.css"))

                dropMenu.addItems(["Change ID", "Disable", "Delete"])

                layout2 = QHBoxLayout()

                layout2.addWidget(label)
                layout2.addWidget(dropMenu)
                widget2.setLayout(layout2)
                layout.setSpacing(0)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.addWidget(widget2,alignment=Qt.AlignmentFlag.AlignTop)

                widget2.setObjectName("mesho")
                widget2.setStyleSheet(css("Interface.css"))

        widget.setLayout(layout)


        # for mesho in room:
        #     widget2 = QWidget()
        #     label=QLabel(mesho)
        #
        #     label.setObjectName("Ids")
        #     label.setStyleSheet(css("Interface.css"))
        #
        #     dropMenu=QComboBox()
        #
        #     dropMenu.setObjectName("dropMenu")
        #     dropMenu.setStyleSheet(css("Interface.css"))
        #
        #     dropMenu.addItems(["Change ID","Disable","Delete"])
        #     layout2=QHBoxLayout()
        #
        #     layout2.addWidget(label)
        #     layout2.addWidget(dropMenu)
        #     widget2.setLayout(layout2)
        #     layout.addWidget(widget2)
        #
        #     widget2.setObjectName("mesho")
        #     widget2.setStyleSheet(css("Interface.css"))
        #
        # widget.setLayout(layout)

MakeTheRoom()
window.TabW.setObjectName("TabW")
window.TabW.setStyleSheet(css("Interface.css"))
window.setObjectName("body")
window.setStyleSheet(css("Interface.css"))

window.show()
app.exec()
