from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time



def test_products_details(browser):
    browser.get("https://www.automationexercise.com/")
    assert "Automation Exercise" in browser.title
    try:

        accept_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p")))
        accept_button.click()
    except:
        print("Pop-up is not visible")

    products_btn = browser.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[2]/a")
    products_btn.click()
    expected_text = "ALL PRODUCTS"
    actual_text = browser.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/h2").text
    assert expected_text in actual_text, f"You are not in the products pages. Page: {actual_text}"

    view_product_btn = browser.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/ul/li/a")
    view_product_btn.click()
    expected_details = ['Blue Top', 'Women > Tops', 'Rs. 500', 'In Stock', 'New', 'Polo']
    actual_details = browser.find_element(By.CLASS_NAME, "product-information").text
    for text in expected_details:
        assert text in actual_details, f"'{expected_text}' are not present in product details"
