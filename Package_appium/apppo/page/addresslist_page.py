from appium.webdriver.common.mobileby import MobileBy

from Package_appium.apppo.page.addmember_page import AddMember
from Package_appium.apppo.page.base_page import BasePage
from Package_appium.apppo.page.search_page import SearchPage


class AddresslistPage(BasePage):

    def goto_addmember(self):
        element = self.swipe_find('添加成员')
        element.click()
        return AddMember(self.driver)

    def goto_search(self):
        #         进入查找页面
        self.find_and_click(MobileBy.ID, 'com.tencent.wework:id/igk')
        return SearchPage(self.driver)
