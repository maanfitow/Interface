# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'first_w.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QGroupBox,
    QLabel, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setMinimumSize(QSize(1024, 600))
        MainWindow.setMaximumSize(QSize(1024, 600))
        MainWindow.setStyleSheet(u"background-color: rgb(245, 251, 255)")
        self.frame = QFrame(MainWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(924, 500))
        self.frame.setMaximumSize(QSize(924, 500))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.bt_capture = QPushButton(self.frame)
        self.bt_capture.setObjectName(u"bt_capture")
        self.bt_capture.setGeometry(QRect(80, 410, 91, 41))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.bt_capture.setFont(font)
        self.bt_capture.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255,255,255);\n"
"border-radius:10px")
        self.bt_clear = QPushButton(self.frame)
        self.bt_clear.setObjectName(u"bt_clear")
        self.bt_clear.setGeometry(QRect(210, 410, 91, 41))
        self.bt_clear.setFont(font)
        self.bt_clear.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255,255,255);\n"
"border-radius:10px")
        self.bt_save = QPushButton(self.frame)
        self.bt_save.setObjectName(u"bt_save")
        self.bt_save.setGeometry(QRect(340, 410, 91, 41))
        self.bt_save.setFont(font)
        self.bt_save.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255,255,255);\n"
"border-radius:10px")
        self.label_1 = QLabel(self.frame)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(70, 120, 81, 31))
        self.label_1.setFont(font)
        self.label_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 180, 81, 31))
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 240, 81, 31))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 300, 81, 31))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gb_water = QGroupBox(self.frame)
        self.gb_water.setObjectName(u"gb_water")
        self.gb_water.setGeometry(QRect(200, 300, 231, 41))
        self.rb_yes = QRadioButton(self.gb_water)
        self.rb_yes.setObjectName(u"rb_yes")
        self.rb_yes.setGeometry(QRect(50, 10, 71, 20))
        self.rb_yes.setFont(font)
        self.label = QLabel(self.gb_water)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 10, 16, 16))
        self.label.setFont(font)
        self.rb_no = QRadioButton(self.gb_water)
        self.rb_no.setObjectName(u"rb_no")
        self.rb_no.setGeometry(QRect(130, 10, 71, 20))
        self.rb_no.setFont(font)
        self.rb_no.setChecked(True)
        self.sp_width = QSpinBox(self.frame)
        self.sp_width.setObjectName(u"sp_width")
        self.sp_width.setEnabled(True)
        self.sp_width.setGeometry(QRect(200, 180, 231, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.sp_width.setFont(font1)
        self.sp_width.setAlignment(Qt.AlignCenter)
        self.sp_width.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sp_width.setMaximum(10000)
        self.sp_volume = QSpinBox(self.frame)
        self.sp_volume.setObjectName(u"sp_volume")
        self.sp_volume.setEnabled(True)
        self.sp_volume.setGeometry(QRect(200, 240, 231, 31))
        self.sp_volume.setFont(font1)
        self.sp_volume.setAlignment(Qt.AlignCenter)
        self.sp_volume.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sp_volume.setMaximum(10000)
        self.sp_height = QSpinBox(self.frame)
        self.sp_height.setObjectName(u"sp_height")
        self.sp_height.setEnabled(True)
        self.sp_height.setGeometry(QRect(200, 120, 231, 31))
        self.sp_height.setFont(font1)
        self.sp_height.setWrapping(False)
        self.sp_height.setAlignment(Qt.AlignCenter)
        self.sp_height.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sp_height.setMaximum(10000)
        self.bt_form = QPushButton(self.frame)
        self.bt_form.setObjectName(u"bt_form")
        self.bt_form.setGeometry(QRect(550, 30, 91, 41))
        self.bt_form.setFont(font)
        self.bt_form.setStyleSheet(u"background-color: rgb(117, 117, 117);\n"
"color: rgb(255,255,255);\n"
"border-radius:10px")
        self.bt_form.setCheckable(False)
        self.bt_database = QPushButton(self.frame)
        self.bt_database.setObjectName(u"bt_database")
        self.bt_database.setGeometry(QRect(710, 30, 91, 41))
        self.bt_database.setFont(font)
        self.bt_database.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"color: rgb(117,117,117);\n"
"border-radius:10px")
        self.img_oak = QLabel(self.frame)
        self.img_oak.setObjectName(u"img_oak")
        self.img_oak.setGeometry(QRect(510, 110, 350, 350))
        font2 = QFont()
        font2.setBold(False)
        self.img_oak.setFont(font2)
        self.img_oak.setStyleSheet(u"")
        self.img_oak.setFrameShape(QFrame.Box)
        self.chkOAK = QPushButton(self.frame)
        self.chkOAK.setObjectName(u"chkOAK")
        self.chkOAK.setGeometry(QRect(240, 30, 141, 41))
        self.chkOAK.setFont(font)
        self.chkOAK.setStyleSheet(u"background-color: rgb(255, 37, 80);\n"
"color: rgb(255,255,255);\n"
"border-radius:10px")
        self.chkOAK.setCheckable(True)
        MainWindow.setCentralWidget(self.frame)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dialog", None))
        self.bt_capture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.bt_clear.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.bt_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Water", None))
        self.gb_water.setTitle("")
        self.rb_yes.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.rb_no.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.bt_form.setText(QCoreApplication.translate("MainWindow", u"Form", None))
        self.bt_database.setText(QCoreApplication.translate("MainWindow", u"Database", None))
        self.img_oak.setText("")
        self.chkOAK.setText(QCoreApplication.translate("MainWindow", u"Enable CAM", None))
    # retranslateUi

