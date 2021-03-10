from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from Package_appium.apppo.page.base_page import BasePage


class EditMemberPage(BasePage):
    def delmember(self):
        # 删除成员操作
        self.find_and_click(MobileBy.XPATH, "//*[@text='删除成员']")
        sleep(2)
        # 确定弹框，点击确定，删除成员
        self.find_and_click(MobileBy.XPATH, "//*[@text='确定']")
        sleep(2)
        self.driver.save_screenshot('screenshot/delresult.jpg')
