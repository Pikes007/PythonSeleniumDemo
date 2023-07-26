from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[contains(@href,'shop')]")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.XPATH, "//input[@name = 'email']")
    gender_select = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    alert = (By.CLASS_NAME, "alert-success")

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        check_out_page = CheckoutPage(self.driver)
        return check_out_page

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def click_submit(self):
        self.driver.find_element(*HomePage.submit).click()

    def get_alert_message(self):
        return self.driver.find_element(*HomePage.alert).text



