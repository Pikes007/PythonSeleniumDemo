from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    check_out = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    check_out_confirm = (By.CSS_SELECTOR, ".btn.btn-success")

    def get_card_elements(self):
        wait = WebDriverWait(self.driver, 10)
        cards = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "app-card")))
        return cards

    def select_item_by_name(self, item_name):
        cards = self.get_card_elements()
        for card in cards:
            item_name_element = card.find_element(By.CSS_SELECTOR, "h4.card-title a")
            if item_name_element.text == item_name:
                add_to_cart_button = card.find_element(By.XPATH, ".//button[contains(@class, 'btn')]")
                add_to_cart_button.click()
                break

    def check_out_items(self):
        return self.driver.find_element(*CheckoutPage.check_out)

    def complete_checkout(self):
        self.driver.find_element(*CheckoutPage.check_out_confirm).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page














