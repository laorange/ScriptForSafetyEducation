# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 450)
        MainWindow.setMinimumSize(QSize(800, 0))
        font = QFont()
        font.setFamilies([u"MiSans"])
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 95, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 100))
        font1 = QFont()
        font1.setFamilies([u"MiSans"])
        font1.setPointSize(24)
        self.label.setFont(font1)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.verticalLayout.addWidget(self.label)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.TARGET_URL = QLineEdit(self.centralwidget)
        self.TARGET_URL.setObjectName(u"TARGET_URL")
        self.TARGET_URL.setMinimumSize(QSize(115, 0))
        self.TARGET_URL.setAcceptDrops(False)
        self.TARGET_URL.setFrame(True)
        self.TARGET_URL.setDragEnabled(True)

        self.gridLayout_2.addWidget(self.TARGET_URL, 0, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.MAX_BIAS = QSpinBox(self.centralwidget)
        self.MAX_BIAS.setObjectName(u"MAX_BIAS")
        self.MAX_BIAS.setMaximum(3600)

        self.gridLayout.addWidget(self.MAX_BIAS, 1, 0, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.INTERVAL_BETWEEN_TWO_LESSON = QSpinBox(self.centralwidget)
        self.INTERVAL_BETWEEN_TWO_LESSON.setObjectName(u"INTERVAL_BETWEEN_TWO_LESSON")
        self.INTERVAL_BETWEEN_TWO_LESSON.setMinimum(10)
        self.INTERVAL_BETWEEN_TWO_LESSON.setMaximum(3600)

        self.gridLayout.addWidget(self.INTERVAL_BETWEEN_TWO_LESSON, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 2, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout_2.addWidget(self.progressBar, 3, 1, 1, 1)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 4, 0, 1, 1)

        self.totalProgressBar = QProgressBar(self.centralwidget)
        self.totalProgressBar.setObjectName(u"totalProgressBar")
        self.totalProgressBar.setValue(0)
        self.totalProgressBar.setAlignment(Qt.AlignCenter)
        self.totalProgressBar.setTextVisible(True)
        self.totalProgressBar.setInvertedAppearance(False)
        self.totalProgressBar.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout_2.addWidget(self.totalProgressBar, 4, 1, 1, 1)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 5, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        font2 = QFont()
        font2.setFamilies([u"MiSans"])
        font2.setPointSize(8)
        self.lineEdit_2.setFont(font2)
        self.lineEdit_2.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 6, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BROWSER = QComboBox(self.centralwidget)
        self.BROWSER.addItem("")
        self.BROWSER.addItem("")
        self.BROWSER.addItem("")
        self.BROWSER.setObjectName(u"BROWSER")

        self.horizontalLayout.addWidget(self.BROWSER)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout.addWidget(self.label_11)

        self.downloadDriverButton = QPushButton(self.centralwidget)
        self.downloadDriverButton.setObjectName(u"downloadDriverButton")

        self.horizontalLayout.addWidget(self.downloadDriverButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 1, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 7, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.findLocalDriver = QPushButton(self.centralwidget)
        self.findLocalDriver.setObjectName(u"findLocalDriver")

        self.horizontalLayout_2.addWidget(self.findLocalDriver)

        self.driverPath = QLabel(self.centralwidget)
        self.driverPath.setObjectName(u"driverPath")

        self.horizontalLayout_2.addWidget(self.driverPath)

        self.horizontalLayout_2.setStretch(1, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout_2, 7, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.checkLog = QPushButton(self.centralwidget)
        self.checkLog.setObjectName(u"checkLog")

        self.horizontalLayout_3.addWidget(self.checkLog)

        self.testDriver = QPushButton(self.centralwidget)
        self.testDriver.setObjectName(u"testDriver")

        self.horizontalLayout_3.addWidget(self.testDriver)

        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        font3 = QFont()
        font3.setFamilies([u"MiSans"])
        font3.setBold(True)
        self.start.setFont(font3)

        self.horizontalLayout_3.addWidget(self.start)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 94, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5b89\u5168\u6559\u80b2\u5237\u8bfe\u7a0b\u5e8f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u7f51\u5740\uff1a", None))
        self.TARGET_URL.setText(QCoreApplication.translate("MainWindow", u"http://weiban.mycourse.cn/#/course?projectType=normal", None))
        self.TARGET_URL.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7f51\u5740\u683c\u5f0f\uff1ahttp://weiban.mycourse.cn/#/course?projectType=...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6bcf\u8282\u8bfe\u7684\u5b8c\u6210\u65f6\u957f\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u79d2 (\u81f3\u5c1110\u79d2\u3002\u65f6\u95f4\u592a\u77ed\u5bb9\u6613\u88ab\u53d1\u73b0\u662f\u7528\u7a0b\u5e8f\u5237\u8bfe)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u79d2 (\u8ba9\u6bcf\u8282\u8bfe\u5b8c\u6210\u7684\u65f6\u95f4\u6709\u6240\u5dee\u5f02\uff0c\u82e5\u4e3a0\u5219\u76f8\u540c)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\u504f\u5dee\u4e0a\u9650\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u5ea6\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u603b\u8fdb\u5ea6\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u6d4f\u89c8\u5668\u9a71\u52a8\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u5728\u6d4f\u89c8\u5668\u8bbf\u95ee\uff1a", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"https://www.selenium.dev/zh-cn/documentation/webdriver/getting_started/install_drivers/", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6d4f\u89c8\u5668\uff1a", None))
        self.BROWSER.setItemText(0, QCoreApplication.translate("MainWindow", u"Edge", None))
        self.BROWSER.setItemText(1, QCoreApplication.translate("MainWindow", u"Firefox", None))
        self.BROWSER.setItemText(2, QCoreApplication.translate("MainWindow", u"Chrome", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u8fd8\u6ca1\u5b89\u88c5\u9a71\u52a8\uff1f\u8bf7\u5148\u67e5\u770b\u6d4f\u89c8\u5668\u7248\u672c\uff0c\u518d\u70b9\u6b64\u5904\u5b89\u88c5\u7248\u672c\u5339\u914d\u7684\u9a71\u52a8\uff1a", None))
        self.downloadDriverButton.setText(QCoreApplication.translate("MainWindow", u"\u5b89\u88c5\u9a71\u52a8", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u6d4f\u89c8\u5668\u9a71\u52a8\uff1a", None))
        self.findLocalDriver.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u627e\u6587\u4ef6", None))
        self.driverPath.setText("")
        self.checkLog.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u65e5\u5fd7", None))
        self.testDriver.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u9a71\u52a8", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5237\u8bfe", None))
    # retranslateUi
