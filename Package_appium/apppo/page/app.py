# 启动 停止 重启app
import yaml
from appium import webdriver

from Package_appium.apppo.page.base_page import BasePage
from Package_appium.apppo.page.main_page import MainPage

with open('../datas/desire_cap.yml', encoding='UTF-8') as f:
    datas = yaml.safe_load(f)
    desire_cap = datas['desirecaps']
    ip = datas['server']['ip']
    port = datas['server']['port']


class App(BasePage):
    def start(self):
        # 以配置文件的方式读取
        if self.driver == None:
            #  启动app
            # 创建json串，客户端告诉server信息
            # desire_cap = {
            #     "platformName": "android",
            #     "deviceName": "127.0.0.1:7555",
            #     "appPackage": "com.tencent.wework",
            #     "appActivity": ".launch.LaunchSplashActivity",
            #     "noReset": True,
            #     "dontStopAppOnReset": True,
            #     "skipServerInstallation": True,
            #     "skipDeviceInitialization": True,
            #     "unicodeKeyboard": True,
            #     "resetKeyboard": True,
            #     # 执行过程中完成appium设置，动态等待时长
            #     "settings[waitForIdleTimeout]": 1,
            #     "automationName": "uiautomator2"
            # }
            # 客户端和appium server端的链接
            self.driver = webdriver.Remote(f'http://{ip}:{port}/wd/hub', desire_cap)
            # 隐式等待增强测试用例的稳定性
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        # 重启app
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        # 停止app
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)
