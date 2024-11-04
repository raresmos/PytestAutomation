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

    product_btn = browser.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[2]/a")
    product_btn.click()
    expected_text = "ALL PRODUCTS"
    actual_text = browser.find_element(By.CLASS_NAME, "title.text-center").text
    assert expected_text in actual_text, f"The text '{expected_text}' was not found"

    search_input = browser.find_element(By.NAME, "search")
    search_input.send_keys("t-shirt")
    search_btn = browser.find_element(By.ID, "submit_search")
    search_btn.click()
    expected_txt = "SEARCHED PRODUCTS"
    actual_txt = browser.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/h2").text
    assert expected_txt in actual_txt, f"{expected_text} was not found"

    products_searched = browser.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div")
    visible_products = products_searched.find_elements(By.CLASS_NAME, "product-image-wrapper")
    product_count = len(visible_products)
    print(f"Number of product visible are: {product_count}")
    assert product_count > 0, "No products found"
