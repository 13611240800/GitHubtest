from appium.webdriver.common.mobileby import MobileBy

# 主页

from Package_appium.apppo.page.addresslist_page import AddresslistPage
from Package_appium.apppo.page.base_page import BasePage


class MainPage(BasePage):
    addresslist_ele = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_address(self):
        # 点击通讯录
        self.find_and_click(*self.addresslist_ele)
        # self.driver.find_elementslement(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddresslistPage(self.driver)
