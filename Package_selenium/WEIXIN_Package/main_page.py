from selenium import webdriver

from Package_selenium.WEIXINLogin_Package.downloadpage import DownloadPage
from Package_selenium.WEIXINLogin_Package.loginpage import LoginPage
from Package_selenium.WEIXINLogin_Package.registerpage import RegisterPage


# class DownloadPage(object):
#     pass


class MainPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('https://work.weixin.qq.com/')

    def goto_register(self):
        self.driver.find_element_by_xpath('//*[@id="tmp"]/div[1]/a').click()
        return RegisterPage(self.driver)

    def goto_login(self):
        self.driver.find_element_by_xpath('//*[@class="index_top_operation_loginBtn"]').click()
        return LoginPage(self.driver)

    def goto_download(self):
        self.driver.find_element_by_xpath('//*[@class="index_top_operation_registerBtn"]').click()
        return DownloadPage(self.driver)
