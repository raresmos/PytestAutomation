from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, MoveTargetOutOfBoundsException
from selenium.webdriver.common.action_chains import ActionChains
import time



def test_subscription_cartPage(browser):
    browser.get("https://www.automationexercise.com/")
    assert "Automation Exercise" in browser.title
    try:

        accept_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p")))
        accept_button.click()
    except:
        print("Pop-up is not visible")

    prod_btn = browser.find_element(By.CLASS_NAME, 'material-icons.card_travel')
    prod_btn.click()

    # Hover over the product and add to the cart
    product_hover = browser.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[4]/div/div[1]/div[1]/img")
    action = ActionChains(browser)
    action.move_to_element(product_hover).perform()
    add_cart = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[4]/div/div[1]/div[2]/div/a")))
    add_cart.click()

    continue_btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-success.close-modal.btn-block")))
    continue_btn.click()

    #Hover over the second prod and add to cart
    product_hover2 = browser.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[5]/div/div[1]/div[1]/img")
    browser.execute_script("arguments[0].scrollIntoView(true);", product_hover2)
    action = ActionChains(browser)
    action.move_to_element(product_hover2).perform()
    add_cart2 = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[5]/div/div[1]/div[2]/div/a")))
    add_cart2.click()

    #View Cart
    view_cart = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[1]/div/div/div[2]/p[2]/a/u")))
    view_cart.click()

    #Verify if both products are present in the cart
    prod_expected1 = "Sleeveless Dress"
    prod_expected2 = "Stylish Dress"
    products_details = [WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'Sleeveless Dress')]"))
    ).text, WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'Stylish Dress')]"))).text
    ]

    assert prod_expected1 and prod_expected2 in products_details


