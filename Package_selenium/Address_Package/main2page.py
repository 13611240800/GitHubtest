from selenium import webdriver

from Package_selenium.Address_Package.addresspage import AddressPage


class MainPage():
    def __init__(self):
        # 声明chrome参数
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        # chrome - -remote - debugging - port = 9222
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.implicitly_wait(5)

    def go_to_address(self):
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        return AddressPage(self.driver)
