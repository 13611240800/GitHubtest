from Package_appium.apppo.page.app import App


class TestDelMember:
    def setup(self):
        self.app = App().start()
        self.main = self.app.goto_main()

    def teardown(self):
        pass

    def test_delmember(self):
        search_ele = self.main.goto_address().goto_search()
        search_ele.search()
        search_ele.goto_membermessage().goto_membermesslist().goto_editmember().delmember()
