from selenium.webdriver.support.wait import WebDriverWait


class AddressPage:
    def __init__(self, driver):
        self.driver = driver

    def add_member(self):
        # 点击添加成员按钮,不可交互原因，1被遮挡，2有多个需要人工挑选合适的元素find_elements()[1]
        # 等待时间不够，可点击就是隐式等待的条件，但是逻辑还没有出来
        def wait_name(driver):
            ele = driver.find_elements_by_xpath('//*[@class="qui_btn ww_btn js_add_member"]')
            print(ele)
            if len(ele) < 3:
                ele[0].click()
            else:
                ele[1].click()
            eles = self.driver.find_elements_by_xpath('//*[@id="username"]')
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_name)
        # # self.driver.find_element_by_xpath('//*[@id="member_list"]/tr[1]').click()
        # # self.driver.find_element_by_xpath('//*[@id="js_contacts87"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
        # # 输入姓名
        # self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('wangwei3')
        # # 输入账号
        # self.driver.find_element_by_xpath('//*[@id="memberAdd_acctid"]').send_keys('ww003')
        # # 输入手机号
        # self.driver.find_element_by_xpath('//*[@id="memberAdd_phone"]').send_keys('13611240803')
        # # 保存
        # self.driver.find_element_by_xpath('//*[@class="qui_btn ww_btn js_btn_save"]').click()
