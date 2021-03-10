from appium.webdriver.common.mobileby import MobileBy

from Package_appium.apppo.page.base_page import BasePage
from Package_appium.apppo.page.membermesslist_page import MemberMessListPage


class MemberMessagePage(BasePage):
    def goto_membermesslist(self):
        #     点击右上角的原点链接，进入个人信息列表页面
        self.find_and_click(MobileBy.ID, 'com.tencent.wework:id/iga')
        return MemberMessListPage(self.driver)
