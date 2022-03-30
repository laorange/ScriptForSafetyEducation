__Author__ = "bilibili@辣橙yzc"
__version__ = "v2022.03.30"

import os
import sys
import traceback
from pathlib import Path
from threading import Thread

import selenium.common.exceptions
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow, QFileDialog
from PySide6.QtCore import Qt

from ui import Ui_MainWindow
from util import MyWebDriver, Handler, logger, BROWSER_CHOICE, my_signal, PROJECT_TYPE_CHOICE


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(f"安全教育刷课程序 {__version__}")
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint |
                            Qt.WindowCloseButtonHint | Qt.WindowStaysOnTopHint)

        self.TARGET_URL: str = ""
        self.INTERVAL_BETWEEN_TWO_LESSON: int = 20
        self.MAX_BIAS: int = 10
        self.driverPath: str = ""

        if not sys.platform.startswith('win'):
            QMessageBox.warning(self, "兼容性警告", "本程序在非Windows系统上使用可能会出现异常！")

        self.bind_slots_and_signals()

    def bind_slots_and_signals(self):
        self.ui.downloadDriverButton.clicked.connect(self.downloadDriverButtonFunction)
        self.ui.findLocalDriver.clicked.connect(self.findLocalDriverFunction)
        self.ui.testDriver.clicked.connect(self.testDriverFunction)
        self.ui.start.clicked.connect(self.startFunc)
        self.ui.projectType.currentIndexChanged.connect(self.changeProjectTypeFunction)

        self.ui.checkLog.triggered.connect(self.checkLogFunction)
        self.ui.whyNeedDriver.triggered.connect(lambda _: os.startfile("https://www.selenium.dev/zh-cn/documentation/webdriver/getting_started/"))
        self.ui.how2DownloadDriver.triggered.connect(
            lambda _: os.startfile("https://www.selenium.dev/zh-cn/documentation/webdriver/getting_started/install_drivers/"))
        self.ui.bilibili_v1.triggered.connect(lambda _: os.startfile("https://www.bilibili.com/video/BV1UL411t7CR"))
        self.ui.bilibili_v2.triggered.connect(lambda _: os.startfile("https://www.bilibili.com/video/BV1TL411c7mt"))
        self.ui.bilibili_v3.triggered.connect(lambda _: os.startfile("https://www.bilibili.com/video/BV1Wa41127fk"))
        self.ui.bilibili_v4.triggered.connect(lambda _: os.startfile("https://www.bilibili.com/video/BV18F411W7y2"))
        self.ui.github.triggered.connect(lambda _: os.startfile("https://github.com/laorange/ScriptForSafetyEducation"))
        self.ui.gitee.triggered.connect(lambda _: os.startfile("https://gitee.com/laorange/ScriptForSafetyEducation"))
        self.ui.how2GetVersionOfBrowser.triggered.connect(lambda _: os.startfile("https://jingyan.baidu.com/article/0964eca222def8c384f5361e.html"))

        my_signal.enable_start_button.connect(self.enable_start_button_function)
        my_signal.disable_start_button.connect(self.disable_download_button_function)
        my_signal.set_progress_bar.connect(self.set_progress_bar_function)
        my_signal.set_total_progress_bar.connect(self.set_total_progress_bar_function)
        my_signal.set_wait_progress_bar.connect(self.set_wait_progress_bar_function)

    def load_data(self) -> bool:
        self.INTERVAL_BETWEEN_TWO_LESSON = self.ui.INTERVAL_BETWEEN_TWO_LESSON.value()
        self.MAX_BIAS = self.ui.MAX_BIAS.value()
        self.driverPath = self.ui.driverPath.text()
        self.TARGET_URL = self.ui.TARGET_URL.text()
        if not self.driverPath or "未选择" in self.driverPath:
            QMessageBox.about(self, "提示", "请先“选择驱动文件”")
            return False
        if not self.TARGET_URL:
            QMessageBox.about(self, "提示", "目标网址为空")
            return False
        return True

    def get_browser_info(self, key: str):
        browser_index = self.ui.BROWSER.currentIndex()
        return BROWSER_CHOICE[browser_index][key]

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '关闭提示', "是否要退出界面？")
        if reply == QMessageBox.Yes:
            MyWebDriver.stop_flag = True
            sys.exit(app.exec())
        elif reply == QMessageBox.No:
            event.ignore()

    def downloadDriverButtonFunction(self):
        download_driver_url = self.get_browser_info("url")
        os.startfile(download_driver_url)

    def findLocalDriverFunction(self):
        file_dialog = QFileDialog(self)
        if driverPath := file_dialog.getOpenFileName(self, "请选择驱动器", filter="浏览器驱动(*.exe)")[0]:
            self.driverPath = driverPath
            self.ui.driverPath.setText(driverPath)
            logger.debug(f"选择了本地驱动器：{driverPath}，(当前浏览器：{self.get_browser_info('name')})")

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

    def testDriverFunction(self):
        try:
            if self.load_data():
                web = MyWebDriver(self.get_browser_info("driver"), self.driverPath)
                web.driver.close()
                QMessageBox.about(self, "成功", f"您的驱动已完成配置，可以开始使用了！")
        except Exception as e:
            logger.error(traceback.format_exc())
            QMessageBox.warning(self, "很抱歉", f"该驱动不可用。您可以在'开发'-'运行日志'中的最后一段描述找到详细原因")

    def enable_start_button_function(self):
        self.ui.start.setEnabled(True)

    def disable_download_button_function(self):
        self.ui.start.setDisabled(True)

    def set_progress_bar_function(self, progress_value: int):
        self.ui.progressBar.setValue(progress_value)

    def set_total_progress_bar_function(self, progress_value: int):
        self.ui.totalProgressBar.setValue(progress_value)

    def set_wait_progress_bar_function(self, progress_value: int):
        self.ui.waitProgressBar.setValue(progress_value)

    def changeProjectTypeFunction(self):
        self.ui.TARGET_URL.setText(PROJECT_TYPE_CHOICE[self.ui.projectType.currentIndex()])

    def startFunc(self):
        @logger.catch
        def task_func():
            handler = None
            try:
                handler = Handler(self.TARGET_URL, self.get_browser_info("driver"), self.driverPath,
                                  self.INTERVAL_BETWEEN_TWO_LESSON, self.MAX_BIAS)
                handler.start()
            except KeyboardInterrupt:
                logger.info("结束！")
            except selenium.common.exceptions.WebDriverException as e:
                logger.error(traceback.format_exc())
                QMessageBox.warning(self, "出错了", "出错了，详情可在“开发”中选择“查看日志”")
            except Exception:
                logger.error(traceback.format_exc())
                QMessageBox.warning(self, "出错了", "出错了，详情可在“开发”中选择“查看日志”")
            finally:
                if hasattr(handler, "web") and hasattr(handler.web, "driver"):
                    handler.web.driver.close()
            self.ui.start.setEnabled(True)
            my_signal.set_progress_bar.emit(0)
            my_signal.set_total_progress_bar.emit(0)
            my_signal.set_wait_progress_bar.emit(0)

        choice = QMessageBox.question(self, "使用须知",
                                      "1.该程序仅用于学习交流，请勿商用\n"
                                      "2.如果不着急，每节课的间隔时长可以设置在1分钟以上，尽量与正常看课时间接近，这样会非常安全\n"
                                      "3.使用该程序导致的任何后果请由使用者自行承担\n\n是否同意：")

        if choice == QMessageBox.Yes and self.load_data():
            task = Thread(target=task_func)
            task.start()
            self.ui.start.setDisabled(True)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
