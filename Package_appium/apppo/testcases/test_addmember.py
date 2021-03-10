from Package_appium.apppo.page.app import App


class TestAddmember:
    def setup(self):
        self.app = App().start()
        self.main = self.app.goto_main()

    def teardown(self):
        self.app.stop()

    def test_addmember(self):
        name = '王一为'
        num = '13611240912'
        menual = self.main.goto_address().goto_addmember().addmember_menual()
        menual.addmemberditail(name, num)
        menual.verify_ok()
