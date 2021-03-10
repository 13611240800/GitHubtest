import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


# 基类，初始化，find,finds,find and click,find and sendkeys,swipe find
class BasePage:
    logging.basicConfig(level=logging.INFO, force=True, filename='../logs/config.log')

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locater, value):
        logging.info('find方法')
        logging.info(f'查找{locater},{value}')
        return self.driver.find_element(locater, value)

    def finds(self, locater, value):
        logging.info('finds方法')
        logging.info(f'查找{locater}，{value}')
        return self.driver.find_elements(locater, value)

    def find_and_click(self, locater, value):
        logging.info('find and click方法')
        logging.info(f'查找{locater},{value}')
        return self.driver.find_element(locater, value).click()

    def find_and_sendkeys(self, locater, value, sendvalue):
        logging.info('find and sendkeys方法')
        logging.info(f'查找{locater},{value},输入值{sendvalue}')
        return self.driver.find_element(locater, value).send_keys(sendvalue)

    def swipe_find(self, text, num=3):
        logging.info('滑动查找')
        logging.info('查找时')
        logging.info('set implicitly=1')
        self.driver.implicitly_wait(1)
        for i in range(num):
            if i == num:
                logging.info('没找到')
                logging.info('set implicitly=5')
                self.driver.implicitly_wait(5)
                raise Exception(f'找了{num}次，没找到')

            try:
                ele = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                logging.info('找到后')
                logging.info('set implicitly=5')
                self.driver.implicitly_wait(5)
                return ele
            except:
                print('未找到')
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get('height')
                start_x = width * 0.5
                start_y = height * 0.75
                end_x = start_x
                end_y = height * 0.25
                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)
