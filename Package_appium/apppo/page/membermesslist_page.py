from appium.webdriver.common.mobileby import MobileBy

from Package_appium.apppo.page.base_page import BasePage
from Package_appium.apppo.page.editmember_list import EditMemberPage


class MemberMessListPage(BasePage):
    def goto_editmember(self):
        # 点击编辑成员链接，进入编辑成员详情页面
        self.find_and_click(MobileBy.XPATH, "//*[@text='编辑成员']")
        return EditMemberPage(self.driver)
