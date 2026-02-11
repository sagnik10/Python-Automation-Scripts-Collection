import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_registration_and_checkout(driver):
    wait = WebDriverWait(driver, 30)

    def click(locator):
        el = wait.until(EC.element_to_be_clickable(locator))
        driver.execute_script("arguments[0].click();", el)

    def type_text(locator, value):
        el = wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(value)

    def get_text(locator):
        return wait.until(EC.visibility_of_element_located(locator)).text

    driver.get("https://automationexercise.com/login")

    click((By.LINK_TEXT, "Signup / Login"))

    type_text((By.NAME, "name"), "Test User")
    type_text((By.XPATH, "//input[@data-qa='signup-email']"), f"test{int(time.time())}@mail.com")
    click((By.XPATH, "//button[@data-qa='signup-button']"))

    wait.until(EC.visibility_of_element_located((By.ID, "id_gender1")))
    click((By.ID, "id_gender1"))
    type_text((By.ID, "password"), "Test@1234")
    type_text((By.ID, "first_name"), "Test")
    type_text((By.ID, "last_name"), "User")
    type_text((By.ID, "address1"), "Test Address")
    type_text((By.ID, "state"), "WB")
    type_text((By.ID, "city"), "Kolkata")
    type_text((By.ID, "zipcode"), "700001")
    type_text((By.ID, "mobile_number"), "9999999999")
    click((By.XPATH, "//button[@data-qa='create-account']"))

    wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Created!']")))

    driver.get("https://automationexercise.com/products")

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "productinfo")))

    click((By.XPATH, "(//a[@data-product-id='1'])[1]"))
    click((By.XPATH, "//button[text()='Continue Shopping']"))

    driver.get("https://automationexercise.com/view_cart")

    wait.until(EC.visibility_of_element_located((By.ID, "cart_info_table")))

    product_name = get_text((By.CSS_SELECTOR, ".cart_description a"))
    quantity = get_text((By.CSS_SELECTOR, ".cart_quantity button"))
    price = get_text((By.CSS_SELECTOR, ".cart_price p"))

    assert product_name.strip() != ""
    assert int(quantity) > 0
    assert price.strip() != ""

    click((By.LINK_TEXT, "Proceed To Checkout"))

    checkout_header = get_text((By.XPATH, "//h2[text()='Address Details']"))
    assert "Address" in checkout_header