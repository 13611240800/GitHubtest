class DownloadPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_mainpage(self):
        # self.driver.find_element_by_xpath('//*[@class="ww_officialImg ww_officialImg_LogoBlue"]').click()
        self.driver.find_element_by_xpath('//*[@class="ww_officialImg ww_officialImg_LogoBlue"]').click()
