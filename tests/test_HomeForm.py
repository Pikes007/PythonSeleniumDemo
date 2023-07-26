import pytest

from TestData.FormSubmissionData import FormSubmissionData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHome(BaseClass):

    def test_form_submission(self, get_data):
        home_page = HomePage(self.driver)
        home_page.get_name().send_keys(get_data["first_name"])
        home_page.get_email().send_keys(get_data["last_name"])
        self.select_option_by_text(HomePage.gender_select, get_data["gender"])
        home_page.click_submit()
        message = home_page.get_alert_message()
        assert "success" in message
        self.take_screenshot(get_data["filename"])
        self.driver.refresh()

    @pytest.fixture(params=FormSubmissionData.test_form_data)
    def get_data(self, request):
        return request.param
