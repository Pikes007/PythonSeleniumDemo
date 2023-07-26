from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    country_input = (By.CSS_SELECTOR, "#country")
    checkbox = (By.XPATH, "//label[@for='checkbox2']")
    purchase = (By.XPATH, "//input[@value='Purchase']")
    alert_element = (By.XPATH, "//div[contains(@class, 'success')]")

    def enter_country(self, country):
        country_select = self.driver.find_element(*ConfirmPage.country_input)
        country_select.send_keys(country)
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, f"//a[normalize-space()='{country}']"))).click()
        except Exception as e:
            print(f"NonExistentCountry: Error: {e}")

    def select_checkbox(self):
        self.driver.find_element(*ConfirmPage.checkbox).click()

    def click_purchase(self):
        self.driver.find_element(*ConfirmPage.purchase).click()

    def get_success_alert_text(self):
        alert = self.wait.until(EC.visibility_of_element_located(self.alert_element))
        return alert.text


