from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from Package_appium.apppo.page.base_page import BasePage
from Package_appium.apppo.page.membermessage_page import MemberMessagePage


class SearchPage(BasePage):
    def search(self):
        self.find(MobileBy.XPATH, "//*[@text='搜索']").send_keys('王一为')
        sleep(3)

    def goto_membermessage(self):
        find_ele = self.finds(MobileBy.XPATH, "//*[@text='王一为']")
        eles = len(find_ele)
        if eles > 1:
            print(f'找到了{eles - 1}个结果')
            self.driver.save_screenshot('screenshot/searchlist.jpg')
            find_ele[1].click()
        return MemberMessagePage(self.driver)
