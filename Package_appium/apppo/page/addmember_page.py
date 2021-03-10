from appium.webdriver.common.mobileby import MobileBy

from Package_appium.apppo.page.addmemberdetail_page import AddMemberDetail
from Package_appium.apppo.page.base_page import BasePage


class AddMember(BasePage):

    def addmember_menual(self):
        # 选择手动添加
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").classick()
        return AddMemberDetail(self.driver)
