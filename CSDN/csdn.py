from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PLATFORM = 'Android'
DEVICENAME = 'OPPO_R9m'
APP_PACKAGE = 'net.csdn.csdnplus'
APP_ACTIVITY = '.activity.MainActivity'
SERVER = 'http://localhost:4723/wd/hub'
NORESET = 'True'
TIMEOUT = 10
KEYWORD = 'python'  # 搜索关键字
SCROLL_START_X = 300  # 滑动起始位置横坐标
SCROLL_START_Y = 300  # 滑动起始位置纵坐标
SCROLL_DISTANCE = 400  # 滑动距离
SCROLL_SLEEP_TIME = 1  # 每两次滑动的间隔时间


class Action():

    def __init__(self):
        # 配置驱动
        self.desired_caps = {
            'platformName': PLATFORM,
            'deviceName': DEVICENAME,
            'appPackage': APP_PACKAGE,
            'appActivity': APP_ACTIVITY,
            'noReset': NORESET
        }
        self.driver = webdriver.Remote(SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def search(self):
        # 搜索
        sleep(5)
        self.wait.until(EC.presence_of_element_located((By.ID, 'net.csdn.csdnplus:id/iv_search')))
        self.driver.tap([(150, 150)])
        print("*"*100)
        search = self.wait.until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText')))
        search.send_keys(KEYWORD)
        button = self.wait.until(EC.element_to_be_clickable((By.ID, 'net.csdn.csdnplus:id/tv_search_search')))
        button.click()

    def scroll(self):
        # 模拟滑动操作
        while True:
            self.driver.swipe(SCROLL_START_X, SCROLL_START_Y+SCROLL_DISTANCE, SCROLL_START_X, SCROLL_START_Y)
            sleep(SCROLL_SLEEP_TIME)

    def main(self):
        self.search()
        self.scroll()


if __name__ == '__main__':
    action = Action()
    action.main()