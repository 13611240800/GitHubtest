from time import sleep

from Package_selenium.WEIXINLogin_Package.registerpage import RegisterPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def scan(self):
        pass

    def goto_register(self):
        self.driver.find_element_by_xpath('//*[@class="login_registerBar_link"]').click()
        sleep(3)
        return RegisterPage(self.driver)
