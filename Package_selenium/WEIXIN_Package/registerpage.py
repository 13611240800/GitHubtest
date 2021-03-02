from Package_selenium.Base import Base


class RegisterPage():
    def __init__(self, driver):
        self.driver = driver

    def register(self):
        self.driver.find_element_by_xpath('//*[@id="corp_name"]').send_keys('wangwei')

    def go_to_mainpage(self):
        self.driver.find_element_by_xpath('//*[@class="ww_commonImg ww_commonImg_LogoSmall"]').click()
