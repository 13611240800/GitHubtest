from appium.webdriver.common.mobileby import MobileBy

from Package_appium.apppo.page.base_page import BasePage


class AddMemberDetail(BasePage):

    def addmemberditail(self, name, num):
        self.find_and_sendkeys(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@text='必填']", name)
        self.find_and_sendkeys(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='必填']", num)
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")

    def verify_ok(self):
        # 查找“添加成功”toast弹框
        print(self.find(MobileBy.XPATH, "//*[contains(@text,'成功')]").text)
        print(self.driver.page_source)
        #         保存成功后截图
        self.driver.save_screenshot('screenshot/save.jpg')
