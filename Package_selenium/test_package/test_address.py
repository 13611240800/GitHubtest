from Package_selenium.Address_Package.main2page import MainPage


class TestAddress:
    def test_address(self):
        MainPage().go_to_address().add_member()
