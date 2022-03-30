import time
import traceback
from random import randint

from loguru import logger
from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from PySide6.QtCore import Signal, QObject

logger.add('运行日志.txt', level="DEBUG", retention='3 days', encoding="utf-8")
BROWSER_CHOICE = [
    {"name": "Edge", "driver": webdriver.Edge,
     "url": "https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/"},
    {"name": "Firefox", "driver": webdriver.Firefox,
     "url": "https://github.com/mozilla/geckodriver/releases"},
    {"name": "Chrome", "driver": webdriver.Chrome,
     "url": "https://chromedriver.storage.googleapis.com/index.html"},
]
PROJECT_TYPE_CHOICE = ["http://weiban.mycourse.cn/#/course?projectType=normal",
                       "http://weiban.mycourse.cn/#/course?projectType=pre",
                       "http://weiban.mycourse.cn/#/course?projectType=special", ""]


class MySignal(QObject):
    enable_start_button = Signal()
    disable_start_button = Signal()
    set_progress_bar = Signal(int)
    set_total_progress_bar = Signal(int)
    set_wait_progress_bar = Signal(int)


my_signal = MySignal()


def sleep(secs: int, info: str = ""):
    secs = int(secs)
    if info:
        logger.debug(f"{f'[{info}]-' if info else ''}等待{secs}秒")
    x = 1
    for t, _ in enumerate(range(x * secs)):
        if MyWebDriver.stop_flag:
            raise KeyboardInterrupt
        my_signal.set_wait_progress_bar.emit((t + 1) / (x * secs) * 100)
        time.sleep(1 / x)
    my_signal.set_wait_progress_bar.emit(100)


@logger.catch
class MyWebDriver:
    stop_flag = False
    finished_course_num = 0
    total_course_num = 0.001

    @staticmethod
    def init_num():
        MyWebDriver.finished_course_num = 0
        MyWebDriver.total_course_num = 0

    def add_one_finished_course(self):
        MyWebDriver.finished_course_num += 1
        self.refresh_progress_bar()

    def refresh_progress_bar(self):
        if MyWebDriver.total_course_num == 0:
            logger.error("没有检测到有效的课程")
            logger.error(f"当前url:{self.getDriver().current_url}")
        else:
            my_signal.set_progress_bar.emit(int(MyWebDriver.finished_course_num / MyWebDriver.total_course_num * 100))

    def __init__(self, driver, driver_path=""):
        try:
            self.driver = driver(driver_path)
        except selenium.common.exceptions.SessionNotCreatedException:
            raise Exception(f"错误！您的浏览器驱动不匹配，请重新下载驱动器")
        except selenium.common.exceptions.WebDriverException:
            raise Exception(f"错误！没有找到可用的浏览器驱动！")
        except:
            logger.error(traceback.format_exc())
            raise Exception(f"该浏览器驱动不可用！详情可在“开发”中选择“查看日志”")

        self.driver.maximize_window()

    def getDriver(self):
        if MyWebDriver.stop_flag:
            raise KeyboardInterrupt
        return self.driver

    def get(self, target_url: str):
        self.getDriver().get(target_url)
        self.getDriver().implicitly_wait(5)

    def query_selector(self, css_selector: str):
        try:
            return self.getDriver().find_element(by=By.CSS_SELECTOR, value=css_selector)
        except selenium.common.exceptions.NoSuchElementException:
            return None

    def query_selector_all(self, css_selector: str):
        return self.getDriver().find_elements(by=By.CSS_SELECTOR, value=css_selector)

    def get_iframe_body(self):
        inner_frame = self.query_selector("iframe.page-iframe")
        self.getDriver().switch_to.frame(inner_frame)
        inner_frame_body = self.query_selector("body")
        return inner_frame_body

    def filter_chapter(self):
        self.getDriver().implicitly_wait(5)
        sleep(3)
        raw_chapters = self.query_selector_all("li.folder-item")

        filtered_chapters_list = []
        for raw_chapter in raw_chapters:
            state = raw_chapter.find_element(by=By.CSS_SELECTOR, value=".state")
            if state.text and "/" in state.text:
                finished, total = tuple(map(int, state.text.split('/', 2)))
                MyWebDriver.finished_course_num += finished
                MyWebDriver.total_course_num += total
                if finished < total:
                    filtered_chapters_list.append(raw_chapter)
        self.refresh_progress_bar()
        return filtered_chapters_list


class Handler:
    def __init__(self, target_url: str, driver, driver_path: "",
                 interval_between_two_lesson: int = 10, max_bias: int = 10):
        self.target_url = target_url
        self.interval_between_two_lesson = interval_between_two_lesson
        self.max_bias = max_bias

        self.web = MyWebDriver(driver, driver_path)
        self.if_login = False

    @logger.catch
    def start(self):
        self.web.get(self.target_url)
        self.ensure_login()
        self.chapter_list_page_func()

    def update_login_status(self):
        if "login" not in self.web.driver.current_url:
            self.web.get(self.target_url)
            if r"/course" in self.web.driver.current_url:
                self.if_login = True

    def ensure_login(self):
        while not self.if_login:
            sleep(5)
            self.update_login_status()

    def chapter_list_page_func(self):
        def next_step():
            self.web.driver.implicitly_wait(5)
            sleep(1)
            self.course_list_page_list()

        logger.debug("进入主页面")  # 章节列表页，可以算是主页面
        areas = self.web.query_selector("div.mint-tab-container-item:not([display=none])")
        if not areas:
            logger.warning("没检测到有效区域!")
            return

        parts = self.web.query_selector_all(".mint-navbar a")
        if parts:
            for _index, part in enumerate(parts):
                self.web.init_num()
                part.click()  # 点击导航栏的按钮，进入到某个板块儿
                total_progress = int((_index + 1) / len(parts) * 100)
                my_signal.set_total_progress_bar.emit(total_progress)
                if filtered_chapters := self.web.filter_chapter():
                    filtered_chapters[0].find_element(by=By.CSS_SELECTOR, value=".btn").click()
                    next_step()
                    break
        else:
            if filtered_chapters := self.web.filter_chapter():
                filtered_chapters[0].find_element(by=By.CSS_SELECTOR, value=".btn").click()
                next_step()
        raise KeyboardInterrupt

    def course_list_page_list(self):
        logger.debug("进入章节页面")
        courses = self.web.query_selector_all(".course")
        for course in courses:
            if course.text and not course.find_elements(by=By.CSS_SELECTOR, value="h3>i"):
                course.click()
                self.web.driver.implicitly_wait(5)
                sleep(3)
                self.course_page_list()
                return
        self.start()

    def course_page_list(self):
        logger.debug("进入课程页面")
        inner_frame = self.web.driver.find_element(by=By.CSS_SELECTOR, value="iframe")
        self.web.driver.switch_to.frame(inner_frame)
        sleep(self.interval_between_two_lesson + randint(0, self.max_bias + 1), "课程不能刷太快，等一等")
        inner_frame_body = self.web.driver.find_element(by=By.CSS_SELECTOR, value="body")
        self.web.driver.execute_script("finishWxCourse()", inner_frame_body)
        sleep(1)
        self.web.driver.switch_to.alert.accept()
        sleep(1)
        logger.info(f"完成课程：{self.web.driver.title}")
        self.web.add_one_finished_course()
        self.start()

    def minimize_window(self):
        self.web.driver.minimize_window()


if __name__ == '__main__':
    TARGET_URL = r"http://weiban.mycourse.cn/#/course?projectType=normal"
    INTERVAL_BETWEEN_TWO_LESSON = 20
    MAX_BIAS = 10
    handler = Handler(target_url=TARGET_URL, driver=BROWSER_CHOICE[0]["driver"])

    try:
        handler.start()
    except KeyboardInterrupt:
        logger.info("结束。将会在30秒后自动关闭页面")
        handler.minimize_window()
        sleep(30)
    except Exception as e:
        logger.error(traceback.format_exc())
        raise Exception
    finally:
        if hasattr(handler, "web") and hasattr(handler.web, "driver"):
            handler.web.driver.close()
