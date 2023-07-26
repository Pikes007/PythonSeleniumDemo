from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestProject16(BaseClass):
    def test_e2e(self):
        home_page = HomePage(self.driver)
        check_out_page = home_page.shop_items()
        item_name = "Blackberry"
        check_out_page.select_item_by_name(item_name)
        check_out_page.check_out_items().click()
        confirm_page = check_out_page.complete_checkout()
        confirm_page.enter_country("India")
        confirm_page.select_checkbox()
        confirm_page.click_purchase()
        alert_text = confirm_page.get_success_alert_text()
        assert "Success! Thank you!" in alert_text
        print(alert_text)
        self.take_screenshot("success.png")
