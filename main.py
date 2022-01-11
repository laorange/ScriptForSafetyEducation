__Author__ = ", ".join(["GitHub@laorange", "bilibili@辣橙yzc"])

from selenium import webdriver
import time
from traceback import print_exc
from pathlib import Path

BASE_DIR = Path(__file__).parent

# 创建浏览器对象
driver = webdriver.Edge(str(BASE_DIR / "msedgedriver.exe"))
# 窗口最大化显示
driver.maximize_window()

url = r"https://weiban.mycourse.cn/index.html#/course?projectType=pre"
driver.get(url)

start_time = time.perf_counter()
login = False
course_p_percent = 1
course_progress_percent = 0


def exe(if_debug: bool = False):
    global login, start_time, course_p_percent, course_progress_percent

    css_selector_chapter = ".folder-list > .folder-item"
    chapters = []

    while not chapters:
        if not login:
            time.sleep(10)  # 用于登录
        driver.implicitly_wait(5)
        if not str(driver.current_url).endswith("login"):
            driver.get(url)
        driver.implicitly_wait(5)
        chapters = driver.find_elements_by_css_selector(css_selector_chapter)

    if not login:
        start_time = time.perf_counter()
        login = True
        progress_percent_pre = driver.find_element_by_css_selector(".progress-percent").text
        progress_percent = float(str(progress_percent_pre)[:-1])
        course_p_percent = progress_percent / 80 if progress_percent < 80 else 1
        if course_p_percent == 1:
            email_c = "经检查，您的课程已全部完成，请在公众号“平安航大”的“安全微伴”中查看。"
        else:
            email_c = "已开始学习。经检查，您的当前进度为{}".format(progress_percent_pre)
        print(email_c)

    finished_chapters_amount = 0
    for chapter in chapters:  # 遍历所有章节
        state = str(chapter.find_element_by_css_selector(".state").text)
        assert state
        finished, total = tuple(state.split('/', 2))

        if finished == total and not if_debug:
            finished_chapters_amount += 1
            continue  # 这一章节刷完了

        # 进入到某个章节中
        chapter.find_element_by_css_selector("div.folder-extra > a.btn").click()
        driver.implicitly_wait(5)

        # 章节 > 课程  获取列表最上面的那节课
        css_selector_course = ".course-list > li:nth-child(1)"
        course = driver.find_element_by_css_selector(css_selector_course)

        if not if_debug:
            if course.find_elements_by_css_selector("h3 > i"):  # 最上面的课已经处于完成状态了，则返回
                return False

        course.find_element_by_css_selector("h3").click()  # 进入该课程
        driver.implicitly_wait(15)
        time.sleep(6)

        inner_frame = driver.find_element_by_css_selector("iframe.page-iframe")
        driver.switch_to.frame(inner_frame)
        time.sleep(5)
        inner_frame_body = driver.find_element_by_css_selector("body")
        driver.execute_script("finishWxCourse()", inner_frame_body)

        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(1)
        return False

    if finished_chapters_amount == len(chapters):  # 所有章节都刷完时
        durant = "共用时：{:.2f}秒".format(time.perf_counter() - start_time)
        print(f'您的课程已全部完成。{durant}')
        input("\n请敲击回车来结束程序：")
        return True  # 课刷完了，程序终止
    else:
        return False


if __name__ == '__main__':
    FINISHED = False
    while not FINISHED:
        try:
            FINISHED = exe()
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(e)
            print_exc()
            time.sleep(10)
