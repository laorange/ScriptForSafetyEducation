__Author__ = ", ".join(["GitHub@laorange", "bilibili@辣橙yzc"])

import time

from selenium import webdriver
from loguru import logger
from tqdm import tqdm

import selenium.common.exceptions
from selenium.webdriver.common.by import By

logger.add('运行日志.txt', level="DEBUG", rotation="1 MB", retention='1 days', encoding="utf-8")


def sleep(secs: int, info: str = ""):
    secs = int(secs)
    for _ in tqdm(list(range(secs)), desc=f"{f'[{info}]-' if info else ''}等待{secs}秒"):
        time.sleep(1)


@logger.catch
class MyWebDriver:
    def __init__(self):
        try:
            self.driver = webdriver.Edge()
        except selenium.common.exceptions.SessionNotCreatedException:
            raise Exception(f"错误！您的浏览器驱动不匹配，请重新下载后将驱动器与程序放在同一文件夹下。\n"
                            f"请访问该链接来下载与您浏览器版本对应的驱动："
                            f"https://www.selenium.dev/zh-cn/documentation/webdriver/getting_started/install_drivers/")
        except selenium.common.exceptions.WebDriverException:
            raise Exception(f"错误！没有找到可用的浏览器驱动！\n"
                            f"请访问该链接来下载与您浏览器版本对应的驱动："
                            f"https://www.selenium.dev/zh-cn/documentation/webdriver/getting_started/install_drivers/")
        self.driver.maximize_window()

    def get(self, target_url: str):
        self.driver.get(target_url)
        self.driver.implicitly_wait(5)

    def query_selector(self, css_selector: str):
        try:
            return self.driver.find_element(by=By.CSS_SELECTOR, value=css_selector)
        except selenium.common.exceptions.NoSuchElementException:
            return None

    def query_selector_all(self, css_selector: str):
        return self.driver.find_elements(by=By.CSS_SELECTOR, value=css_selector)

    def get_iframe_body(self):
        inner_frame = self.query_selector("iframe.page-iframe")
        self.driver.switch_to.frame(inner_frame)
        inner_frame_body = self.query_selector("body")
        return inner_frame_body

    def filter_chapter(self):
        self.driver.implicitly_wait(5)
        sleep(3)
        raw_chapters = self.query_selector_all("li.folder-item")

        filtered_chapters_list = []
        for raw_chapter in raw_chapters:
            state = raw_chapter.find_element(by=By.CSS_SELECTOR, value=".state")
            if state.text and "/" in state.text:
                finished, total = tuple(map(int, state.text.split('/', 2)))
                if finished < total:
                    filtered_chapters_list.append(raw_chapter)
        return filtered_chapters_list


@logger.catch
class Handler:
    def __init__(self, target_url: str):
        self.target_url = target_url
        self.info()
        self.web = MyWebDriver()
        self.if_login = False

    def info(self):
        answer1 = input(f"即将访问的页面是：{self.target_url}，请问这是否为您想要刷的课？\n若是，请直接回车；若不是，请输入no：")
        if answer1 in ["n", "N", "no", "No"]:
            self.target_url = input("请注意，本程序是为安全教育（http://weiban.mycourse.cn）而设计的，并不适用于别的网站。\n"
                                    "请输入想要刷课的目标网址(应以 http://weiban.mycourse.cn/#/course?projectType=... 开头)：")
        print("\n使用提示：\n"
              "1.在接下来，会去调用浏览器驱动(webdriver)，如果驱动失败请下载与自己的浏览器匹配的驱动器，详情可查看我在b站发的视频(https://space.bilibili.com/384113181)\n"
              "2.将会跳转到安全教育的登录页面，请扫码登录后 回到这个黑框敲回车\n"
              "3.程序能跑，但不耐折腾，请勿在程序运行时，手动地和驱动器抢夺浏览器的控制权，否则可能会出现未知的bug\n"
              "4.如果遇到了问题，可以查看当前文件夹下的“运行日志”，也可以在视频的评论区留言讨论~\n"
              "5.如果想要终止程序，可以在这个黑框里按ctrl+c\n"
              "6.一键三连后(认真脸)，就可以开始啦\n")
        input("请在阅读上方的使用提示后(尤其是第二条)，敲击回车:")

    def start(self):
        self.web.get(self.target_url)
        self.ensure_login()
        self.chapter_list_page_func()

    def update_login_status(self):
        if r"/course" in self.web.driver.current_url:
            self.if_login = True

    def ensure_login(self):
        while not self.if_login:
            input("\n现在请您先扫码登录，确认已经了登录后，请敲回车：")
            self.web.get(self.target_url)
            self.update_login_status()

    def chapter_list_page_func(self):
        def next_step():
            self.web.driver.implicitly_wait(5)
            sleep(1)
            self.course_list_page_list()

        logger.debug("进入主页面")  # 章节列表页，可以算是主页面
        areas = self.web.query_selector("div.mint-tab-container-item:not([display=none])")
        if not areas:
            print("没检测到有效区域!")
            return

        parts = self.web.query_selector_all(".mint-navbar a")
        if parts:
            for part in parts:
                part.click()  # 点击导航栏的按钮，进入到某个板块儿
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
        sleep(10)
        inner_frame_body = self.web.driver.find_element(by=By.CSS_SELECTOR, value="body")
        self.web.driver.execute_script("finishWxCourse()", inner_frame_body)
        sleep(1)
        self.web.driver.switch_to.alert.accept()
        sleep(1)
        logger.info(f"完成课程：{self.web.driver.title}")
        self.start()

    def minimize_window(self):
        self.web.driver.minimize_window()


if __name__ == '__main__':
    TARGET_URL = r"http://weiban.mycourse.cn/#/course?projectType=normal"
    INTERVAL_BETWEEN_TWO_LESSON = 20
    MAX_BIAS = 10
    BROWSER_CHOICE = [
        {"name": "Edge", "url": "https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/"},
        {"name": "Firefox", "url": "https://github.com/mozilla/geckodriver/releases"},
        {"name": "Chrome", "url": "https://chromedriver.storage.googleapis.com/index.html"},
    ]

    handler = Handler(target_url=TARGET_URL)

    try:
        handler.start()
    except KeyboardInterrupt:
        logger.info("结束。将会在30秒后自动关闭页面")
        handler.minimize_window()
        sleep(30)
    except Exception as e:
        print(f"{e}\n\n出错了，详情请查看运行日志")
        input("敲击回车 来终止程序:")
    finally:
        if hasattr(handler, "web") and hasattr(handler.web, "driver"):
            handler.web.driver.close()
