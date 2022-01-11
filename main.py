import os
import sys
from pathlib import Path
from typing import Union

from PySide6.QtWidgets import (QApplication, QMessageBox, QMainWindow,
                               QWidget, QFileDialog)
from ui import Ui_MainWindow

__version__ = "3.0.0"
BROWSER_CHOICE = [
    {"name": "Edge", "url": "https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/"},
    {"name": "Firefox", "url": "https://github.com/mozilla/geckodriver/releases"},
    {"name": "Chrome", "url": "https://chromedriver.storage.googleapis.com/index.html"},
]


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(f"安全教育刷课程序 v{__version__}")

        self.TARGET_URL: str = r"http://weiban.mycourse.cn/#/course?projectType=normal"
        self.INTERVAL_BETWEEN_TWO_LESSON: int = 20
        self.MAX_BIAS: int = 10
        self.driverPath: str = ""

        self.bind_slots_and_signals()

    def bind_slots_and_signals(self):
        self.ui.downloadDriverButton.clicked.connect(self.downloadDriverButtonFunction)
        self.ui.findLocalDriver.clicked.connect(self.findLocalDriverFunction)
        self.ui.checkLog.clicked.connect(self.checkLogFunction)

    def load_data(self) -> bool:
        self.INTERVAL_BETWEEN_TWO_LESSON = self.ui.INTERVAL_BETWEEN_TWO_LESSON.value()
        self.MAX_BIAS = self.ui.MAX_BIAS.value()
        self.driverPath = self.ui.driverPath.text()
        if not self.driverPath:
            QMessageBox.about(self, "提示", "请先选择驱动器")
            return False
        return True

    def downloadDriverButtonFunction(self):
        browser_index = self.ui.BROWSER.currentIndex()
        download_driver_url = BROWSER_CHOICE[browser_index]['url']
        os.startfile(download_driver_url)

    def findLocalDriverFunction(self):
        file_dialog = QFileDialog(self)
        if driverPath := file_dialog.getOpenFileName(self, "请选择驱动器", filter="浏览器驱动(*.exe)")[0]:
            self.driverPath = driverPath
            self.ui.driverPath.setText(driverPath)

    def checkLogFunction(self):
        self.start_file(Path("运行日志.txt"))

    def start_file(self, path: Path):
        if sys.platform.startswith('win'):
            if path.exists():
                os.startfile(path)
            else:
                QMessageBox.warning(self, "很抱歉", f"{path} 不存在！")
        else:
            QMessageBox.warning(self, "很抱歉", "打开指定文件夹的功能仅支持在Windows上使用！")





if __name__ == '__main__':
    pass
