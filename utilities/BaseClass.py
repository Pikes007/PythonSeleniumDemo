import inspect
import logging
import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def select_option_by_text(self, locator, text):
        dropdown_list = Select(self.driver.find_element(*locator))
        text_lower = text.lower()
        for option in dropdown_list.options:
            if option.text.strip().lower() == text_lower:
                option.click()
                break
        else:
            print(f"Text '{text}' not found in the dropdown options.")

    def take_screenshot(self, filename):
        self.driver.get_screenshot_as_file(filename)
