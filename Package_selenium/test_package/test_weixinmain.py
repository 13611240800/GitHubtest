from time import sleep

from Package_selenium.WEIXINLogin_Package.main_page import MainPage


class TestMainPage:
    def test_weixinmain(self):
        m = MainPage()
        m.goto_download().go_to_mainpage()
        sleep(3)
