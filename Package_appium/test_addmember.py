from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAddMember:
    def setup(self):
        # 创建json串，客户端告诉server信息
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": True,
            "dontStopAppOnReset": True,
            "skipDeviceInitialization": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            # 执行过程中完成appium设置，动态等待时长
            "settings[waitForIdleTimeout]": 1,
            "automationName": "uiautomator2"
        }

        # 客户端和appium server端的链接
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_cap)

        # 隐式等待增强测试用例的稳定性
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_addmember(self):
        '''
        已登录状态（noReset=true）
        1.打开企业微信应用
        2.进入通讯录
        3.点击添加成员
        4.选择手动输入添加
        5.输入：姓名、手机号
        6.点击保存
        7.查找“添加成功”toast
        8.保存添加成功后截图
        9，退出企业微信应用
        :return:
        '''
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 点击添加成员
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                               '.scrollable(true).instance(0))'
                                                               '.scrollIntoView(new UiSelector()'
                                                               '.text("添加成员").instance(0));').click()
        # 选择手动添加
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 输入用户名、手机号，进行保存
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b7m']").send_keys('王一为')
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/fwi']").send_keys(
            '13611240808')
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # 查找“添加成功”toast弹框
        print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'成功')]").text)
        #         保存成功后截图
        self.driver.save_screenshot('save.jpg')
