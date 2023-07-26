from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Selenium webdriver (make sure you have installed the appropriate webdriver for your browser)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)    #global wait
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/angularpractice/')

# Wait for the page to load
driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()
wait = WebDriverWait(driver, 10)
cards = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "app-card")))

# Loop through the cards and find the Blackberry item
for card in cards:
    item_name = card.find_element(By.CSS_SELECTOR, "h4.card-title a").text
    if item_name == "Blackberry":
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn')]")))
        add_to_cart_button.click()
        break

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
driver.find_element(By.CSS_SELECTOR, "#country").send_keys("in")

wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='India']")))
driver.find_element(By.XPATH, "//a[normalize-space()='India']").click()
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

alert = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'success')]")))
alert_text = alert.text
assert "Success! Thank you!" in alert_text
print(alert_text)
driver.get_screenshot_as_file("success.png")
driver.close()



