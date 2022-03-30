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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 475)
        MainWindow.setMinimumSize(QSize(700, 0))
        font = QFont()
        MainWindow.setFont(font)
        self.whyNeedDriver = QAction(MainWindow)
        self.whyNeedDriver.setObjectName(u"whyNeedDriver")
        self.how2DownloadDriver = QAction(MainWindow)
        self.how2DownloadDriver.setObjectName(u"how2DownloadDriver")
        self.action_B = QAction(MainWindow)
        self.action_B.setObjectName(u"action_B")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.bilibili_v1 = QAction(MainWindow)
        self.bilibili_v1.setObjectName(u"bilibili_v1")
        self.bilibili_v2 = QAction(MainWindow)
        self.bilibili_v2.setObjectName(u"bilibili_v2")
        self.bilibili_v3 = QAction(MainWindow)
        self.bilibili_v3.setObjectName(u"bilibili_v3")
        self.actionGithub = QAction(MainWindow)
        self.actionGithub.setObjectName(u"actionGithub")
        self.actionGitee = QAction(MainWindow)
        self.actionGitee.setObjectName(u"actionGitee")
        self.checkLog = QAction(MainWindow)
        self.checkLog.setObjectName(u"checkLog")
        self.github = QAction(MainWindow)
        self.github.setObjectName(u"github")
        self.actionGitee_2 = QAction(MainWindow)
        self.actionGitee_2.setObjectName(u"actionGitee_2")
        self.how2GetVersionOfBrowser = QAction(MainWindow)
        self.how2GetVersionOfBrowser.setObjectName(u"how2GetVersionOfBrowser")
        self.bilibili_v4 = QAction(MainWindow)
        self.bilibili_v4.setObjectName(u"bilibili_v4")
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

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.projectType = QComboBox(self.centralwidget)
        self.projectType.addItem("")
        self.projectType.addItem("")
        self.projectType.addItem("")
        self.projectType.addItem("")
        self.projectType.setObjectName(u"projectType")

        self.horizontalLayout_5.addWidget(self.projectType)

        self.TARGET_URL = QLineEdit(self.centralwidget)
        self.TARGET_URL.setObjectName(u"TARGET_URL")
        self.TARGET_URL.setMinimumSize(QSize(115, 0))
        self.TARGET_URL.setAcceptDrops(False)
        self.TARGET_URL.setFrame(True)
        self.TARGET_URL.setDragEnabled(True)

        self.horizontalLayout_5.addWidget(self.TARGET_URL)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)

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

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 3, 0, 1, 1)

        self.waitProgressBar = QProgressBar(self.centralwidget)
        self.waitProgressBar.setObjectName(u"waitProgressBar")
        self.waitProgressBar.setValue(0)
        self.waitProgressBar.setAlignment(Qt.AlignCenter)
        self.waitProgressBar.setTextVisible(True)
        self.waitProgressBar.setInvertedAppearance(False)
        self.waitProgressBar.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout_2.addWidget(self.waitProgressBar, 3, 1, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout_2.addWidget(self.progressBar, 4, 1, 1, 1)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 5, 0, 1, 1)

        self.totalProgressBar = QProgressBar(self.centralwidget)
        self.totalProgressBar.setObjectName(u"totalProgressBar")
        self.totalProgressBar.setValue(0)
        self.totalProgressBar.setAlignment(Qt.AlignCenter)
        self.totalProgressBar.setTextVisible(True)
        self.totalProgressBar.setInvertedAppearance(False)
        self.totalProgressBar.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout_2.addWidget(self.totalProgressBar, 5, 1, 1, 1)

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
        self.BROWSER.setFont(font)

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
        font2 = QFont()
        font2.setBold(True)
        self.findLocalDriver.setFont(font2)

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

        self.testDriver = QPushButton(self.centralwidget)
        self.testDriver.setObjectName(u"testDriver")
        font3 = QFont()
        font3.setPointSize(12)
        self.testDriver.setFont(font3)

        self.horizontalLayout_3.addWidget(self.testDriver)

        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.start.setFont(font4)

        self.horizontalLayout_3.addWidget(self.start)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_14)

        self.verticalSpacer_2 = QSpacerItem(20, 94, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_B = QMenu(self.menu)
        self.menu_B.setObjectName(u"menu_B")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.gitee = QMenu(self.menu_3)
        self.gitee.setObjectName(u"gitee")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.how2GetVersionOfBrowser)
        self.menu.addAction(self.whyNeedDriver)
        self.menu.addAction(self.how2DownloadDriver)
        self.menu.addSeparator()
        self.menu.addAction(self.menu_B.menuAction())
        self.menu_B.addAction(self.bilibili_v1)
        self.menu_B.addAction(self.bilibili_v2)
        self.menu_B.addAction(self.bilibili_v3)
        self.menu_B.addAction(self.bilibili_v4)
        self.menu_3.addAction(self.checkLog)
        self.menu_3.addAction(self.gitee.menuAction())
        self.gitee.addAction(self.github)
        self.gitee.addAction(self.actionGitee_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.whyNeedDriver.setText(QCoreApplication.translate("MainWindow", u"\u4e3a\u4ec0\u4e48\u9700\u8981\u6d4f\u89c8\u5668\u9a71\u52a8", None))
        self.how2DownloadDriver.setText(QCoreApplication.translate("MainWindow", u"\u600e\u4e48\u5b89\u88c5\u6d4f\u89c8\u5668\u9a71\u52a8", None))
        self.action_B.setText(QCoreApplication.translate("MainWindow", u"\u672c\u7a0b\u5e8f\u5728B\u7ad9\u7684\u89c6\u9891", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u7a0b\u5e8f\u6e90\u4ee3\u7801", None))
        self.bilibili_v1.setText(QCoreApplication.translate("MainWindow", u"1.\u65b0\u751f\u5b89\u5168\u6559\u80b2(2021.8.19)", None))
        self.bilibili_v2.setText(QCoreApplication.translate("MainWindow", u"2.\u5b89\u5168\u6559\u80b2(2022.1.10)", None))
        self.bilibili_v3.setText(QCoreApplication.translate("MainWindow", u"3.\u56fe\u5f62\u754c\u9762(2022.2.1)", None))
        self.actionGithub.setText(QCoreApplication.translate("MainWindow", u"Github(\u53ef\u80fd\u4f1a\u88ab\u5899)", None))
        self.actionGitee.setText(QCoreApplication.translate("MainWindow", u"Gitee", None))
        self.checkLog.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u65e5\u5fd7", None))
        self.github.setText(QCoreApplication.translate("MainWindow", u"Github(\u53ef\u80fd\u4f1a\u88ab\u5899)", None))
        self.actionGitee_2.setText(QCoreApplication.translate("MainWindow", u"Gitee", None))
        self.how2GetVersionOfBrowser.setText(QCoreApplication.translate("MainWindow", u"\u600e\u4e48\u67e5\u770b\u6d4f\u89c8\u5668\u7248\u672c\u53f7", None))
        self.bilibili_v4.setText(QCoreApplication.translate("MainWindow", u"4.\u4fe1\u53f7\u4e0e\u69fd(2022.3.24)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5b89\u5168\u6559\u80b2\u5237\u8bfe\u7a0b\u5e8f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u7f51\u5740\uff1a", None))
        self.projectType.setItemText(0, QCoreApplication.translate("MainWindow", u"\u901a\u7528\u5b89\u5168\u6559\u80b2", None))
        self.projectType.setItemText(1, QCoreApplication.translate("MainWindow", u"\u65b0\u751f\u5b89\u5168\u6559\u80b2", None))
        self.projectType.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4e13\u9898\u5b89\u5168\u6559\u80b2", None))
        self.projectType.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5176\u4ed6(\u8bf7\u5728\u53f3\u4fa7\u6846\u5185\u586b\u5199)", None))

        self.TARGET_URL.setText(QCoreApplication.translate("MainWindow", u"http://weiban.mycourse.cn/#/course?projectType=normal", None))
        self.TARGET_URL.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7f51\u5740\u683c\u5f0f\uff1ahttp://weiban.mycourse.cn/#/course?projectType=...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6bcf\u8282\u8bfe\u7684\u5b8c\u6210\u65f6\u957f\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u79d2 (\u81f3\u5c1110\u79d2\u3002\u65f6\u95f4\u592a\u77ed\u5bb9\u6613\u88ab\u53d1\u73b0\u662f\u7528\u7a0b\u5e8f\u5237\u8bfe)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u79d2 (\u8ba9\u6bcf\u8282\u8bfe\u5b8c\u6210\u7684\u65f6\u95f4\u6709\u6240\u5dee\u5f02; \u82e5\u4e3a0, \u5219\u76f8\u540c)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\u504f\u5dee\u4e0a\u9650\uff1a", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u7b49\u5f85\u8fdb\u5ea6\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u5757\u8fdb\u5ea6\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u603b\u8fdb\u5ea6\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6d4f\u89c8\u5668\uff1a", None))
        self.BROWSER.setItemText(0, QCoreApplication.translate("MainWindow", u"Edge", None))
        self.BROWSER.setItemText(1, QCoreApplication.translate("MainWindow", u"Firefox", None))
        self.BROWSER.setItemText(2, QCoreApplication.translate("MainWindow", u"Chrome", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u8fd8\u6ca1\u5b89\u88c5\u9a71\u52a8\uff1f\u8bf7\u5148\u67e5\u770b\u6d4f\u89c8\u5668\u7248\u672c\uff0c\u518d\u70b9\u6b64\u5904\u5b89\u88c5\u7248\u672c\u5339\u914d\u7684\u9a71\u52a8\uff1a", None))
        self.downloadDriverButton.setText(QCoreApplication.translate("MainWindow", u"\u5b89\u88c5\u9a71\u52a8", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u6d4f\u89c8\u5668\u9a71\u52a8\uff1a", None))
        self.findLocalDriver.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u9a71\u52a8\u6587\u4ef6", None))
        self.driverPath.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u672a\u9009\u62e9\u9a71\u52a8\u6587\u4ef6", None))
        self.testDriver.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u9a71\u52a8", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5237\u8bfe", None))
        self.label_14.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.menu_B.setTitle(QCoreApplication.translate("MainWindow", u"\u672c\u7a0b\u5e8f\u76f8\u5173B\u7ad9\u89c6\u9891", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5f00\u53d1", None))
        self.gitee.setTitle(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u7a0b\u5e8f\u6e90\u4ee3\u7801", None))
    # retranslateUi

